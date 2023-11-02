# DNS Reset Script

This Python script is designed to reset the DNS settings for network adapters on a Windows system to their default settings, typically to obtain DNS server addresses automatically via DHCP.

## Prerequisites

To run this script, you will need:
- Python 3.6 or higher installed on your Windows machine.
- Administrative privileges on the system where the script will be executed.

## Installation

No installation is necessary. Simply download the `dns_reset.py` script from the repository.

## Usage

To use the script, follow these steps:

1. Open the Command Prompt or PowerShell with administrative privileges.
2. Navigate to the directory where you have downloaded the `dns_reset.py` file.
3. Run the script by entering `python dns_reset.py` and press Enter.

The script will first determine the active code page used by your system to handle potential encoding issues. It will then list all network adapters found on the system and prompt you to either reset the DNS settings for all adapters or to specify a single adapter to reset.

## Features

- Automatically detects the system's active code page for proper encoding handling.
- Provides an option to reset DNS settings for all network adapters.
- Allows for resetting DNS settings of a specific network adapter chosen by the user.

## Contributing

Contributions to this script are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements

- Thanks to the contributors who have helped in testing and refining the script.
- This project is not affiliated with or endorsed by any company.

## Disclaimer

This script is provided "as is", without warranty of any kind, express or implied. Use at your own risk.

## Contact

If you have any questions or feedback, please file an issue on the GitHub repository.

