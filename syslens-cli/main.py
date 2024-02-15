from connections import *
from vars import *
from formatter import *
from menu import logo, menu, hosts_selection

start = True


def main(host, func):
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


logo()

while start:
    answer = menu()
    match answer:
        case 1:
            host = hosts_selection(server_list)
            if type(host) is list:
                for vm in host:
                    print(f"Connecting to: {vm}")
                    main(vm, docker_status)
                print("")
                print("Choose the next option: ")
            else:
                print(f"Connecting to: {host}")
                main(host, docker_status)
                print("")
                print("Choose the next option: ")
        case 2:
            host = hosts_selection(server_list)
            if type(host) is list:
                for vm in host:
                    print(f"Connecting to: {vm}")
                    main(vm, disk_size)
                print("")
                print("Choose the next option: ")
            else:
                print(f"Connecting to: {host}")
                main(host, disk_size)
                print("")
                print("Choose the next option: ")
        case 0:
            print("Goodbye.")
            start = False
        case _:
            print("Invalid parameter.")
