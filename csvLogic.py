import csv  # Importing everything from csv module
import os  # Importing Everything from os module

def account_look_up(username, password):
    """
    Check if the given username and password exist in the account information.

    Parameters:
        username (str): The username to look up.
        password (str): The password associated with the username.

    Returns:
        bool: True if the account with the given username and password exists, False otherwise.
    """
    # Open the CSV file
    with open('account_info.csv', mode='r') as file:
        reader = csv.reader(file)
        # Iterate through each row in the CSV file
        for row in reader:
            # Check if the username and password match
            if row[0] == username and row[1] == password:
                return True  # Account found
    return False  # Account not found

def account_creation(username, password):
    """
    Create a new account with the given username and password.

    Parameters:
        username (str): The username of the new account.
        password (str): The password of the new account.

    Notes:
        This function appends the new account information to the 'account_info.csv' file.
        Each row in the CSV file represents an account with columns: username, password, balance, and credit.

    """
    # Open the CSV file in append mode
    with open('account_info.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write the new account information to the CSV file
        writer.writerow([username, password, 0, 100])

def account_balance_checking(username):
    """
    Retrieve the checking account balance for the specified username.

    Parameters:
        username (str): The username of the account holder.

    Returns:
        str: The checking account balance of the specified user.
             Returns None if the username is not found.
    """
    with open('account_info.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[2]

def account_balance_savings(username):
    """
    Retrieve the savings account balance for the specified username.

    Parameters:
        username (str): The username of the account holder.

    Returns:
        str: The savings account balance of the specified user.
             Returns None if the username is not found.
    """
    with open('account_info.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[3]

def update_balance_checking(username, new_balance):
    """
    Update the checking account balance for the specified username.

    Parameters:
        username (str): The username of the account holder.
        new_balance (str): The new balance to be set for the checking account.
    """
    # Open the CSV file in read mode and create a temporary file to write the updated data
    with open('account_info.csv', mode='r') as file, open('temp_account_info.csv', mode='w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)

        # Iterate through each row in the CSV file
        for row in reader:
            # If the username matches, update the balance in the third column
            if row[0] == username:
                row[2] = new_balance
            # Write the row to the temporary file
            writer.writerow(row)

    # Replace the original CSV file with the temporary file
    os.remove('account_info.csv')
    os.rename('temp_account_info.csv', 'account_info.csv')

def update_balance_savings(username, new_balance):
    """
    Update the savings account balance for the specified username.

    Parameters:
        username (str): The username of the account holder.
        new_balance (str): The new balance to be set for the savings account.
    """
    # Open the CSV file in read mode and create a temporary file to write the updated data
    with open('account_info.csv', mode='r') as file, open('temp_account_info.csv', mode='w', newline='') as temp_file:
        reader = csv.reader(file)
        writer = csv.writer(temp_file)

        # Iterate through each row in the CSV file
        for row in reader:
            # If the username matches, update the balance in the fourth column
            if row[0] == username:
                row[3] = new_balance
            # Write the row to the temporary file
            writer.writerow(row)

    # Replace the original CSV file with the temporary file
    os.remove('account_info.csv')
    os.rename('temp_account_info.csv', 'account_info.csv')