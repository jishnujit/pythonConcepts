'''
> decorators allows us to easily modify functions, i.e. consider we have a function like below get_admin_password() and
  it should only return the password only of the access-level of user is admin. There may be many modules where we
  would have called get_admin_password() function. So just by adding an if stmt here to check the access level in this
  one snippet may not be enough. In such scenarios we use decorators
  user = {"username":"abcdefg", "access-level":"guest"}
> def get_admin_password():
      return "P@ss1234"
  print(get_admin_password())
> Ideally we need to write a function which need to check the user access level when we call the get_admin_password()
  function and not when we define it, i.e. while calling the get_admin_password() function it actually checks the user
  access-level and only based on that it calls the get_admin_password(). Decorator creates a function and replaces the
  original function with a secured one
'''

user = {"username":"abcdefg", "access-level":"guest"}


def get_admin_password():
    return "P@ss1234"


def make_secure(func):
    def secure_function():
        if user["access-level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function


get_admin_password = make_secure(get_admin_password())
print(get_admin_password())
