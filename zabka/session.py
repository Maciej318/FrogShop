
current_user = None

def login(username):
    global current_user
    current_user = username


def logout():
    global current_user
    current_user = None

def get_current_user():
    return current_user

def is_logged_in():
    return current_user is not None