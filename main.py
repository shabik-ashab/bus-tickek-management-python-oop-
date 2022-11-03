

#bus ticket reservation system

from lib2to3.pgen2 import driver
from sys import flags
from unicodedata import name


def show_bus(bus):
    print('*'*50)
    print()
    print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
    print(f"Bus Number: {bus['coach']} \t\t Driver: {bus['driver']}")
    print(f"Arrival: {bus['arrival']} \t\t Derparture: {bus['departure']}")
    print(f"From: {bus['from_des']} \t\t To: {bus['to']}")
    print()
    a = 1
    # show the bus seat in a table
    # this table will have two colum and each column will have info 
    # about 2 seats
    for i in range(5):
        for j in range(2):
            print(f"{a}. {bus['seat'][a-1]}", end="\t")
            a+=1
        print("\t", end="")
        for j in range(2):
            print(f"{a}. {bus['seat'][a-1]}", end="\t")
            a+=1
        print()

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Bus:
    bus_seat = 20
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(self.bus_seat)]

class MyCompany: #bus install for admin
    total_bus = 5
    total_bus_lst = [] #dummy database
    
    def install(self):
        bus_no = int(input("Enter bus number: "))
        flag = 1
        for bus in self.total_bus_lst: #checking if the bus is already on the road
            if bus_no == bus['coach']:
                print("Bus already installed")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus driver name: ")
            bus_arrival = input("Enter Bus arrival time: ")
            bus_depurture = input("Enter Bus deperture time: ")
            bus_form = input("Enter Bus start from: ")
            bus_to = input("Enter Bus destination: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,bus_depurture,bus_form,bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus installed succesfully")


class BusCounter(MyCompany):
    user_lst = [] #user database
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter Bus Number: "))
        for bus in self.total_bus_lst:
            # print(bus['coach'])
            if bus_no == bus['coach']:
                passenger = input("Enter Your Name: ")
                seat_no = int(input("Enter Your Seat Number: "))
                if seat_no - 1 > self.bus_seat:
                    print(f"only {self.bus_seat} is avilable")
                elif bus['seat'][seat_no - 1] != 'Empty':
                    print("Seat already booked")
                else:
                    bus['seat'][seat_no - 1] = passenger
                    break
            else:
                print("No bus number avilable")
                break
    def showBusInfo(self):
        bus_no = int(input("Enter Bus Number: "))       
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
               show_bus(bus)

    def get_user(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your name: ")
        flag = 0
        for user in self.get_user():
            if user.username == name:
                print("username already exist")
                flag - 1
                break
        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name,password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully")

    def avilable_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No bus avilable")
        else:
            for bus in self.total_bus_lst:
                show_bus(bus)




while True:
    counter = BusCounter()
    print("1. Create an Account ")
    print("2. Login to your Account ")
    print("3. Exit")
    user_input = int(input("Enter your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    else:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False
        flag = 0
        if name == 'admin' and password == '123':
            isAdmin = True
        
        if isAdmin == False:
            for user in counter.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                    a = int(input("Enter Your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.avilable_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
            else:
                print("No username found")
        else:
            while True:
                print(f"\n {' '*10} HELLO ADMIN Welcome to BUS TICKET BOOKING SYSTEM\n")
                print(
                    "1. Install Bus\n2. Available Buses\n3. Show Bus Info\n4. EXIT")
                a = int(input("Enter Your Choice : "))
                if a == 4:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.avilable_buses()
                elif a == 3:
                    counter.showBusInfo()


# company = MyCompany()
# company.install()

# b = BusCounter()
# b.reservation()
# b.showBusInfo()
# b.create_account()
# b.install()
# b.install()
# b.avilable_buses()


