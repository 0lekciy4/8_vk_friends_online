# Watcher of Friends Online
This script prints in the terminal a list of your friends online in vk.
Before the first start, you must get **"APP_ID"** . To get **"APP_ID"**,
you need to register your
application at **https://vk.com/dev**

# Example run
Open the terminal, go to the directory where the file is located
and run **"python vk_friends_online.py"**, if python 3 as not default
try **"python3 vk_friends_online.py"**


```bash

$ python vk_friends_online.py
please enter APP_ID, or change variable APP_ID
in 'vk_friends_online.py': <your app_id>
Enter please your vk login
<your vk_login>
Enter please your vk password
<your vk_password>
Your friends online
<First_name1> <Last_name1>
<First_name2> <Last_name2>

. . .


```

# How to Install

Python 3 should be already installed.
Then use **pip** (or pip3 if there is a conflict with old Python 2 setup)
to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
