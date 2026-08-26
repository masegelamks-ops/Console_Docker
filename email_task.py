"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
"""Starting with creating the class and initialising the constructor"""

class Email:

# Initialise the instance variables for each email.

    """ Initialise a new email instance"""
    def __init__(self, email_adress, Subject_line, email_content):

        """ Initialise the instance variable for each email"""
        self.email_adress = email_adress
        self.Subject_line = Subject_line
        self.email_content = email_content
        self.has_been_read = False
        

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    """changes the has_been_read from False to True"""

    def mark_as_read (self):
        self.has_been_read = True
    

    # Initialise an empty variable called inbox
inbox = []

# --- Functions --- #

def populate_inbox(email_1, email_2, email_3):
    # Create 3 sample emails and add them to the inbox list.
    """Three sample emails to be used in the inbox"""
    email_1 = Email("one@gmail.com", "Hello world","Welcome to the world of programming", mark_as_read = False)
    email_2 = Email("two@gmail.com", "How are you", "I heard you are not doing well", mark_as_read = False )
    email_3 = Email("three@gmail.com", "Well Done", "Great programming skills you have developed", mark_as_read = False)
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)
    
    
    
def list_emails(inbox):
    # Create a function that prints each email's subject line
    populate_inbox(inbox)
    for i,v in enumerate:
        print(i,v)
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    

def read_email(inbox):
    email_number = int(input("From the list of emails, which email (0 being the first) would you like to read?: "))
    message = inbox [email_number]
    mark_as_read = True
    print(read_email(inbox))

    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    


def view_unread_emails(inbox):
    if mark_as_read is False:
        unread_email = inbox [1] 
        print(f"The email at position {i} is {view_unread_emails}")
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        read_email(inbox)
        pass

    elif user_choice == 2:
        view_unread_emails(inbox)
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        break

    else:
        print("Oops - incorrect input.")
