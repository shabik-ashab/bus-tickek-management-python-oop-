

#bus ticket reservation system

class User:
    def __init__(self,username,password);
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]

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




