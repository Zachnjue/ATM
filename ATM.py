account_balance = 500.25
deposit = 0
withdrawal = 0


def print_balance():
    print(f'Current Balance: {account_balance}')
    ATM_Summary()


def deposit_amount():
    while True:
        try:
            global deposit
            deposit = float(
                input("Please enter the amount you would like to deposit? \n"))
            global account_balance
            account_balance = account_balance + deposit
            print(f"The new account balance is: {account_balance}")
            ATM_Summary()
            break
        except:
            print("\nPlease enter only digits")
    return account_balance


def user_input():
    user_choice = input(
        "Select (D) for Deposit\nSelect (W) for Withdrawal\nSelect (B) for Account Balance\nSelect (Q) to Quit\n")
    while True:
        if user_choice == 'B':
            print_balance()
            break
        if user_choice == 'W':
            withdrawal_amount()
            break
        if user_choice == 'D':
            deposit_amount()
            break
        if user_choice == 'Q':
            ATM_Summary()
            break
        if user_choice != "O" or user_choice != "W" or user_choice != "Q":
            print("\nBad input....Please enter O,W,B or Q")
            user_choice = input(
                "Select (D) for Deposit\nSelect (W) for Withdrawal\nSelect (B) for Account Balance\nSelect (Q) to Quit\n")


def withdrawal_amount():
    while True:
        try:
            global withdrawal
            withdrawal = float(
                input("Please enter the amount you would like to withdraw: \n"))
            global account_balance
            while True:
                if withdrawal > account_balance:
                    print(
                        f"{withdrawal} is greater than your account balance of {account_balance}")
                    withdrawal = float(
                        input("Please enter the amount you would like to withdraw: \n"))
                else:
                    account_balance = account_balance - withdrawal
                    print(
                        f"Withdrawal amount was {withdrawal}Ksh current balance is {account_balance}Ksh")
                    break
            break
        except:
            print("Please enter your number in digits")
    return account_balance


def ATM_Summary():
    print("Thank you for banking with us.")


user_input()
