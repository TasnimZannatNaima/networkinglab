import subprocess
import shlex

command_line = "ping -c 1 127.0.0.1"

if __name__ == '__main__':
    args = shlex.split(command_line)
    try:
        subprocess.check_call(args,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        print("Your PC is up!")
    except subprocess.CalledProcessError:
        print("Failed to get ping.")
