balance = 5000  
withdraw = float(input("Enter withdrawal amount: "))
remaining =float(balance) - float(withdraw)

if withdraw > balance:
    print("Insufficient balance!")
else:
   
    print("Transaction successful. Remaining balance:", remaining)
