# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
# range 0 and n.

class Gen:

    def divisible_by_7(self, n):
        for num in range(1, n+1):
            if num % 7 == 0:
                yield num


gen_object = Gen()
limit = int(input("Enter a limit: "))
generate = gen_object.divisible_by_7(limit)
for number in generate:
    print(number)
