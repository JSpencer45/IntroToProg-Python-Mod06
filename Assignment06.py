# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JSpencer,5/28/2025,Edited Script
# ------------------------------------------------------------------------------------------ #
import json
from idlelib.browser import file_open

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


#-- Processing --#
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What) 
    JSpencer, 5/28/2025, Created Class
    """


    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads json file in dict rows and checks for errors
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function

        :return: None
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function opens the json file in write mode and checks for errors
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
    
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        print("-" * 50)
        print("The following data has been saved: ")
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
        print("-" * 50)
        return student_data


#-- Presentation (Input/Output) --#
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    JSpencer, 5/28/2025, Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function outputs error messages
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
        
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """
        This function outputs menu choice
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
         
        :return: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """
        This function captures user menu choice and displays it back
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
        
        :return: string with the user's choice
        """
        choice = "0"
        try:
            choice = input("Enter your choice: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Menu choice must be 1, 2, 3, or 4!")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function outputs student course registration
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
    
        :return: None
        """

        print()
        print("-" * 50)
        for student in students:
            print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
        print("-" * 50)
        print()



    @staticmethod
    def input_student_data(student_data: list):
        """
        This function inputs the student's first name, last name and registered class
        ChangeLog: (Who, When, What)
        JSpencer, 5/28/2025, Created Function
        
        
        :return: show's the user's entry back to them
        """
        try:
            student_first_name = input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student first name should not contain numbers!")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student last name should not contain numbers!")
            course_name = input("Enter student's course name: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print("-" * 50)
            print("The following data has been entered: ")
            for student in students:
                print(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
            print("-" * 50)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# End of function definitions #


# Beginning of the main body of the script

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# repeat the follow tasks
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
        print("Program Ended")
    else:
        print("Please only choose options 1, 2, 3 or 4!")