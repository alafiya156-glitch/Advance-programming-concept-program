
# 20. Write a Python program to store bank transactions in a file
# and calculate the final account balance.

file = open("transactions.txt", "w")

file.write("Deposit,5000\n")
file.write("Withdraw,1000\n")
file.write("Deposit,2000\n")
file.write("Withdraw,500\n")

file.close()

balance = 0

file = open("transactions.txt", "r")

for line in file:
    data = line.strip().split(",")

    transaction = data[0]
    amount = int(data[1])

    if transaction == "Deposit":
        balance += amount
    elif transaction == "Withdraw":
        balance -= amount

file.close()

print("Final Account Balance:", balance)