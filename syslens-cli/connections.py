import paramiko
from vars import *
from menu import *
from formatter import Bcolors


def key_based_connect(bastion, username, ssh_key):
    pkey = paramiko.RSAKey.from_private_key_file(ssh_key)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(bastion, username=username, pkey=pkey)
    return client


def jump_to_target(client, target, bastion_priv_ip):
    bastion_transport = client.get_transport()
    src_addr = (bastion_priv_ip, 22)
    dest_addr = (target, 22)
    bastion_channel = bastion_transport.open_channel(
        "direct-tcpip", dest_addr, src_addr
    )
    return bastion_channel


def main_bastion_connector(host, func):
    connection = key_based_connect(server, user, ssh_key_filename)
    bastion_channel = jump_to_target(connection, host, bastion_private_ip)
    target = paramiko.SSHClient()
    target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target.connect(
        host,
        username=user,
        key_filename=inner_ssh_key_filename,
        sock=bastion_channel,
    )
    func(target)
    target.close()
    bastion_channel.close()


def direct_connector(host, func):
    target = key_based_connect(host, user, ssh_key_filename)
    func(target)
    target.close()


def process_hosts(jump, func):
    if jump == "active":
        host = hosts_selection(server_list)
        if type(host) is list:
            for vm in host:
                print(f"Connecting to: {vm}")
                main_bastion_connector(vm, func)
            print("")
            print(
                f"Choose the next option: (JUMP MODE: {Bcolors.BLINK_WARNING}{jump.upper()}{Bcolors.ENDC})"
            )
        else:
            print(f"Connecting to: {host}")
            main_bastion_connector(host, func)
            print("")
            print(
                f"Choose the next option: (JUMP MODE: {Bcolors.BLINK_WARNING}{jump.upper()}{Bcolors.ENDC})"
            )
    elif jump == "inactive":
        host = hosts_selection(server_list)
        if type(host) is list:
            for vm in host:
                print(f"Connecting to: {vm}")
                direct_connector(vm, func)
            print("")
            print(
                f"Choose the next option: (JUMP MODE: {Bcolors.BLINK_WARNING}{jump.upper()}{Bcolors.ENDC})"
            )
        else:
            print(f"Connecting to: {host}")
            direct_connector(host, func)
            print("")
            print(
                f"Choose the next option: (JUMP MODE: {Bcolors.BLINK_WARNING}{jump.upper()}{Bcolors.ENDC})"
            )
    else:
        print("Invalid parameter.")
