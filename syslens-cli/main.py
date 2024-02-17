from connections import *
from formatter import *
from menu import logo, menu

start = True


logo()

while start:
    answer = menu()
    match answer:
        case 1:
            process_hosts(docker_status)
        case 2:
            process_hosts(disk_size)
        case 0:
            print("Goodbye.")
            start = False
        case _:
            print("Invalid parameter.")
