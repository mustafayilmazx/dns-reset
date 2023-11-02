import subprocess
import re
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_active_code_page():
    """
    Fetch the active Windows code page via the 'chcp' command.
    """
    try:
        output = subprocess.check_output('chcp', shell=True).decode()
        return re.search(r':\s+(\d+)', output).group(1)
    except subprocess.CalledProcessError as e:
        logging.error("Error fetching the active code page: %s", e.output)
        return '850'  # Default to code page 850 in case of an error

def get_network_adapters(code_page):
    """
    Retrieves the list of network adapters using the specified code page.
    """
    try:
        output = subprocess.check_output(
            "netsh interface ipv4 show config", 
            shell=True
        ).decode(encoding=f'cp{code_page}', errors='ignore')
        return output
    except subprocess.CalledProcessError as e:
        logging.error("Error fetching network adapter information: %s", e.output)
        return None

def reset_dns(adapter_name, code_page):
    """
    Resets the DNS settings for a given network adapter.
    """
    try:
        subprocess.run(
            f"netsh interface ipv4 set dns \"{adapter_name}\" dhcp", 
            shell=True,
            check=True,
            stderr=subprocess.PIPE
        )
        logging.info(f"DNS settings reset for adapter: {adapter_name}")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to reset DNS for %s: %s", adapter_name, 
                      e.stderr.decode(encoding=f'cp{code_page}', errors='ignore'))

def reset_dns_for_all_adapters(adapter_names, code_page):
    """
    Resets the DNS settings for all network adapters.
    """
    for adapter_name in adapter_names:
        reset_dns(adapter_name, code_page)

def user_interaction(adapter_names, code_page):
    """
    Handles user interaction to either reset all adapters or a specific one.
    """
    response = input("Do you want to reset all network adapters? (yes/no): ").strip().lower()
    if response == 'yes':
        reset_dns_for_all_adapters(adapter_names, code_page)
    else:
        adapter_to_reset = input("Enter the name of the adapter you want to reset: ").strip()
        if adapter_to_reset in adapter_names:
            reset_dns(adapter_to_reset, code_page)
        else:
            logging.error("Adapter not found: %s", adapter_to_reset)

def main():
    """
    The main function that orchestrates the DNS resetting process.
    """
    code_page = get_active_code_page()
    logging.info(f"Active code page: {code_page}")

    logging.info("Fetching network adapters...")
    network_adapters_output = get_network_adapters(code_page)
    if network_adapters_output:
        adapter_names = re.findall(r"Configuration for interface \"(.+)\"", network_adapters_output)
        logging.info("Found adapters: %s", ', '.join(adapter_names))

        user_interaction(adapter_names, code_page)

if __name__ == "__main__":
    main()
