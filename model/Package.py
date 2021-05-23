class Package:
    truck = 0

    def __init__(self, id, address, city, state, zip_code, deadline, mass, note=""):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.note = note
        self.is_delivered = False
        self.delivered_time = "11:59 PM"
        self.left_hub_time = "7:59 AM"
        self.status = "at the hub"
        self.distance = 0

    def __repr__(self):
        return f"Package ID: {self.id}\n\taddress: {self.address} deadline: {self.deadline} mass: {self.mass}\n"

    def __iter__(self):
        return iter(self.id)

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def get_delivered_time(self):
        return self.delivered_time

    def set_delivered_time(self, value):
        self.delivered_time = value

    def get_left_hub_time(self):
        return self.left_hub_time

    def set_left_hub_time(self, value):
        self.left_hub_time = value

    def get_truck(self):
        return self.truck

    def set_truck(self, truck):
        self.truck = truck

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance
