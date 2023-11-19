import subprocess
import re

def execute_command(command):
    # Execute the command and capture the output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Decode the output from bytes to string
    output = output.decode('utf-8')

    return output

def get_ip_address(output):
    # Use regular expressions to extract the IP address
    pattern = r'Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(pattern, output)
    if match:
        ip_address = match.group(1)
        return ip_address

    return None


def url_to_ipadd(url):
    # Execute nslookup command with query type A
    result = execute_command('nslookup '+url+' -querytype=A')

    # Extract the IP address from the result
    ip_address = get_ip_address(result)

    # Print the IP address
    return ip_address
