import dotenv
import os

var = dotenv.dotenv_values("../configurations/.env")
inner_ssh_key_filename = "../configurations/inner_key"
ssh_key_filename = os.getenv("HOME") + var.get("KEY")
server = var.get("BASTION")
final_target = "10.232.5.8"
user = var.get("USER")
bastion_private_ip = var.get("BASTION_PRIVATE_IP")
port = var.get("PORT")


def jump_set():
    try:
        config = dotenv.dotenv_values("../configurations/workspace.conf")
        jump_mode = config.get("JUMP_MODE")
        if jump_mode is not None:
            return jump_mode

    except Exception as e:
        print(
            f"{e}. The variable JUMP_MODE was not found. Creating file with default value of active..."
        )
    default_value = "active"
    with open("../configurations/workspace.conf", "w") as f:
        f.write(f"JUMP_MODE='{default_value}'")
    return default_value


def server_list_chooser():
    config = dotenv.dotenv_values("../configurations/workspace.conf")
    jump_mode = config.get("JUMP_MODE")
    if jump_mode == "active":
        s_list = var.get("SERVER_LIST")
        s_list = s_list.split(",")
        return s_list
    elif jump_mode == "inactive":
        s_list = var.get("SINGLE_SERVER_LIST")
        s_list = s_list.split(",")
        return s_list
    else:
        print("ERROR")


server_list = server_list_chooser()
