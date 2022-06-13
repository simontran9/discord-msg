import time, os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


load_dotenv()


browser = webdriver.Chrome()
discord_home = "https://discord.com/login"
browser.get(discord_home)
browser.maximize_window()


def calculate_time(time_send):
    current_time = str(datetime.now().time().strftime("%H:%M:%S"))
    current_time = datetime.strptime(current_time, "%H:%M:%S")
    difference_time = time_send - current_time
    difference_seconds = difference_time.total_seconds()
    return difference_seconds


def show_time():
    current_time = str(datetime.now().time().strftime("%H:%M:%S"))
    print("The current time is: " + str(current_time) + "\n")
    print("Input format: Hours:Minutes:Seconds")
    desired_time = input("What time do you want to send your message: ")
    desired_time = datetime.strptime(desired_time, "%H:%M:%S")
    return desired_time


def time_to_send():
    wrong_time = True
    while wrong_time:
        try:
            print()
            desired_time = show_time()
            difference = calculate_time(desired_time)
            if difference > 0:
                print("Nice!")
                wrong_time = False
            else:
                print("Your target time has passed! Please input a new time")
        except ValueError:
            print("Wrong thing format (format: Hours:Minutes:Seconds)\n")
    time.sleep(difference)


def fill_login_page(email, password):
    username_elem = browser.find_element(By.NAME, "email")
    password_elem = browser.find_element(By.NAME, "password")
    username_elem.send_keys(email)
    password_elem.send_keys(password)
    password_elem.submit()


def click_item(xpath, send_info=None, info=None):
    item = browser.find_element(By.XPATH, xpath)
    item.click()
    if send_info:
        item.send_keys(info)
    return item


def send():
    browser.implicitly_wait(40)
    click_item(os.environ.get("SEARCH_BAR"))
    click_item(
        os.environ.get("SEARCH_INPUT_BOX"), True, os.environ.get("FRIEND_USERNAME")
    )
    browser.implicitly_wait(20)
    click_item(os.environ.get("FRIEND_NAME_OPTION"))
    input_message = click_item(
        os.environ.get("MESSAGE_INPUT_BOX"), True, os.environ.get("MESSAGE")
    )
    input_message.send_keys(Keys.RETURN)
    print("Your message was successfully sent! Have a good day!")


def main():
    time_to_send()
    fill_login_page(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
    send()


if __name__ == "__main__":
    main()
