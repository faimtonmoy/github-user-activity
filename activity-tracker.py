import requests


def get_user_name():
    user_input = input("Enter your user name: ")
    return user_input


def get_user_activity(user_name):
    url = f"https://api.github.com/users/{user_name}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def user_activity_tracker():
    user_name = get_user_name()
    user_activity = get_user_activity(user_name)
    print(user_activity)


user_activity_tracker()
