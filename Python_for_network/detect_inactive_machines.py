import argparse
import time
import sched
from scapy.all import sr, IP, ICMP

RUN_FREQUENCY = 10
scheduler = sched.scheduler(time.time, time.sleep)

def detect_inactive_hosts(scan_hosts):
    global scheduler
    scheduler.enter(RUN_FREQUENCY, 1, detect_inactive_hosts, (scan_hosts,))
    inactive_hosts = []

    ans, unans = sr(IP(dst=scan_hosts)/ICMP(), timeout=1, retry=0)
    for snd, rcv in ans:
        print(rcv.src, "is alive")

    for pkt in unans:
        print(pkt.dst, "is inactive")
        inactive_hosts.append(pkt.dst)

    print("Total inactive hosts:", len(inactive_hosts))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--scan-hosts', required=True)
    args = parser.parse_args()

    scheduler.enter(1, 1, detect_inactive_hosts, (args.scan_hosts,))
    scheduler.run()
