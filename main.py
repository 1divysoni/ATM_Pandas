import pandas as pd


def check_user(name, pin):
    try:
        df = pd.read_csv('Data.csv')
        username_present = df[(df['UserName'] == name) & (df['Pin'] == pin)]
        return not username_present.empty
    except Exception as e:
        return e


def update_data(name, pin, amount):
    try:
        df = pd.read_csv('Data.csv')
        condition = (df['UserName'] == name) & (df['Pin'] == pin)
        df.loc[condition, 'Amount'] = amount
        df.to_csv('Data.csv', index=False)
        return True
    except Exception as e:
        return e


def update_pin(name, pin):
    try:
        df = pd.read_csv('Data.csv')
        condition = (df['UserName'] == name)
        df.loc[condition, 'Pin'] = pin
        df.to_csv('Data.csv', index=False)
        return True
    except Exception as e:
        return e


def append(name, pin, amount):
    try:
        df = pd.read_csv('Data.csv')
        new_row = pd.DataFrame({'UserName': [name], 'Pin': [pin], 'Amount': [amount]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv('Data.csv', index=False)
        return True
    except Exception as e:
        return e


def delete(name, pin):
    try:
        df = pd.read_csv('Data.csv')
        condition = (df['UserName'] == name) & (df['Pin'] == pin)
        df = df[~condition]
        df.to_csv('Data.csv', index=False)
        return True
    except Exception as e:
        return e


def check_amount(pin):
    try:
        df = pd.read_csv('Data.csv')
        filtered_df = df[df['Pin'] == pin]
        if not filtered_df.empty:
            return filtered_df['Amount'].values[0]
        else:
            print("Number not found in the Data.")
    except Exception as e:
        return e


def withdrawal(name, pin, amount):
    try:
        CurrentAmount = check_amount(pin)
        if CurrentAmount > amount:
            newAmount = CurrentAmount-amount
            if update_data(name, pin, newAmount):
                return True
        else:
            print('Balance Is Not Enough In Your Account')
    except Exception as e:
        return e


def deposit(name, pin, amount):
    try:
        CurrentAmount = check_amount(pin)
        newAmount = CurrentAmount + amount
        if update_data(name, pin, newAmount):
            return True
    except Exception as e:
        return e


if __name__ == '__main__':
    print('Welcome Sir/Mam...')
    while True:
        print('\tselect command to execute\n\t1-Login.\n\t2-Create Account.\n\t3-Exit.')
        command = int(input())
        if command == 1:
            userName = input('Enter your user name')
            Pin = int(input('Enter Pin'))
            if check_user(userName, Pin):
                print(f'Welcome {userName}')
                while True:
                    print('\nselect command to execute\n\t1-Check Balance.\n\t2-Withdrawal.\n\t3-deposit.'
                          '\n\t4-Change Pin.\n\t5-Delete my account.\n\t6-Exit.')
                    command_second = int(input())
                    if command_second == 1:
                        print(check_amount(Pin))
                    elif command_second == 2:
                        withdrawal_amount = int(input('Enter Amount To Withdrawal'))
                        if withdrawal(userName, Pin, withdrawal_amount):
                            print('Withdrawal Successfully')
                        else:
                            print('Error')
                    elif command_second == 3:
                        deposit_amount = int(input('Enter Amount To Deposit'))
                        if deposit(userName, Pin, deposit_amount):
                            print('Deposit Successfully')
                        else:
                            print('Error')
                    elif command_second == 4:
                        new_pin = int(input('Enter New Pin'))
                        if update_pin(userName, new_pin):
                            print('Pin Updated')
                    elif command_second == 5:
                        while True:
                            print('You Want To Delete Your Account? Y/N')
                            command_third = input()
                            if command_third == 'Y':
                                if delete(userName, Pin):
                                    print('Account Deleted')
                                    exit()
                            elif command_third == 'N':
                                print('Account Delete Request Rejected')
                                break
                            else:
                                print('Select correct Option')
                    elif command_second == 6:
                        break
                    else:
                        print('Select correct Option')
            else:
                print('Account Not Found')
        elif command == 2:
            userName = input('Enter your user name')
            Pin = int(input('Enter Pin'))
            Amount = int(input('Deposit your first amount'))
            df = pd.read_csv('Data.csv')
            username_present = userName in df['UserName'].values or Pin in df['Pin'].values
            if not username_present:
                if append(userName, Pin, Amount):
                    print('Account Created Successfully Please login to continue')
            else:
                print('User name or pin already in use please enter unic user name or pin')
        elif command == 3:
            break
        else:
            print('Select correct Option')

#-------------------------------------------------END-------------------------------------------------------------
