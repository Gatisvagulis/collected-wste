import datetime
from collected_waste import Volunteer, InputValuesWithValidators


def menu_options():

    """
    This function display user choices on console as menu
    :return: Nothing
    """

    print("Hello, please chose what you want to do!")
    print("(1) - Add info about collected trash.")
    print("(2) - Overview info about collected waste")
    print("(3) - Check volume or weight by period")
    print("(4) - Overview info about collected waste")
    print("(5) - Open full name with male")
    print("(6) - Open image as string")
    print("(7) - Create Image")


def enter_employee_data():
    """
    This function help create a new user
    :return: object user
    """
    print("Please enter user info: ")
    last_name = InputValuesWithValidators.enter_last_name()
    enter_name = InputValuesWithValidators.enter_name()
    year_of_birth = InputValuesWithValidators.enter_year_of_birth()
    e_mail = InputValuesWithValidators.enter_e_mail()
    mobile_number = InputValuesWithValidators.enter_mobile_number()
    address = InputValuesWithValidators.enter_address()
    admin = InputValuesWithValidators.enter_is_administrator()
    volunteer = Volunteer(last_name, enter_name, year_of_birth, e_mail, mobile_number, address, admin)
    return volunteer


def main():
    """
    This function executes collect waste program.
    :return:
    """
    print("Wellcome in collecting waste manager.")
    volunteer = enter_employee_data()
    # volunteer = Volunteer('last_name', 'name', 'year_of_birth', 'e_mail', 'phone', 'address', 'isAdministrator')
    while True:
        menu_options()
        select = input("Enter your choice: ")
        if select == '1':
            volunteer.add_daly_collected_waste()
        elif select == '2':
            volunteer.display_collected_waste()
        elif select == '3':
            # Here should be added validations for input fields
            print("Here you can calculate weight or volume in range of your selected days")
            weight_or_volume = input("Enter weight or volume: ")
            trash_type = input("Trash type 'glass', 'paper', 'plastic': ")
            start_year = int(input("Enter starting year: "))
            start_month = int(input("Enter starting month: "))
            start_day = int(input("Enter starting day: "))
            end_year = int(input("Enter end year: "))
            end_month = int(input("Enter starting month: "))
            end_day = int(input("Enter starting day: "))

            start = datetime.date(start_year, start_month, start_day)
            end = datetime.date(end_year, end_month, end_day)

            volunteer.calculate_sum_of_trash(weight_or_volume, trash_type, start, end)
        elif select == '4':
            volunteer.calculate_sum_of_trash_total()
        elif select == '5':
            print(volunteer.full_name_with_male())
        elif select == '6':
            volunteer.create_image_string(volunteer.image)
        elif select == '7':
            volunteer.create_image_from_string(volunteer.image)
            print("Image created!")


main()