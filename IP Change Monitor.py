# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 1/7/2025 - 3:33AM
# Script Purpose : Monitor and report public IP address changes
# Description    : This script uses the 'requests' library to fetch the current public IP 
#                  address and monitors it at a user-defined interval. It prints a message 
#                  when the IP address changes.
#                  
#                  The script captures the public IP address repeatedly at the specified 
#                  interval and compares it to the previous IP address. If the IP address 
#                  changes, it prints the new IP address.
#                  
#                  The script also provides real-time feedback with a countdown timer during 
#                  the waiting period between checks. Additionally, it includes error handling 
#                  for network-related issues, ensuring the script continues to run smoothly.
#                  If it cannot fetch the IP address, it will display a clean error message.
#                  
# Features       :
#                  - User-defined monitoring interval.
#                  - Real-time feedback with countdown timer.
#                  - Detection and reporting of IP address changes.
#                  - Graceful error handling for network issues with retries.
# Requirements   :
#                  - Python 3.x
#                  - 'requests' library (install using `pip install requests`)
#                  - 'halo' library (install using `pip install halo`)
# ===================================================================================
import requests
import time
from halo import Halo

def get_public_ip():
    max_retries = 5
    backoff_factor = 2
    for i in range(max_retries):
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=10)
            response.raise_for_status()
            return response.json()["ip"]
        except requests.RequestException:
            time.sleep(backoff_factor ** i)
    print("Unable to fetch public IP.")
    return None

def monitor_ip(interval):
    previous_ip = get_public_ip()
    if previous_ip is None:
        print("Unable to fetch initial IP address. Exiting.")
        return
    print(f"Current IP: {previous_ip}")

    while True:
        spinner = Halo(text=f"Waiting for {interval} seconds", spinner='dots')
        spinner.start()
        for i in range(interval, 0, -1):
            spinner.text = f"Waiting for {i} seconds"
            time.sleep(1)
        spinner.stop()

        current_ip = get_public_ip()
        if current_ip is None:
            print("Error fetching current IP address. Retrying...")
            continue
        if current_ip != previous_ip:
            print(f"IP changed to: {current_ip}")
            previous_ip = current_ip

def main():
    try:
        interval = int(input("Enter check interval (seconds): "))
        if interval <= 0:
            raise ValueError("Interval must be a positive integer.")
        monitor_ip(interval)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == '__main__':
    main()
