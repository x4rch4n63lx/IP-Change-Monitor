# IP-Change-Monitor

Created By     : x_4rch4n63l_x
Created On     : 1/7/2025 - 3:33AM
Script Purpose : Monitor and report public IP address changes
Description    : This script uses the 'requests' library to fetch the current public IP 
                 address and monitors it at a user-defined interval. It prints a message 
                 when the IP address changes.
                 
                 The script captures the public IP address repeatedly at the specified 
                 interval and compares it to the previous IP address. If the IP address 
                 changes, it prints the new IP address.
                 
                 The script also provides real-time feedback with a countdown timer during 
                 the waiting period between checks. Additionally, it includes error handling 
                 for network-related issues, ensuring the script continues to run smoothly.
                 If it cannot fetch the IP address, it will display a clean error message.
                 
Features       :
                 - User-defined monitoring interval.
                 - Real-time feedback with countdown timer.
                 - Detection and reporting of IP address changes.
                 - Graceful error handling for network issues with retries.
Requirements   :
                 - Python 3.x
                 - 'requests' library (install using `pip install requests`)
                 - 'halo' library (install using `pip install halo`)
