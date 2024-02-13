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
volume_table = PrettyTable(
    ["Volume", "Size", "Used", "Available", "Percentage", "Mounted On"]
)


def docker_status(target):
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
            # docker_table.add_row([container_name, created_at, size, health_status])
            docker_table.add_row([name, created_at, size, status])
    print(docker_table)
    docker_table.clear_rows()


def disk_size(target):
    stdin, stdout, stderr = target.exec_command("df -h | tail -n +2")
    for line in stdout.read().split(b"\n"):
        stringed_line = str(line)
        # print(stringed_line)
        listed_data = stringed_line.split(" ")
        for element in listed_data:
            if element is None:
                listed_data.remove(listed_data)
            else:
                continue
        print(listed_data)
        # if len(listed_data) <= 1:
        #     continue
        # volume = listed_data[0].replace("b'", "")
        # size = listed_data[1]
        # used = listed_data[2]
        # avail = listed_data[3]
        # mounted_on = listed_data[5]
        # percentage = listed_data[4].replace("%'", "%")
    #     number_without_percent_sign = int(percentage.replace("%", ""))
    #     if 50 <= number_without_percent_sign <= 75:
    #         percentage = percentage.replace(
    #             f"{percentage}", f"{Bcolors.WARNING}{percentage}{Bcolors.ENDC}"
    #         )
    #     elif 76 <= number_without_percent_sign:
    #         percentage = percentage.replace(
    #             f"{percentage}", f"{Bcolors.FAIL}{percentage}{Bcolors.ENDC}"
    #         )
    #     else:
    #         percentage = percentage.replace(
    #             f"{percentage}", f"{Bcolors.OKGREEN}{percentage}{Bcolors.ENDC}"
    #         )
    #     volume_table.add_row([volume, percentage])
    # print(volume_table)
    # volume_table.clear_rows()
