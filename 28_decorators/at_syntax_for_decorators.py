import functools

user = {"username":"abcdefg", "access-level":"guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access-level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


@make_secure
def get_admin_password():
    return "P@ss1234"


# get_admin_password = make_secure(get_admin_password()) we need not assign the decorator function to the original
# function this way. We can simply write @decorator (i.e. @make_secure) just above the 'get_admin_password()'
print(get_admin_password())

'''
> if we print, 'print(get_admin_password.__name__)', we get secure_fucntion as output. This is because we replace 
  'get_admin_password()' with 'secure_function'. Also if there is any documentation as part of 'get_admin_password()'
  that gets deleted to. To avoid this, we need to import functools and add another decorator @functools.wraps(org 
  function name which you are decorating). This keeps the documentation of original function also
'''
