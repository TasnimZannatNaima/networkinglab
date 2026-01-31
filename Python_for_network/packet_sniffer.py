import subprocess

if __name__ == '__main__':
    subprocess.call(["tcpdump", "-c", "1", "-i", "eth0"])
