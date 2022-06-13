#!/usr/bin/env bash

echo "Creating .env file for user details and the HTML element's XPath"
touch .env
echo "# Input your information below
EMAIL=
PASSWORD=
FRIEND_USERNAME=
MESSAGE=

# If Discord updates the XPath, make the changes below to make sure it finds the elements
SEARCH_BAR='//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[1]/button'
SEARCH_INPUT_BOX='//*[@id="app-mount"]/div[2]/div/div[3]/div[2]/div/div/div/input'
FRIEND_NAME_OPTION='//*[@id="quick-switcher-uid_29-item-1"]/div/div[2]'
MESSAGE_INPUT_BOX='//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]'" >> .env
wait 

echo "Create Python virtual environment"
python3 -m venv venv
wait

echo "Activating venv"
source venv/bin/activate
wait

echo "Installing dependencies"
pip install -r requirements.txt
wait
