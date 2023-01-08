import datetime
import base64
import os
from pathlib import Path


class Employee:
    """
    Parent class for Volunteer class, requires some default arguments.
    """

    collected_waste_overview = []
    image_64_encode = ''

    def __init__(self, last_name, name, year_of_birth, e_mail, phone, address, isAdministrator):
        self.last_name = last_name
        self.name = name
        self.year_of_birth = year_of_birth
        self.e_mail = e_mail
        self.phone = phone
        self.created = datetime.datetime.now()
        self.address = address
        self.isAdministrator = isAdministrator
        self.image = 'ess.jpg'

    def full_name_with_male(self):
        """
        From user info create combinated string
        :return: string value like this: : <James Bond>agent@gmail.com
        """
        full_name = f"<{self.name} {self.last_name}>{self.e_mail}"
        return str(full_name)

    def create_image_string(self, image_name):
        """
        Create string value from picture.
        :param image_name: string as full image name
        :return: Return encoded picture to string
        """
        get_suffix = Path(os.getcwd(), image_name).suffix
        if get_suffix != '.jpg':
            print("Unsupported file format!")
        else:
            image = open(image_name, 'rb')
            image_read = image.read()
            self.image_64_encode = base64.b64encode(image_read)
            image.close()
            print(self.image_64_encode)
            return self.image_64_encode

    def create_image_from_string(self):
        """
        Create an image from base64 encoded file
        :return: Nothing
        """
        if len(self.image_64_encode) > 0:
            image_64_decode = base64.b64decode(self.image_64_encode)
            image_result = open('foto.jpg', 'wb')
            image_result.write(image_64_decode)
            image_result.close()
            print("Image created!")
        else:
            print("Sorry, first you need to encode image by using 6 option in menu!")



    def admin_add_daly_collected_waste(self):
        """
        With this function only Administrator can add multiple daly collection waste.
        :return: Print when information is successfully added, and append info to the daily_collected_waste_info list.
        """
        if self.isAdministrator:
            print("Add collected trash: ")
            while True:
                waste_type = Volunteer.chose_waste_type()

                volume = round(Volunteer.enter_volume(), 2)
                weight = Volunteer.enter_weight()
                density = Volunteer.calculate_density(weight, volume)
                year = InputValuesWithValidators.validate_year_month_date("Enter year ")
                month = InputValuesWithValidators.validate_year_month_date("Enter month ")
                day = InputValuesWithValidators.validate_year_month_date("Enter day ")

                try:
                    date = datetime.date(year, month, day)
                except:
                    date = datetime.datetime.now().date()

                self.daily_collected_waste_info = {'date': date, 'type': waste_type, 'weight': weight, 'volume': volume, 'density': density}
                self.collected_waste_overview.append(self.daily_collected_waste_info)
                print("Info added!")
                want_to_continue = input("To exit enter e value or enter to continue: ")
                if want_to_continue == 'e':
                    break
        else:
            print("Sorry, you are not an administrator!")


class InputValuesWithValidators:

    """
        Class contains methods to allow input data and validate the inputted value.
    """

    @staticmethod
    def enter_last_name():
        """
        After user input value function check if the value length is bigger than 0.
        :return: Validated input of the last_name value as string.
        """
        while True:
            last_name = input("Enter last name or to quit enter exit: ")
            if len(last_name) == 0:
                print("Last name field is required!")
            elif last_name.lower() == "exit":
                print("Thank you for visiting us!")
                exit()
            else:
                return last_name

    @staticmethod
    def enter_name():
        """
        After user input value function check if the value contains only english alphabetic characters .
        :return: Validated input of the name value as string.
        """
        allowed_symbols = list('qwertyuiopasdfghjklzxcvbnm')
        while True:
            name = input("Enter name or to quit enter exit: ")
            check = all(item in allowed_symbols for item in list(name.lower()))
            if check and name.lower() != "exit":
                break
            elif name.lower() == "exit":
                print("Thank you for visiting us!")
                exit()
            else:
                print("Please use only allowed chars!")
        return name

    @staticmethod
    def enter_year_of_birth():
        """
        After user input value function check if the value is int and bigger or equals than 0 .
        :return: Validated input of the year value as int.
        """
        while True:
            try:
                enter_year = int(input("Enter year of birth or to quit enter -1: "))
                if enter_year >= 0:
                    return enter_year
                elif enter_year == -1:
                    print("Thank you for visiting us!")
                    exit()
                else:
                    return 2000
            except ValueError:
                print("Please enter valid integer: ")

    @staticmethod
    def enter_e_mail():
        """
        After user input value function check if the value is valid email .
        :return: Validated input of the email value as string.
        """
        while True:
            x = '@'
            enter_mail = input("Enter email or to quit enter exit: ")
            if enter_mail == 'exit':
                print("Thank you for visiting us!")
                exit()
            elif any(char in list(enter_mail) for char in x):
                return enter_mail
            elif any(char not in list(enter_mail) for char in x):
                return enter_mail + '@gmail.com'
            else:
                print("Please enter valid email address: ")

    @staticmethod
    def enter_mobile_number():
        """
        After user input value function check if the value is valid phone.
        :return: Validated input of the mobile phone value as string. Remove every character which is not in the +1234567890.
        """
        allowed_characters = list("+1234567890")
        valid_number = []
        keep_open = True
        while keep_open:
            enter_phone = input("Enter mobile number or to quit enter exit: ")
            if len(enter_phone) > 5:
                for v in list(enter_phone):
                    if v in allowed_characters:
                        valid_number.append(v)
                    else:
                        pass
                number = ''
                return number.join(valid_number)
            elif enter_phone == "exit":
                print("Thank you for visiting us!")
                exit()
            else:
                print("Please enter valid mobile number!")

    @staticmethod
    def enter_address():
        """
        After user input value function check if the value length is bigger than 0.
        :return: Validated input of the address value as string.
        """
        while True:
            address = input("Enter address or to quit enter exit: ")
            if len(address) == 0:
                print("Address field is required!")
            elif address.lower() == "exit":
                print("Thank you for visiting us!")
                exit()
            else:
                return address

    @staticmethod
    def enter_is_administrator():
        while True:
            address = input("Enter y is administrator or n if not, to quit enter exit: ")
            if address == 'y':
                return True
            elif address == 'n':
                return False
            elif address == "exit":
                print("Thank you for visiting us!")
                exit()
            else:
                print("Please enter y is administrator or n if not, to quit enter exit.")

    @staticmethod
    def validate_year_month_date(val_name):
        """
        Function validates user input. input must be int and bigger than 0
        :return: return int
        """
        while True:
            try:
                val = int(input(f"Enter {val_name} as number: "))
                if val < 0:
                    print("Value can not be 0 or negative")
                else:
                    return val
            except ValueError:
                print("Please enter valid number.")

    @staticmethod
    def validate_entered_multiple_strings(*args):
        """
        Enter multiple string values between user will enter his choice
        :param args: multiple string values
        :return: user chosen string value
        """

        while True:
            val = input(f"Please enter value from {args} ")
            if val in args:
                return val
            else:
                print("Invalid choice")


class Volunteer(Employee):
    """
    This class inherits from Employee class.
    """

    def __init__(self, last_name, name, year_of_birth, e_mail, phone, address, isAdministrator):
        super().__init__(last_name, name, year_of_birth, e_mail, phone, address, isAdministrator)

    def add_daly_collected_waste(self):
        """
        With this function user can add daly collection waste.
        :return: Print when information is successfully added, and append info to the daily_collected_waste_info list.
        """
        while True:
            waste_type = self.chose_waste_type()

            volume = round(self.enter_volume(), 2)
            date = datetime.datetime.now()
            weight = self.enter_weight()
            density = self.calculate_density(weight, volume)

            self.daily_collected_waste_info = {'date': date.date(), 'type': waste_type, 'weight': weight, 'volume': volume, 'density': density}
            self.collected_waste_overview.append(self.daily_collected_waste_info)
            print("Info added!")
            break

    def display_collected_waste(self):
        """
        Display on the screen by single item collected waste.
        :return: Nothing
        """
        if len(self.collected_waste_overview) > 0:
            print("*" * 20)
            for trash in self.collected_waste_overview:
                print(f"Date collected {trash['date']}")
                print(f"Type {trash['type']}")
                print(f"Weight {trash['weight']}")
                print(f"Volume {trash['volume']}")
                print(f"Density {trash['density']}")

        else:
            print("Sorry, no trash collected!")

    def calculate_sum_of_trash(self, weight, trash_type, start_day, last_day):
        """
        This is helper function to calculate weight or volume by dates.
        :param weight: string value weight or volume
        :param trash_type: string 'glass', 'paper', 'plastic'
        :param start_day: Date field
        :param last_day: Date field
        :return: Nothing, Print on the screen total value
        """
        total = 0
        delta = datetime.timedelta(days=1)

        while start_day <= last_day:
            for i, dat in enumerate(self.collected_waste_overview):
                if dat['date'] == start_day and dat['type'] == trash_type:
                    total += dat[weight]
            start_day += delta

        print(f"Trash type {trash_type} total of {weight} in period {start_day} till {last_day} is {total}")

    def calculate_sum_of_trash_total(self):
        """
        Print on the screen total by elements glass, paper, plastic and totals by type
        :return: Nothing
        """
        waste_type = ['glass', 'paper', 'plastic']
        total_glass_weight = 0
        total_glass_volume = 0
        total_glass_density = 0

        total_paper_weight = 0
        total_paper_volume = 0
        total_paper_density = 0

        total_plastic_weight = 0
        total_plastic_volume = 0
        total_plastic_density = 0

        for data in self.collected_waste_overview:
            if data['type'] == waste_type[0]:
                total_glass_weight += data['weight']
                total_glass_volume += data['volume']
                total_glass_density += data['density']

            elif data['type'] == waste_type[1]:
                total_paper_weight += data['weight']
                total_paper_volume += data['volume']
                total_paper_density += data['density']

            elif data['type'] == waste_type[2]:
                total_plastic_weight += data['weight']
                total_plastic_volume += data['volume']
                total_plastic_density += data['density']

        print(f"Total glass weight {total_glass_weight}")
        print(f"Total glass volume {total_glass_volume}")
        print(f"Total glass density {total_glass_density}")
        print("*" * 20)
        print(f"Total paper weight {total_paper_weight}")
        print(f"Total paper volume {total_paper_volume}")
        print(f"Total paper density {total_paper_density}")
        print("*" * 20)
        print(f"Total plastic weight {total_plastic_weight}")
        print(f"Total plastic volume {total_plastic_volume}")
        print(f"Total plastic density {total_plastic_density}")
        print("*" * 20)
        print("Total")
        print(f"weight = {total_glass_weight + total_paper_weight + total_plastic_weight }")
        print(f"volume = {total_glass_volume + total_paper_volume + total_plastic_volume}")
        print(f"density = {total_glass_density + total_paper_density + total_plastic_density }")

    @staticmethod
    def chose_waste_type():
        """
        Helper function to validate user input
        :return: Nothing
        """
        waste_type = ['glass', 'paper', 'plastic']
        while True:
            try:
                type_of_waste = int(input(f"Chose waste type [1]-{waste_type[0]}, [2]-{waste_type[1]}, [3]-{waste_type[2]}: "))
                if type_of_waste-1 == 0:
                    return waste_type[0]
                elif type_of_waste-1 == 1:
                    return waste_type[1]
                elif type_of_waste-1 == 2:
                    return waste_type[2]
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input you have to chose between 1, 2 or 3!")

    @staticmethod
    def enter_weight():
        """
        Helper function to validate user input
        :return: Nothing
        """
        while True:
            try:
                weight = float(input("Enter weight "))
                if weight >= 0:
                    return weight
                else:
                    print("Value should be positive value! ")
            except ValueError:
                print("Value should be positive number!")

    @staticmethod
    def enter_volume():
        """
        Helper function to validate user input
        :return: Nothing
        """
        while True:
            try:
                volume = float(input("Enter volume m3 "))
                if volume >= 0:
                    return volume
                else:
                    print("Value should be positive value!")
            except ValueError:
                print("Value should be positive number!")

    @staticmethod
    def calculate_density(weight, volume):
        """
        Helper function to calculate density
        :return: int density value
        """
        try:
            return weight/volume
        except ZeroDivisionError:
            return 0

