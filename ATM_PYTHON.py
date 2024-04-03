import time

print("please enter your CARD")

time.sleep(5)

password = 1234
recipient_ID = 98765

pin = int(input("enter your atm pin"))

balnce = 10000

if pin == password:
    while True:

        print("""
              1 == Balance
              2 == Withdraw balance
              3 == Deposit balance
              4 == Transfer
              5 == Transction History
              6 == Quit
              """)
        try:
            option = int(input("please enter your choice"))
        except:
            print("please enter valid option")
        if option == 1:
            print(f"your current balance is {balance}")
        if option == 2:
            withdraw_amount =int(input("please enter withdraw_amount"))
            balance=balance=withdraw_amount
            print(f"{withdraw_amount}is debited from your account")
            print(f"your updated balance is{balance}")
        if option==3:
            deposit_amount=int(input("please enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"{deposit_amount}is credited to your account")
            print(f"your updted balance is {balance}")
        if option ==4:
            transfer=int(input("please enter trafer amount:"))
            recipient =recipient_ID+transfer
            print(f"{transfer}is credited to your account")
            print(f"your updated recipient is{recipient_ID}")
        if option ==5:
            transaction_hisroty=int(input("enter recipient_id"))
            transaction_hisroty=transaction_hisroty+recipient_ID
            print(f"{transaction_hisroty}is transaction history ")
            print(f"your updated history is{transaction_hisroty}")
        if option ==6:
            break
  
else:
    print("wrong pin please try again")

        

        
        
