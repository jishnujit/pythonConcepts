'''Check online'''
import functools

user = {"username":"abcdefg", "access-level":"billing"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access-level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "P@ss1234"
    elif panel == "billing":
        return "super_secret_password"


print(get_password("billing"))
