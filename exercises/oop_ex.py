"""
Design a simple banking system that demonstrates object-oriented principles.
The system should allow for creating multiple types of
bank accounts (e.g., checking and savings) with different behaviors,
 while ensuring that the core functionality (e.g., depositing, withdrawing, and checking balance)
 is shared across account types.
"""

import string
import secrets
import json


def generate_token():
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(7))
    return token


class Account:
    def __init__(self, email, password, is_account):
        self.action = ""
        self.token = generate_token()
        self.email = email
        self.password = password
        self.is_account = is_account
        self.read_data = read_from_json()
        self.value = 0
        self.savings = 0

        if self.is_account == 'new':
            new_user = self.add_user()
            write_to_json(new_user)
            print("You created your account!")
            self.manage_account()

        elif self.is_account == 'log':
            self.check = False
            self.known_user()
            if self.check:
                print('You logged in.')
                self.manage_account()
                self.update_account_value()
            else:
                print('Incorrect e-mail or password, please try again.')

    def manage_account(self):
        while True:
            print('\nCurrent balance:')
            print("Checkings: ", self.value)
            print("Savings: ", self.savings)

            action = input("\nWhat would you like to do? (deposit/withdraw/move/logout): ")

            if action == 'logout':
                print("Thank you for banking with us!")
                break

            self.operation_successful(action)
            self.update_account_value()

    def known_user(self):
        # Check if account exists
        for account in self.read_data['account_details']:
            if self.email == account['email'] and self.password == account['password']:
                self.value = account['balance']
                self.savings = account['savings']
                self.check = True

    def add_user(self):
        new_account = {'id': generate_token(), 'email': self.email, 'password': self.password, 'balance': 0,
                       'savings': 0}
        existing_accounts = self.read_data[f"account_details"]
        existing_accounts.append(new_account)

        return self.read_data

    def account_value(self, action):

        if action == 'deposit':
            deposit_value = self.numeric_input("How much would you like to deposit: ")
            if deposit_value:
                self.value += deposit_value
                return True

        elif action == 'withdraw':
            withdraw_value = self.numeric_input("How much would you like to withdraw: ")
            if withdraw_value:
                if self.value - withdraw_value >= 0:
                    self.value -= withdraw_value
                    return True

                print("Insufficient funds.")

        elif action == 'move':
            move_operation = input("Move to savings or withdraw from savings?: ")
            move_amount = self.numeric_input("How much would like to move: ")
            if move_amount:
                if move_operation == 'savings' and move_amount <= self.value:
                    self.savings += move_amount
                    self.value -= move_amount
                    return True

                elif move_operation == 'withdraw' and move_amount <= self.savings:
                    self.value += move_amount
                    self.savings -= move_amount
                    return True

            print("Insufficient funds.")
        return False

    def operation_successful(self, action):
        self.action = action
        if self.account_value(action):
            print("Operation successful!")

    def update_account_value(self):
        for account in self.read_data['account_details']:
            if self.email == account['email'] and self.password == account['password']:
                account['balance'] = self.value
                account['savings'] = self.savings

        write_to_json(self.read_data)

    def numeric_input(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("Please insert numeric value")
            return None


def read_from_json():
    try:
        with open("sample.json", "r") as outfile:
            try:
                load_data = json.load(outfile)
                # Check if structure is correct
                if "account_details" not in load_data:
                    load_data = {"account_details": []}
            except json.JSONDecodeError:
                # File is empty or invalid JSON
                load_data = {"account_details": []}
    except FileNotFoundError:
        # File doesn't exist, create initial structure
        load_data = {"account_details": []}

    return load_data


def write_to_json(data):
    with open("sample.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def start():
    welcoming_message = input(
        'Welcome to the bank! How can we help you? Type log-in in order to log-in into your account '
        'or new if you are a new client to our bank: ')
    if welcoming_message == 'new' or welcoming_message == 'log':
        mail = input('Please provide username: ')
        passw = input('Please provide password: ')
        Account(mail, passw, welcoming_message)


start()
