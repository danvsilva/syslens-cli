from connections import *
from formatter import *
from menu import logo, menu
from vars import *

start = True

logo()
jump_mode = jump_set()
j_print = f"""
JUMP MODE IS: {Bcolors.BLINK_WARNING}{jump_mode.upper()}{Bcolors.ENDC}"""
print(j_print)

while start:
    answer = menu()
    match answer:
        case 1:
            set_either()
            jump_mode = jump_set()
        case 2:
            process_hosts(jump_mode, docker_status)
        case 3:
            process_hosts(jump_mode, system_metrics)
        case 0:
            print("Goodbye.")
            start = False
        case _:
            print("Invalid parameter.")
