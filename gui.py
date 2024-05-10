from tkinter import *
from csvLogic import *
'''
Import statement 1 imports everything from tkinter to be able to create
    the gui
Import statement 2 imports everything from csvLogic to be able to 
    use the functions within the file
'''

class GUI:
    """
    Class representing the graphical user interface of the application.
    """
    def __init__(self, window):

        """
        Initialize the GUI with login elements.

        Parameters:
            window: The main window of the GUI.

        Attributes:
            window (Tk): The main Tkinter window.
            self.login_attempt (int): Counter for login attempts.
            self.temp_variable_1 (str): Temporary variable 1.
            self.temp_variable_2 (str): Temporary variable 2.
            self.account_type (int): Counter for account type
            self.frame_one_login (Frame): Frame for username entry.
            self.label_username (Label): Label for username entry.
            self.entry_username (Entry): Entry field for username.
            self.frame_two_login (Frame): Frame for password entry.
            self.label_password (Label): Label for password entry.
            self.entry_password (Entry): Entry field for password.
            self.frame_three_login (Frame): Frame for login button.
            self.button_login (Button): Login button.
            self.frame_four_login (Frame): Frame for displaying messages.
            self.label_questions (Label): Label for displaying messages.
            self.frame_one_application (Frame): Frame for displaying application.
            self.button_checking (Button): Checking button.
            self.button_savings (Button): Savings button.
            self.button_exit (Button): Exit button.
            self.frame_two_application (Frame): Frame for displaying application.
            self.label_account_type (Label): Label for displaying account type.
            self.frame_three_application (Frame): Frame for displaying application.
            self.button_info (Button): Account information button.
            self.button_withdraw (Button): Withdraw button.
            self.button_deposit (Button): Deposit button.
            self.frame_application_info_one (Frame): Frame for displaying application info
            self.label_username_show (Label): Label for displaying username.
            self.frame_application_info_two (Frame): Frame for displaying application info
            self.label_balance_show (Label): Label for displaying balance.
            self.frame_deposit_info_one (Frame): Frame for displaying application info
            self.label_deposit (Label): Label deposit.
            self.entry_deposit (Entry): Entry for deposit amount.
            self.frame_deposit_info_two (Frame): Frame for displaying application info
            self.button_deposit (Button): Button for depositing.
            self.frame_deposit_info_three (Frame): Frame for displaying application info
            self.label_output (Label): Label shows if deposit was successful or not.
            self.frame_withdraw_info_one (Frame): Frame for displaying application info
            self.label_withdraw (Label): Label withdraw.
            self.entry_withdraw (Entry): Entry for withdraw amount.
            self.frame_withdraw_info_two (Frame): Frame for displaying application info
            self.button_withdraw_confirm (Button): Button for withdrawing.
            self.frame_withdraw_info_three (Frame): Frame for displaying application info
            self.label_withdraw_sf (Label): Label shows if withdraw was successful or not.
        """
        self.window = window
        self.window.configure()  # Configure the main window
        self.login_attempt = 0  # Counter for login attempts
        self.temp_variable_1 = ''  # Temporary variable 1
        self.temp_variable_2 = ''  # Temporary variable 2
        self.account_type = 0

        # Frame for username entry
        self.frame_one_login = Frame(self.window)
        self.label_username = Label(self.frame_one_login, text='Username:', font=('Arial', 20, 'bold'))
        self.label_username.pack()
        self.entry_username = Entry(self.frame_one_login, font=('Arial', 24))
        self.entry_username.pack()
        self.frame_one_login.pack(pady=(100, 0))

        # Frame for password entry
        self.frame_two_login = Frame(self.window)
        self.label_password = Label(self.frame_two_login, text='Password', font=('Arial', 20, 'bold'))
        self.label_password.pack()
        self.entry_password = Entry(self.frame_two_login, font=('Arial', 24), show='*')
        self.entry_password.pack()
        self.frame_two_login.pack()

        # Frame for login button
        self.frame_three_login = Frame(self.window)
        self.button_login = Button(self.frame_three_login, text='LOGIN', font=('Arial', 20, 'bold'), command=lambda: self.login_pressed())
        self.button_login.pack()
        self.frame_three_login.pack(pady=(20, 0))

        # Frame for displaying messages
        self.frame_four_login = Frame(self.window)
        self.label_questions = Label(self.frame_four_login, text='', font=('Arial', 20))
        self.label_questions.pack()

        # Frame containing buttons for selecting account type
        self.frame_one_application = Frame(self.window)
        # Button for selecting checking account
        self.button_checking = Button(self.frame_one_application, text='Checking Account', font=('Arial', 15, 'bold'),
                                      command=lambda: self.appear_application('Checking', 1))
        self.button_checking.pack(side=LEFT, padx=5)
        # Button for selecting savings account
        self.button_savings = Button(self.frame_one_application, text='Savings Account', font=('Arial', 15, 'bold'),
                                     command=lambda: self.appear_application('Savings', 2))
        self.button_savings.pack(side=LEFT, padx=5)
        # Button for exiting the application
        self.button_exit = Button(self.frame_one_application, text='Exit', font=('Arial', 15, 'bold'),
                                  command=lambda: self.reset_application())
        self.button_exit.pack(anchor='e', padx=10)

        # Frame displaying selected account type
        self.frame_two_application = Frame(self.window)
        self.label_account_type = Label(self.frame_two_application, text='', font=('Arial', 15))
        self.label_account_type.pack()

        # Frame containing buttons for account actions
        self.frame_three_application = Frame(self.window)
        # Button for displaying account information
        self.button_account_info = Button(self.frame_three_application, text='Account Info', font=('Arial', 15, 'bold'),
                                          command=lambda: self.show_account_info())
        self.button_account_info.pack(side=LEFT, padx=5)
        # Button for withdrawing from the account
        self.button_account_withdraw = Button(self.frame_three_application, text='Withdraw', font=('Arial', 15, 'bold'),
                                              command=lambda: self.withdraw_screen())
        self.button_account_withdraw.pack(side=LEFT, padx=5)
        # Button for depositing into the account
        self.button_account_deposit = Button(self.frame_three_application, text='Deposit', font=('Arial', 15, 'bold'),
                                             command=lambda: self.deposit_screen())
        self.button_account_deposit.pack(side=LEFT, padx=5)

        # Frame displaying account username
        self.frame_application_info_one = Frame(self.window)
        self.label_username_show = Label(self.frame_application_info_one, text='', font=('Arial', 15, 'bold'))
        self.label_username_show.pack()

        # Frame displaying account balance
        self.frame_application_info_two = Frame(self.window)
        self.label_balance_show = Label(self.frame_application_info_two, text='', font=('Arial', 15, 'bold'))
        self.label_balance_show.pack()

        # Frame for deposit input
        self.frame_deposit_info_one = Frame(self.window)
        self.validate_input_cmd = (self.window.register(self.validate_input), '%P')
        self.label_deposit = Label(self.frame_deposit_info_one, text='Deposit Amount:', font=('Arial', 15, 'bold'))
        self.label_deposit.pack(side=LEFT)
        self.entry_deposit = Entry(self.frame_deposit_info_one, validate="key", validatecommand=self.validate_input_cmd,
                                   font=('Arial', 15, 'bold'))
        self.entry_deposit.pack(side=LEFT)

        # Frame for deposit button
        self.frame_deposit_info_two = Frame(self.window)
        self.button_deposit = Button(self.frame_deposit_info_two, text='Deposit', font=('Arial', 15, 'bold'),
                                     command=lambda: self.deposit_process())
        self.button_deposit.pack()

        # Frame for deposit output message
        self.frame_deposit_info_three = Frame(self.window)
        self.label_output = Label(self.frame_deposit_info_three, text='Deposit Successful', font=('Arial', 11, 'bold'))
        self.label_output.pack()

        # Frame for withdraw input
        self.frame_withdraw_info_one = Frame(self.window)
        self.label_withdraw = Label(self.frame_withdraw_info_one, text='Withdraw Amount:', font=('Arial', 15, 'bold'))
        self.label_withdraw.pack(side=LEFT)
        self.entry_withdraw = Entry(self.frame_withdraw_info_one, validate="key",
                                    validatecommand=self.validate_input_cmd,
                                    font=('Arial', 15, 'bold'))
        self.entry_withdraw.pack(side=LEFT)

        # Frame for withdraw button
        self.frame_withdraw_info_two = Frame(self.window)
        self.button_withdraw_confirm = Button(self.frame_withdraw_info_two, text='Deposit', font=('Arial', 15, 'bold'),
                                     command=lambda: self.withdraw_process())
        self.button_withdraw_confirm.pack()

        # Frame for withdraw output message
        self.frame_withdraw_info_three = Frame(self.window)
        self.label_withdraw_sf = Label(self.frame_withdraw_info_three, text='D', font=('Arial', 11, 'bold'))
        self.label_withdraw_sf.pack()



    def login_pressed(self):
        """
        Handle the login button press event.

        Checks the username and password entry fields and performs appropriate actions
        based on the input provided.

        """
        # If both username and password fields are empty
        if self.entry_username.get() == '' and self.entry_password.get() == '':
            self.label_questions.configure(text='Enter a username and password', font=('Arial', 20))
            self.frame_four_login.pack(pady=(20,0))
            self.reset_info()
        # If only the username field is empty
        elif self.entry_username.get() == '':
            self.label_questions.configure(text='Enter a username', font=('Arial', 20))
            self.frame_four_login.pack(pady=(20, 0))
            self.reset_info()
        # If only the password field is empty
        elif self.entry_password.get() == '':
            self.label_questions.configure(text='Enter a password', font=('Arial', 20))
            self.frame_four_login.pack(pady=(20, 0))
            self.reset_info()
        # If login attempt is the second one and matches the temporary variables
        elif self.entry_username.get() == self.temp_variable_1 and self.entry_password.get() == self.temp_variable_2 and self.login_attempt == 1:
            # Create a new account with the entered username and password
            account_creation(self.entry_username.get(), self.entry_password.get())
            self.hide_login_frame()
        # If the entered username and password do not match any existing account
        elif not account_look_up(self.entry_username.get(), self.entry_password.get()):
            self.label_questions.configure(text='To create a new account re-click login, else login info is incorrect', font=('Arial', 13))
            self.frame_four_login.pack(pady=(20, 0))
            self.login_attempt +=1
            self.temp_variable_1 = self.entry_username.get()
            self.temp_variable_2 = self.entry_password.get()
        # If the entered username and password match an existing account
        elif account_look_up(self.entry_username.get(), self.entry_password.get()):
            self.hide_login_frame()

    def reset_info(self):
        """
        Reset temporary variables and login attempt counter.
        """
        self.temp_variable_1 = ''
        self.temp_variable_1 = ''
        self.login_attempt = 0

    def hide_login_frame(self):
        """
        Hide the login frame and reset information.
        """
        self.frame_one_login.pack_forget()
        self.frame_two_login.pack_forget()
        self.frame_three_login.pack_forget()
        self.frame_four_login.pack_forget()
        self.reset_info()
        self.frame_one_application.pack(pady=(10, 0))

    def appear_application(self, account_type, account_type_num):
        """
        Display the application interface for the specified account type.

        Parameters:
            account_type (str): The type of account (e.g., "Checking", "Savings").
            account_type_num (int): The numeric identifier for the account type.

        """
        # Clear previous information and set the account type
        self.label_username_show.configure(text='')
        self.label_balance_show.configure(text='')
        self.forget_options()
        self.account_type = account_type_num

        # Set the account type label and display application frames
        self.label_account_type.configure(text=f'{account_type}')
        self.frame_two_application.pack(pady=(15, 0))
        self.frame_three_application.pack(pady=(15, 0))

    def reset_application(self):
        """
        Reset the application to its initial state.

        """
        # Clear user information and hide application frames
        self.reset_info()
        self.account_type = 0
        self.entry_username.delete(0, len(self.entry_username.get()))
        self.entry_password.delete(0, len(self.entry_password.get()))
        self.frame_one_application.pack_forget()
        self.frame_two_application.pack_forget()
        self.frame_three_application.pack_forget()
        self.forget_options()
        self.label_username_show.configure(text='')
        self.label_balance_show.configure(text='')
        # Display login frames
        self.frame_one_login.pack(pady=(100, 0))
        self.frame_two_login.pack()
        self.frame_three_login.pack(pady=(20, 0))

    def show_account_info(self):
        """
        Show account information based on the selected account type.

        """
        if self.account_type == 1:  # Checking Account
            # Hide other options and display checking account information
            self.forget_options()
            self.label_username_show.configure(text=f'{self.entry_username.get()}')
            self.label_balance_show.configure(text=f'${account_balance_checking(self.entry_username.get())}')
            self.frame_application_info_one.pack()
            self.frame_application_info_two.pack()
        elif self.account_type == 2:  # Savings Account
            # Hide other options and display savings account information
            self.forget_options()
            self.label_username_show.configure(text=f'{self.entry_username.get()}')
            self.label_balance_show.configure(text=f'${account_balance_savings(self.entry_username.get())}')
            self.frame_application_info_one.pack()
            self.frame_application_info_two.pack()

    def deposit_screen(self):
        """
        Switch to the deposit screen based on the selected account type.

        """
        if self.account_type == 1:  # Checking Account
            # Hide other options and display checking account balance
            self.forget_options()
            self.label_balance_show.configure(text=f'${account_balance_checking(self.entry_username.get())}')
            self.frame_application_info_two.pack(pady=(10, 0))
            self.frame_deposit_info_one.pack(pady=(10, 0))
            self.frame_deposit_info_two.pack(pady=(10, 0))
        elif self.account_type == 2:  # Savings Account
            # Hide other options and display savings account balance
            self.forget_options()
            self.label_balance_show.configure(text=f'${account_balance_savings(self.entry_username.get())}')
            self.frame_application_info_two.pack(pady=(10, 0))
            self.frame_deposit_info_one.pack(pady=(10, 0))
            self.frame_deposit_info_two.pack(pady=(10, 0))

    def withdraw_screen(self):
        """
        Switch to the withdrawal screen based on the selected account type.

        """
        if self.account_type == 1:  # Checking Account
            # Hide other options and display checking account balance
            self.forget_options()
            self.label_balance_show.configure(text=f'${account_balance_checking(self.entry_username.get())}')
            self.frame_application_info_two.pack(pady=(10, 0))
            self.frame_withdraw_info_one.pack(pady=(10, 0))
            self.frame_withdraw_info_two.pack(pady=(10, 0))
        elif self.account_type == 2:  # Savings Account
            # Hide other options and display savings account balance
            self.forget_options()
            self.label_balance_show.configure(text=f'${account_balance_savings(self.entry_username.get())}')
            self.frame_application_info_two.pack(pady=(10, 0))
            self.frame_withdraw_info_one.pack(pady=(10, 0))
            self.frame_withdraw_info_two.pack(pady=(10, 0))

    def deposit_process(self):
        """
        Process a deposit transaction based on the selected account type.

        """
        if self.account_type == 1:  # Checking Account
            if self.entry_deposit.get() == '':
                self.label_output.configure(text='Deposit Can Not Be Blank')
                self.frame_deposit_info_three.pack()
            else:
                # Calculate new balance and update checking account balance
                new_balance = int(account_balance_checking(self.entry_username.get())) + int(self.entry_deposit.get())
                update_balance_checking(self.entry_username.get(), str(new_balance))
                self.label_output.configure(text='Deposit Successful')
                self.frame_deposit_info_three.pack()
        elif self.account_type == 2:  # Savings Account
            if self.entry_deposit.get() == '':
                self.label_output.configure(text='Deposit Can Not Be Blank')
                self.frame_deposit_info_three.pack()
            else:
                # Calculate new balance and update savings account balance
                new_balance = int(account_balance_savings(self.entry_username.get())) + int(self.entry_deposit.get())
                update_balance_savings(self.entry_username.get(), str(new_balance))
                self.label_output.configure(text='Deposit Successful')
                self.frame_deposit_info_three.pack()

    def withdraw_process(self):
        """
        Process a withdrawal transaction based on the selected account type.

        """
        if self.account_type == 1:  # Checking Account
            if self.entry_withdraw.get() == '':
                self.label_withdraw_sf.configure(text='Withdraw Can Not Be Blank')
                self.frame_withdraw_info_three.pack()
            elif int(account_balance_checking(self.entry_username.get())) - int(self.entry_withdraw.get()) < 0:
                self.label_withdraw_sf.configure(text='Withdraw Can Not Bring Your Account To Negative')
                self.frame_withdraw_info_three.pack()
            else:
                # Calculate new balance and update checking account balance
                new_balance = int(account_balance_checking(self.entry_username.get())) - int(self.entry_withdraw.get())
                update_balance_checking(self.entry_username.get(), str(new_balance))
                self.label_withdraw_sf.configure(text='Withdraw Successful')
                self.frame_withdraw_info_three.pack()
        elif self.account_type == 2:  # Savings Account
            if self.entry_withdraw.get() == '':
                self.label_withdraw_sf.configure(text='Withdraw Can Not Be Blank')
                self.frame_withdraw_info_three.pack()
            elif (int(account_balance_savings(self.entry_username.get())) - int(
                    self.entry_withdraw.get()) < 100) or self.entry_withdraw == '':
                self.label_withdraw_sf.configure(text='Withdraw Can Not Bring Your Account Below $100')
                self.frame_withdraw_info_three.pack()
            else:
                # Calculate new balance and update savings account balance
                new_balance = int(account_balance_savings(self.entry_username.get())) - int(self.entry_withdraw.get())
                update_balance_savings(self.entry_username.get(), str(new_balance))
                self.label_withdraw_sf.configure(text='Withdraw Successful')
                self.frame_withdraw_info_three.pack()


    def validate_input(self, new_text):
        """
        Validate the input for Entry widgets to allow only digits or a single decimal point.

        Parameters:
            new_text (str): The new text to be validated.

        Returns:
            bool: True if the new text is valid (contains only digits or a single decimal point),
                False otherwise.
        """
        # Check if the new text contains only digits or a single decimal point
        if new_text == "" or new_text.isdigit() or (new_text.count('.') == 1 and new_text.replace('.', '').isdigit()):
            return True
        else:
            return False


    def forget_options(self):
        """
        Clear the input fields and hide the application frames.
        """
        # Clear the input fields
        self.entry_deposit.delete(0, len(self.entry_deposit.get()))
        self.entry_withdraw.delete(0, len(self.entry_withdraw.get()))

        # Hide the application frames
        self.frame_application_info_one.pack_forget()
        self.frame_application_info_two.pack_forget()
        self.frame_deposit_info_one.pack_forget()
        self.frame_deposit_info_two.pack_forget()
        self.frame_deposit_info_three.pack_forget()
        self.frame_withdraw_info_one.pack_forget()
        self.frame_withdraw_info_two.pack_forget()
        self.frame_withdraw_info_three.pack_forget()