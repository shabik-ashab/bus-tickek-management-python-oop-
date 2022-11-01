

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