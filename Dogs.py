import requests
import random
import json
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \___||_|\_\ 
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[Dogs Bot]---------------\033[0m\n\033[1;96m---------------------------------------\033[0m")    

def test_proxy(proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN + Style.BRIGHT}Proxy Connected: {proxy[:3]}.....{proxy[-3:]}")
            return True
    except:
        return False
    return False

def read_query_ids(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def login_with_proxy(query_id, proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "text/plain;charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    body = query_id
    response = requests.post(
        "https://api.onetime.dog/join",
        headers=headers,
        data=body,
        proxies=proxies,
        timeout=10
    )
    return response

def login_without_proxy(query_id):
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "text/plain;charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    body = query_id
    response = requests.post(
        "https://api.onetime.dog/join",
        headers=headers,
        data=body,
        timeout=10
    )
    return response

def check_task_completion(telegram_id, reference):
    url = f"https://api.onetime.dog/tasks?user_id={telegram_id}&reference={reference}"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    response = requests.get(url, headers=headers)
    return response

def verify_task_completion(slug, telegram_id, reference):
    url = f"https://api.onetime.dog/tasks/verify?task={slug}&user_id={telegram_id}&reference={reference}"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    response = requests.post(url, headers=headers)
    return response
    
def daily_reward(telegram_id):
    url = f"https://api.onetime.dog/rewards?user_id={telegram_id}"
    headers = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    response = requests.get(url, headers=headers)
    return response    

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')  # Clear the countdown message

def main():
    clear_terminal()
    art()

    use_proxy = input("Do you want to use proxy? (y/n): ").strip().lower()
    proxies = []

    if use_proxy == 'y':
        proxies = read_query_ids('proxy.txt')

    while True:  # Infinite loop to keep the script running
        query_ids = read_query_ids('data.txt')
        clear_terminal()
        art()

        for index, query_id in enumerate(query_ids, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{index}------")
            query_id = query_id.strip()

            if use_proxy == 'y':
                proxy = None
                while not proxy:
                    random_proxy = random.choice(proxies)
                    if test_proxy(random_proxy):
                        proxy = random_proxy
                response = login_with_proxy(query_id, proxy)
            else:
                response = login_without_proxy(query_id)

            if response.status_code == 200:
                try:
                    response_data = response.json()
                    telegram_id = response_data.get("telegram_id", "N/A")
                    reference = response_data.get("reference", "N/A")
                    balance = response_data.get("balance", "N/A")
                    username = response_data.get("username", "N/A")
                    print(f"{Fore.YELLOW + Style.BRIGHT}Name: {username}")
                    print(f"{Fore.YELLOW + Style.BRIGHT}Balance: {balance}")

                    # Check task completion
                    task_response = check_task_completion(telegram_id, reference)
                    if task_response.status_code == 200:
                        task_data = task_response.json()
                        for task in task_data:
                            slug = task.get("slug", "N/A")
                            complete = task.get("complete", False)
                            if complete:
                                print(f"{Fore.GREEN + Style.BRIGHT}Task Complete Successful: {slug}")
                            else:
                                verify_response = verify_task_completion(slug, telegram_id, reference)
                                if verify_response.status_code == 200:
                                    verify_response_data = verify_response.json()
                                    error_code = verify_response_data.get("error_code", "")
                                    if error_code == "already_complete":
                                        print(f"{Fore.GREEN + Style.BRIGHT}Task Complete Successful: {slug}")
                                    elif error_code == "not_verified":
                                        print(f"{Fore.RED + Style.BRIGHT}Task Not Complete: {slug}")
                                else:
                                    print(f"{Fore.RED + Style.BRIGHT}Task Verification Failed: {verify_response.text} for task {slug}")
                                    
                     # Claim daily reward
                        reward_response = daily_reward(telegram_id)
                        if reward_response.status_code == 200:
                            reward_data = reward_response.json()
                            daily = reward_data.get("daily", "N/A")
                            total = reward_data.get("total", "N/A")
                            print(f"{Fore.CYAN + Style.BRIGHT}Daily Reward: {daily}")
                            print(f"{Fore.YELLOW + Style.BRIGHT}New Balance: {total}")               

                except (ValueError, KeyError) as e:
                    print(f"{Fore.RED + Style.BRIGHT}Error parsing response JSON: {e}")
            else:
                print(f"{Fore.RED + Style.BRIGHT} Query ID date expired")

            countdown_timer(5)  # Wait for 5 seconds before the next account

        countdown_timer(24 * 60 * 60)  # Wait for 1 day before the next iteration

if __name__ == "__main__":
    main()
