from connections import *
from formatter import *
from menu import logo, menu

start = True


logo()

while start:
    answer = menu()
    match answer:
        case 1:
            set_either()
        case 2:
            process_hosts(jump_mode, docker_status)
        case 3:
            process_hosts(jump_mode, system_metrics)
        case 0:
            print("Goodbye.")
            start = False
        case _:
            print("Invalid parameter.")
