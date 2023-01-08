import datetime
from collected_waste import Volunteer, InputValuesWithValidators, Employee


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
    print("(8) - Administrator can add multiple collected waste days")


def enter_employee_data():
    """
    This function help create a new user
    :return: object user
    """
    print("Please enter volunteer info!")
    last_name = InputValuesWithValidators.enter_last_name()
    enter_name = InputValuesWithValidators.enter_name()
    year_of_birth = InputValuesWithValidators.enter_year_of_birth()
    e_mail = InputValuesWithValidators.enter_e_mail()
    mobile_number = InputValuesWithValidators.enter_mobile_number()
    address = InputValuesWithValidators.enter_address()
    admin = False
    volunteer = Volunteer(last_name, enter_name, year_of_birth, e_mail, mobile_number, address, admin)

    print("Volunteer created!")

    print("Please enter administrator info: ")
    admin_last_name = InputValuesWithValidators.enter_last_name()
    admin_enter_name = InputValuesWithValidators.enter_name()
    admin_year_of_birth = InputValuesWithValidators.enter_year_of_birth()
    admin_e_mail = InputValuesWithValidators.enter_e_mail()
    admin_mobile_number = InputValuesWithValidators.enter_mobile_number()
    admin_address = InputValuesWithValidators.enter_address()
    admin_admin = True
    administrator = Employee(admin_last_name, admin_enter_name, admin_year_of_birth, admin_e_mail, admin_mobile_number, admin_address, admin_admin)

    print("Administrator created!")

    return volunteer, administrator


def main():
    """
    This function executes collect waste program. If number is displayed please enter it to navigate. Else write the given word.
    :return:
    """
    print("Wellcome in collecting waste manager.")
    print("You are administrator now")
    volunteer, administrator = enter_employee_data()

    while True:
        menu_options()
        select = input("Enter your choice: ")
        if select == '1':
            volunteer.add_daly_collected_waste()
        elif select == '2':
            volunteer.display_collected_waste()
        elif select == '3':
            print("Here you can calculate weight or volume in range of your selected days")
            weight_or_volume = InputValuesWithValidators.validate_entered_multiple_strings('weight', 'volume')
            trash_type = InputValuesWithValidators.validate_entered_multiple_strings('glass', 'paper', 'plastic')
            start_year = InputValuesWithValidators.validate_year_month_date('start year')
            start_month = InputValuesWithValidators.validate_year_month_date('start month')
            start_day = InputValuesWithValidators.validate_year_month_date('start day')
            end_year = InputValuesWithValidators.validate_year_month_date('end year')
            end_month = InputValuesWithValidators.validate_year_month_date('end month')
            end_day = InputValuesWithValidators.validate_year_month_date('end day')

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
            volunteer.create_image_from_string()
        elif select == '8':
            administrator.admin_add_daly_collected_waste()


main()
