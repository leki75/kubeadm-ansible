#!/usr/bin/env python
import json
import subprocess
import sys


def main():
    cmd = "vagrant ssh-config"
    config = subprocess.check_output(cmd.split(), text=True)

    host = ""
    hosts = {}
    for line in config.split('\n'):
        line = line.strip()
        if line == '':
            continue

        (key, value) = line.split(' ', 2)
        if key == 'Host':
            host = value
            hosts[host] = {}
        elif key == 'HostName':
            hosts[host]['ansible_ssh_host'] = value
        elif key == 'Port':
            hosts[host]['ansible_ssh_port'] = value
        elif key == 'User':
            hosts[host]['ansible_ssh_user'] = value
        elif key == 'IdentityFile':
            hosts[host]['ansible_ssh_private_key_file'] = value

    result = {
        'all': {'hosts': [h for h in hosts]},
        '_meta': {'hostvars': hosts},
    }

    json.dump(result, sys.stdout, indent=2)

if __name__ == '__main__':
    main()
