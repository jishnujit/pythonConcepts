# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 100

balance_amount = 0
while True:
    tran = input("Enter transaction: ")
    if not tran:
        break
    transaction_type = tran.split(" ")[0]
    transaction_amount = int(tran.split(" ")[1])
    if transaction_type == "D":
        balance_amount += transaction_amount
    else:
        balance_amount -= transaction_amount
    print(balance_amount)