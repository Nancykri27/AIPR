class sru_student:
    # Initialize a new student object with given attributes
    def __init__(self, name, roll_no, hostel_status):
        self.name = name                # Assign the name parameter to the name attribute
        self.roll_no = roll_no          # Assign the roll number to the roll_no attribute
        self.hostel_status = hostel_status  # Set hostel status for the student
        self.fee = 0                    # Initialize fee to zero by default

    # Update the student's fee with the provided amount
    def fee_update(self, amount):
        self.fee = amount               # Store the new fee amount

    # Print all details of the student
    def display_details(self):
        print("Name:", self.name)              # Output the student's name
        print("Roll No:", self.roll_no)        # Output the student's roll number
        print("Hostel Status:", self.hostel_status)  # Output hostel status
        print("Fee:", self.fee)                # Output the student's fee


# Create an instance of the sru_student class
student1 = sru_student("Nancy", 101, True)   # Instantiate student with name, roll, hostel
student1.fee_update(50000)                   # Update the student's fee
student1.display_details()                   # Call method to show all student info
