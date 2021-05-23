import operator
import os
from datetime import datetime


class Menu:
    """
    CLI Menu for printing information about the packages, and trucks.
    """

    def __init__(self, truck_1, truck_2, packages_table, routes, package_list, full_route):
        self.truck_1 = truck_1
        self.truck_2 = truck_2
        self.package_list = package_list
        self.packages_table = packages_table
        self.routes = routes
        self.full_route = full_route

    # Main menu
    def main_menu(self):
        print("\n\n--------------------------------------------")
        print("Please choose the menu you want to start: ")
        print("1. View Summarize Report")
        print("2. View Delivery Report of Packages")
        print("3. View Routes Taken and mileage\n\tfrom one destination to another")
        print("\n0. Quit")
        choice = input(" >>  ")

        while choice != "0":
            print("------------------------------------------------\n")
            if choice == "1":
                self.summary()
            if choice == "2":
                self.report_packages()
            if choice == "3":
                self.print_route()
            x = input("\n\nPress Enter to continue... ")

            print("\n\n--------------------------------------------")
            print("1. View Summarize Report")
            print("2. View Delivery Report of Packages")
            print("3. View Routes Taken and mileage\n\tfrom one destination to another")
            print("\n0. Quit")
            choice = input(" >>  ")

    def summary(self):
        total_distance = self.truck_1.get_total_distance() + self.truck_2.get_total_distance()
        total_time_elapse = (self.truck_1.get_total_time() / 60) + (self.truck_2.get_total_time() / 60)

        print("\nTruck 1 and 2")
        print(f"\t   Total Distance:          {round(total_distance, 2)} miles")
        print(f"\t   Total Time Elapse:       {int(total_time_elapse)} minutes")
        print(f"\t   Total Package Delivered: "
              f"{len(self.routes[0]) + len(self.routes[1]) + len(self.routes[2]) + len(self.routes[3])}")
        print(f"\t   Truck 1 time:            {self.truck_1.dt.strftime('%r')}")
        print(f"\t   Truck 2 time:            {self.truck_2.dt.strftime('%r')}")

    def report_packages(self):
        sorted_pkg = self.package_list[:]
        print("Sort Package By: ")
        print("1. ID")
        print("2. Delivered Time")
        print("3. Deadline\n")
        sort_by_id = input(" >>  ")

        if sort_by_id == "2":
            sorted_pkg = sorted(self.package_list, key=operator.attrgetter("delivered_time"))
        elif sort_by_id == "3":
            sorted_pkg = sorted(self.package_list, key=operator.attrgetter("deadline"), reverse=True)
        elif sort_by_id == "4":
            sorted_pkg = sorted(self.package_list, key=operator.attrgetter("left_hub_time"))

        print("Enter STARTING time (11:00 am): ")
        s = input(" >>  ")
        print("Enter ENDING time (11:00 am): ")
        e = input(" >>  ")

        time_start = datetime.strptime(s, "%I:%M %p")
        time_end = datetime.strptime(e, "%I:%M %p")
        ids = []
        address = []
        deadline = []
        city = []
        zipcode = []
        weight = []
        status = []
        count_delivered = 0
        count_hub = 0
        count_en_route = 0
        distance = 0

        for package in sorted_pkg:
            c_status = ""
            time_package_end = datetime.strptime(package.delivered_time, "%I:%M %p")
            time_package_start = datetime.strptime(package.left_hub_time, "%I:%M %p")
            if time_start < time_package_end < time_end or time_start >= time_package_end and time_start >= time_package_start:
                c_status = f"Delivered at {package.delivered_time} by Truck {package.truck}"
                count_delivered += 1
                distance = distance + package.distance
            elif time_start > time_package_start and time_end < time_package_end:
                c_status = f"En Route, left HUB at {package.left_hub_time}"
                count_en_route += 1
            else:
                c_status = f"At Hub"
                count_hub += 1

            ids.append(package.id)
            address.append(package.address)
            deadline.append(package.deadline)
            city.append(package.city)
            zipcode.append(package.zip_code)
            weight.append(package.mass)
            status.append(c_status)

        titles = ['ID', 'Address', 'Deadline', 'City', "Zip Code", "Weight", "Status"]
        zipped = zip(ids, address, deadline, city, zipcode, weight, status)
        data = [titles] + list(zipped)
        for i, d in enumerate(data):
            line = ' | '.join(str(x).ljust(4) + ' | ' for x in d[0:1])
            line = line + ' | '.join(str(x).ljust(40) + ' | ' for x in d[1:2])
            line = line + ' | '.join(str(x).ljust(20) for x in d[2:])
            print(line)
            if i == 0:
                print('-' * len(line))

        print(
            f"\nTotal package delivered and mileage between {time_start.strftime('%r')} and {time_end.strftime('%r')}:"
            f"\n\t     At The Hub: {count_hub}" \
            f"\n\t       En Route: {count_en_route}" \
            f"\n\t      Delivered: {count_delivered}" \
            f"\n\t Total Mileage: {round(distance, 2)} miles")

    def print_route(self):
        print(self.full_route)

    def is_between(self, time, time_range):
        if time_range[1] < time_range[0]:
            return time >= time_range[0] or time <= time_range[1]
        return time_range[0] <= time <= time_range[1]
