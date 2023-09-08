# Reminder Application

# User authentication
users = {'user1': 'password1', 'user2': 'password2'}
logged_in_user = None

def login(username, password):
    global logged_in_user
    if username in users and users[username] == password:
        logged_in_user = username
        return True
    else:
        return False

def logout():
    global logged_in_user
    logged_in_user = None

# Reminder management
reminders = []

def add_reminder(title, date):
    reminders.append({'title': title, 'date': date, 'enabled': True})

def delete_reminder(title):
    for reminder in reminders:
        if reminder['title'] == title:
            reminders.remove(reminder)

def View_reminder(title):
    for reminder in reminders:
        if reminder['title'] == title:
            reminders.show(reminder)

def enable_reminder(title):
    for reminder in reminders:
        if reminder['title'] == title:
            reminder['enabled'] = True

def disable_reminder(title):
    for reminder in reminders:
        if reminder['title'] == title:
            reminder['enabled'] = False

# Main program loop
while True:
    print("\nReminder Application Menu:")
    print("1. Login")
    print("2. Add Reminder")
    print("3. View Reminder")
    print("4. Delete Reminder")
    print("5. Enable Reminder")
    print("6. Disable Reminder")
    print("7. Logout")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if logged_in_user:
            print(f'Already logged in as {logged_in_user}.')
        else:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print(f'Logged in as {username}.')
            else:
                print("Login failed.")

    elif choice == '2':
        if not logged_in_user:
            print("Please login first.")
        else:
            title = input("Enter reminder title: ")
            date = input("Enter reminder date: ")
            add_reminder(title, date)
            print("Reminder added.")

    elif choice == '3':
        if not logged_in_user:
            print("Please login first.")
        else:
            title = input("Enter reminder title to View: ")
            View_reminder(title)
            print("Reminder View.")

    elif choice == '4':
        if not logged_in_user:
            print("Please login first.")
        else:
            title = input("Enter reminder title to delete: ")
            delete_reminder(title)
            print("Reminder deleted.")

    elif choice == '5':
        if not logged_in_user:
            print("Please login first.")
        else:
            title = input("Enter reminder title to enable: ")
            enable_reminder(title)
            print("Reminder enabled.")

    elif choice == '6':
        if not logged_in_user:
            print("Please login first.")
        else:
            title = input("Enter reminder title to disable: ")
            disable_reminder(title)
            print("Reminder disabled.")

    elif choice == '7':
        logout()
        print("Logged out.")

    elif choice == '8':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
