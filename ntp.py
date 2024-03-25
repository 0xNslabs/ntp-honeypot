import os
import time
import argparse
import struct
from struct import unpack, pack
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
from twisted.python import log

script_dir = os.path.dirname(os.path.abspath(__file__))


class SimpleNTPProtocol(DatagramProtocol):
    NTP_TIMESTAMP_DELTA = 2208988800

    def get_ntp_request_type(self, mode):
        mode_to_request_type = {
            0: "Reserved",
            1: "Symmetric Active",
            2: "Symmetric Passive",
            3: "Client",
            4: "Server",
            5: "Broadcast",
            6: "NTP Control Message",
            7: "Private Use",
        }
        return mode_to_request_type.get(mode, "Unknown")

    def system_time_to_ntp(self, time_):
        return int(time_ + self.NTP_TIMESTAMP_DELTA) << 32

    def datagramReceived(self, data, addr):
        if len(data) < 48:
            return
        try:
            client_ip, client_port = addr
            log.msg(f"NTP Request - Client IP: {client_ip}, Port: {client_port}")

            unpacked = unpack("!B B b b I I 4s Q Q Q Q", data[:48])
            (
                leap_ver_mode,
                stratum,
                poll,
                precision,
                root_delay,
                root_dispersion,
                ref_id,
                ref_ts,
                orig_ts,
                recv_ts,
                trans_ts,
            ) = unpacked

            leap = leap_ver_mode >> 6
            version = leap_ver_mode >> 3 & 0x07
            mode = leap_ver_mode & 0x07
            mode = int(mode)
            version = int(version)
            request_type = self.get_ntp_request_type(mode)

            log.msg(
                f"Leap: {leap}, Version: {version}, Mode: {mode}, Request Type: {request_type}, Stratum: {stratum}"
            )

            if mode == 3:
                recv_timestamp = unpacked[8]
                tx_timestamp = self.system_time_to_ntp(time.time())
                response = pack(
                    "!B B b b I I 4s Q Q Q Q",
                    36,
                    1,
                    0,
                    0,
                    0,
                    0,
                    b"LOCL",
                    0,
                    recv_timestamp,
                    tx_timestamp,
                    tx_timestamp,
                )
                self.transport.write(response, addr)
        except Exception as e:
            log.msg(f"Error processing NTP request: {e}")


def main():
    parser = argparse.ArgumentParser(description="Run a simple NTP honeypot server.")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host interface to bind the NTP server to.",
    )
    parser.add_argument(
        "--port", type=int, default=123, help="Port to bind the NTP server to."
    )
    args = parser.parse_args()

    LOG_FILE_PATH = os.path.join(script_dir, "ntp_honeypot.log")
    print(f"NTP HONEYPOT ACTIVE ON HOST: {args.host}, PORT: {args.port}")
    print(f"ALL attempts will be logged in: {LOG_FILE_PATH}")
    log_observer = log.FileLogObserver(open(LOG_FILE_PATH, "a"))
    log.startLoggingWithObserver(log_observer.emit, setStdout=False)

    reactor.listenUDP(args.port, SimpleNTPProtocol(), interface=args.host)
    reactor.run()


if __name__ == "__main__":
    main()
