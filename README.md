# syslens-cli
## Overview
Syslens-CLI is a Python-based command-line interface tool designed for remote server management, specifically focusing on container status and system performance metrics. It uses SSH for secure communication and provides an intuitive interface for system administrators to manage multiple hosts efficiently.

## Features
1. **Container Status and Health Check:** Displays the status and health of Docker containers running on remote hosts.
2. **System Performance and Disk Space Monitoring:** Provides a detailed view of disk usage and system performance metrics.
3. **Key-Based SSH Connection:** Securely connects to remote servers using SSH keys, eliminating the need for passwords.
4. **Bastion Host Support:** Allows connection through a bastion host for enhanced network security.
5. **Color-Coded Outputs:** Utilizes color coding in the terminal for easy identification of different statuses (e.g., healthy, unhealthy).

## Installation
1. Ensure Python 3 and pip are installed on your system.
2. Install required Python libraries:
   ```bash
   pip install paramiko prettytable
   ```
3. Clone the Syslens-CLI repository from GitHub or download the source code.
4. Set up the configuration file with your server details and SSH keys (see Configuration section).

## Configuration
1. Create a `.env` file in the `configurations` directory with the following structure:
   ```
   SERVER_LIST=<comma-separated list of servers>
   BASTION=<bastion host>
   BASTION_PRIVATE_IP=<private IP of bastion host>
   USER=<SSH username>
   KEY=<path to SSH key file>
   PORT=<SSH port, default is 22>
   ```
2. Place your SSH private key files in the `configurations` directory.

## Usage
Run the program from the command line:
```bash
python syslens-cli.py
```
Follow the interactive menu to choose between checking container statuses, disk space, or exiting the application.

### Commands
- **1**: Verify container status and health of hosts.
- **2**: Check system performance and disk space of hosts.
- **0**: Exit the application.

## Dependencies
- Python 3
- Paramiko (for SSH connections)
- PrettyTable (for formatted terminal outputs)
- dotenv (for environment variable management)

## Note
This application assumes SSH access is properly set up and reachable from the machine where Syslens-CLI is run. Ensure all target servers are configured to accept the provided SSH keys for authentication.

## Disclaimer
Syslens-CLI is intended for experienced system administrators. Improper usage or configuration might lead to inaccessible systems or security vulnerabilities. Always test in a controlled environment before deploying to production.

## Support and Contribution
For support, feature requests, or contributions, please open an issue on the project's GitHub page.

## License
Syslens-CLI is released under the MIT License. See the LICENSE file for more details.