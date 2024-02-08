import dotenv
import os

ssh_key_filename = os.getenv("HOME") + "/.ssh/id_rsa"
inner_ssh_key_filename = "./inner_key"
var = dotenv.dotenv_values(".env")

server_list = var.get("SERVER_LIST")
server = var.get("BASTION")
final_target = "10.232.5.8"
user = var.get("USER")
bastion_private_ip = var.get("BASTION_PRIVATE_IP")
port = var.get("PORT")

server_list = server_list.split(",")
