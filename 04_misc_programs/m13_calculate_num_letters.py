my_string = "Hello World 123"
alpha_count = 0
digit_count = 0
for char in my_string:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
print(f"Letters {alpha_count}")
print(f"Digits {digit_count}")