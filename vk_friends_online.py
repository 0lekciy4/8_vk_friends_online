from getpass import getpass

import vk

APP_ID = 0


def get_user_login():
    user_login = input('Enter please your vk login\n')
    return user_login


def get_user_password():
    user_password = getpass('Enter please your vk password\n')
    return user_password


def get_online_friends(login, password, v='5.73', lang='ru', timeout=10):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends',
        )
        api = vk.API(session, v=v, lang=lang, timeout=timeout)
        friends_online_ids = api.friends.getOnline()
        friends_online = (api.users.get(user_ids=friends_online_ids))
        return friends_online
    except vk.exceptions.VkAuthError:
        return None


def output_friends_to_console(friends_online):
    if friends_online:
        print('Your friends online')
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])
    else:
        print('All your friends are offline')


def main():
    login = get_user_login()
    password = get_user_password()
    if login and password:
        friends_online = get_online_friends(login, password)
        if friends_online is not None:
            output_friends_to_console(friends_online)
        else:
            print('Incorrect password or login')
    else:
        print('Login and password must be non-empty')


if __name__ == '__main__':
    main()
