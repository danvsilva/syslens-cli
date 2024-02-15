from connections import *
from vars import *
from formatter import *
from menu import logo, menu

start = True

#     Main:
#         Initialize a list to hold container health statuses
#         For each VM in the list of designated VMs:
#             Establish an SSH connection to the VM
#             For each Docker container in the VM:
#                 Check the health status of the container
#                 Add the VM, container name, and health status to the list
#             Close the SSH connection
#         Display the results in a color-coded table


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
            for vm in server_list:
                print(f"Connecting to: {vm}")
                main(vm, docker_status)
        case 2:
            for vm in server_list:
                print(f"Connecting to: {vm}")
                main(vm, disk_size)
        case 0:
            start = False
        case _:
            print("Invalid parameter.")
    print("")
    print("Choose the next option: ")
