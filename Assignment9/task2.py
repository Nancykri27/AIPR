class sru_student:
    # Constructor initializes student attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                 # Store student's name
        self.roll_no = roll_no           # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status: True/False
        self.fee = 0                     # Default fee value

    # Method to update fee amount
    def fee_update(self, amount):
        self.fee = amount                # Update the student's fee value

    # Method to print all student details
    def display_details(self):
        print("Name:", self.name)              # Print student name
        print("Roll No:", self.roll_no)        # Print student roll number
        print("Hostel Status:", self.hostel_status)  # Print hostel status
        print("Fee:", self.fee)                # Print fee amount


# ----------- Testing the class -----------
student1 = sru_student("Nancy", 101, True)  # Creating a student object
student1.fee_update(50000)                  # Updating fee
student1.display_details()                  # Displaying details
