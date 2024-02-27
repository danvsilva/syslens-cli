import dotenv
import os

var = dotenv.dotenv_values("../configurations/.env")
inner_ssh_key_filename = "../configurations/inner_key"
ssh_key_filename = os.getenv("HOME") + var.get("KEY")
server_list = var.get("SERVER_LIST")
server = var.get("BASTION")
final_target = "10.232.5.8"
user = var.get("USER")
bastion_private_ip = var.get("BASTION_PRIVATE_IP")
port = var.get("PORT")

server_list = server_list.split(",")


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
