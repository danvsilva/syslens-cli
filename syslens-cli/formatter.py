from prettytable import PrettyTable


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    BLINK = "\033[5m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BLINK_WARNING = BLINK + WARNING


# docker ps --format '{{.Names}},{{.CreatedAt}},{{.Size}},{{.Status}}'
docker_table = PrettyTable(["Container Name", "Created At", "Size", "Health Status"])
volume_table = PrettyTable(
    ["Volume", "Size", "Used", "Available", "Percentage", "Mounted On"]
)
volume_table.title = "Filesystem Volume Overview"
system_table = PrettyTable(
    [
        "Total Memory",
        "Memory Used",
        "Free Memory",
        "Shared Memory",
        "Buffered/Cache",
        "Available",
    ]
)
system_table.title = "System Memory and CPU Metrics"
delinquent_processes_table = PrettyTable(["Process ID", "%CPU", "Command"])
delinquent_processes_table.title = "Top 10 CPU Hogging Processes"


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
        listed_data = list(filter(bool, listed_data))
        # print(listed_data)
        if len(listed_data) <= 1:
            continue
        volume = listed_data[0].replace("b'", "")
        size = listed_data[1]
        used = listed_data[2]
        avail = listed_data[3]
        mounted_on = listed_data[5].replace("'", "")
        percentage = listed_data[4].replace("%'", "%")
        number_without_percent_sign = int(percentage.replace("%", ""))
        if 50 <= number_without_percent_sign <= 75:
            percentage = percentage.replace(
                f"{percentage}", f"{Bcolors.WARNING}{percentage}{Bcolors.ENDC}"
            )
        elif 76 <= number_without_percent_sign:
            percentage = percentage.replace(
                f"{percentage}", f"{Bcolors.FAIL}{percentage}{Bcolors.ENDC}"
            )
        else:
            percentage = percentage.replace(
                f"{percentage}", f"{Bcolors.OKGREEN}{percentage}{Bcolors.ENDC}"
            )
        # ["Volume", "Size", "Used", "Available", "Percentage", "Mounted On"]
        volume_table.add_row([volume, size, used, avail, percentage, mounted_on])
    print(volume_table)
    volume_table.clear_rows()


def system_metrics(target):
    # ps -e --sort=-pcpu -o pid,pcpu,comm | head -n 11
    # free -h
    # uptime
    stdin, stdout, stderr = target.exec_command(
        """free -h | awk 'NR==2 {print $2 "," $3 "," $4 "," $5 "," $6 "," $7}'"""
    )
    for line in stdout.read().split(b"\n"):
        stringed_line = str(line)
        # print(stringed_line)
        listed_data = stringed_line.split(",")
        # print(listed_data)
        if len(listed_data) <= 1:
            continue
        t_memory = listed_data[0].replace("b'", "")
        t_memory_float = float(t_memory.replace("Gi", ""))
        m_used = listed_data[1]
        m_used_float = float(m_used.replace("Gi", ""))
        f_memory = listed_data[2]
        s_memory = listed_data[3]
        buffed_m = listed_data[4]
        a_memory = listed_data[5].replace("'", "")
        if (
            t_memory_float / 2
            <= m_used_float
            < (t_memory_float / 2) + (t_memory_float / 4)
        ):
            m_used = m_used.replace(
                f"{m_used}", f"{Bcolors.WARNING}{m_used}{Bcolors.ENDC}"
            )
        elif m_used_float > (t_memory_float / 2) + (t_memory_float / 4):
            m_used = m_used.replace(
                f"{m_used}", f"{Bcolors.FAIL}{m_used}{Bcolors.ENDC}"
            )
        else:
            m_used = m_used.replace(
                f"{m_used}", f"{Bcolors.OKGREEN}{m_used}{Bcolors.ENDC}"
            )
        system_table.add_row([t_memory, m_used, f_memory, s_memory, buffed_m, a_memory])
    print(system_table)
    system_table.clear_rows()

    disk_size(target)
