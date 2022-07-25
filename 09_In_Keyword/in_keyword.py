'''
In keyword is used to check the membership whether one thing is inside a list/tuple/set
'''
friends = ["bob", "rolf", "anne"]
print("anne" in friends)
movies = {"the matrix", "the avengers", "black widow"}
user_watched = input("Enter any of the movies watched recently: ").lower()
print(user_watched in movies)
if user_watched in movies:
    print(f"I have watched {user_watched} too!")
else:
    print(f"I haven't watched {user_watched} yet!")

