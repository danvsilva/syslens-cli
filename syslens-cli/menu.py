# Ask the operator what he wants to do.
from prettytable import PrettyTable


def logo():
    print(
        """\

	     _______.____    ____  _______. __       _______ .__   __.      _______.         ______  __       __  
	    /       |\   \  /   / /       ||  |     |   ____||  \ |  |     /       |        /      ||  |     |  | 
	   |   (----` \   \/   / |   (----`|  |     |  |__   |   \|  |    |   (----` ______|  ,----'|  |     |  | 
	    \   \      \_    _/   \   \    |  |     |   __|  |  . `  |     \   \    |______|  |     |  |     |  | 
	.----)   |       |  | .----)   |   |  `----.|  |____ |  |\   | .----)   |          |  `----.|  `----.|  | 
	|_______/        |__| |_______/    |_______||_______||__| \__| |_______/            \______||_______||__| 


	"""
    )
    print("Welcome to Syslens-CLI: What do you want to do?:")


def menu():
    print(
        """
	1. Verify container status and health of hosts
	2. Check System performance and Disk Space of hosts
	0. Exit
	"""
    )
    answer = int(input("1, 2 or 0: "))
    return answer


def hosts_selection(servers):
    to_select_hosts = {}
    num_of_host = 0
    server_table = PrettyTable(["ID Number", "Hosts Available"])
    if len(servers) == 1:
        return str(servers[0])
    print("Choose a Host from the List: ")
    for host in servers:
        to_select_hosts[num_of_host] = host
        server_table.add_row([num_of_host, host])
        num_of_host += 1
    print(server_table)
    server_table.clear_rows()
    selected_host = input("Input Host Number or 'a' for All Hosts: ").lower()
    print("")
    if selected_host == "a":
        return servers
    else:
        selected_host = int(selected_host)
        return to_select_hosts[selected_host]
