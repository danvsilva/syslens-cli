from prettytable import PrettyTable


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# docker ps --format '{{.Names}},{{.CreatedAt}},{{.Size}},{{.Status}}'
docker_table = PrettyTable(["Container Name", "Created At", "Size", "Health Status"])


def add_rows(container_name, created_at, size, health_status):
    docker_table.add_row([container_name, created_at, size, health_status])


def commands_to_execute(target):
    stdin, stdout, stderr = target.exec_command(
        "docker ps --format '{{.Names}},{{.CreatedAt}},{{.Size}},{{.Status}}'"
    )
    for line in stdout.read().split(b"\n"):
        stringed_line = str(line)
        # print(stringed_line)
        listed_data = stringed_line.split(",")
        # print(listed_data)
        if len(listed_data) < 4:
            continue
        else:
            name = listed_data[0]
            name = name.replace("b'", "")
            created_at = listed_data[1]
            size = listed_data[2]
            status = listed_data[3]
            status = status.replace("'", "")
            if "(healthy)" in status:
                status = status.replace(
                    "(healthy)", f"{Bcolors.OKGREEN}HEALTHY{Bcolors.ENDC}"
                )
            elif "(unhealthy)" in status:
                status = status.replace(
                    "(unhealthy)", f"{Bcolors.WARNING}UNHEALTHY{Bcolors.ENDC}"
                )
            else:
                pass
            add_rows(name, created_at, size, status)
    print(docker_table)
    docker_table.clear_rows()
