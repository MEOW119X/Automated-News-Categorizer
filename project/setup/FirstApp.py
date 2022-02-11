class MyFirstApp:

    def __init__(self, name, lastname, age, email):
        self.name = name
        self.lastname = lastname
        self.age = int(age)
        self.email = email + '@hotmail.com'

    def get_data(self):
        return f'''Name : {self.name} Lastname : {self.lastname} Age : {self.age} Email : {self.email}'''


MyApp = MyFirstApp('Marwan', 'Yeedeng', 22, 'Watchdog.av')


# TODO : Add more class
class TakeName(MyApp):

    def __init__(self):
        print(MyApp.name)


SecondApp = TakeName


def main():
    print(SecondApp)


if __name__ == '__main__':
    main()
