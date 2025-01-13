#!/usr/bin/python3

class Checkbook:
    """
    A class to manage a simple checkbook with deposit and withdrawal functionality.
    
    Attributes:
        balance (float): The current balance in the checkbook.
    """
    
    def __init__(self):
        """
        Initialize a new Checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.
        
        Parameters:
            amount (float): The amount to deposit. Must be positive.
            
        Returns:
            bool: True if deposit was successful, False otherwise.
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
            
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds are available.
        
        Parameters:
            amount (float): The amount to withdraw. Must be positive.
            
        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
            
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return False
            
        self.balance -= amount
        print("Withdrew ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return True

    def get_balance(self):
        """
        Display the current balance.
        
        Returns:
            float: The current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))
        return self.balance

def get_valid_amount(prompt):
    """
    Helper function to get a valid monetary amount from user input.
    
    Parameters:
        prompt (str): The input prompt to display to the user.
        
    Returns:
        float: The valid amount entered by the user.
        None: If the input was invalid or negative.
    """
    try:
        amount = float(input(prompt))
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return None
        return amount
    except ValueError:
        print("Error: Please enter a valid number.")
        return None

def main():
    """
    Main function to run the checkbook program.
    Handles user input and manages the checkbook operations.
    """
    cb = Checkbook()
    
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").lower()
            
            if action == 'exit':
                print("Thank you for using the checkbook program. Goodbye!")
                break
                
            elif action == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:
                    cb.deposit(amount)
                    
            elif action == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:
                    cb.withdraw(amount)
                    
            elif action == 'balance':
                cb.get_balance()
                
            else:
                print("Invalid command. Please use deposit, withdraw, balance, or exit.")
                
        except KeyboardInterrupt:
            print("\nProgram terminated by user. Goodbye!")
            break
        except EOFError:
            print("\nProgram terminated. Goodbye!")
            break

if __name__ == "__main__":
    main()
