def bank():
    print("Welcome to Chase bank.")
    in_session = True
    current_balance = 0
    while in_session:
        action = input("What would you like to do? (deposit, withdraw, check balance) ")
        if action == "check balance":
            print("Your current balance is {}".format(current_balance))
        elif action == "deposit":
            amount = input("How much would you like to deposit? ")
            current_balance += int(amount)
            print("New balance is {}".format(current_balance))
        elif action == "withdraw":
            amount = input("How much would you like to withdraw? ")
            current_balance -= int(amount)
            print("New balance is {}".format(current_balance))
        else:
            print("Action unrecognized")

        another_transaction = input("Another transaction or finish? (another, finish) ")
        if another_transaction == "finish":
            in_session = False
            print("Have a nice day!")
        elif another_transaction == "another":
            in_session = True

bank()
