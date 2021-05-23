from datetime import datetime, timedelta
from utils.Dijkstra import get_shortest_path


class Truck:
    start_address = "HUB"
    total_distance = 0.0
    total_time = 0
    op_load = []
    delivered_packages = []
    left_hub = datetime.strptime("07:59", "%H:%M")

    def __init__(self, truck_num, dt):
        """
        Initialize Truck

        :param truck_num: Integer
        :param dt: datetime
        """
        self.max_load = 16
        self.avg_speed = 18
        self.truck_num = truck_num
        self.loads = []
        self.dt = dt

    def get_total_distance(self):
        """
        return total distance truck traveled

        :return:
        """
        return self.total_distance

    def get_total_time(self):
        """
        return travel time

        :return: datetime
        """
        return self.total_time

    def need_special_adjustment(self, pkg, load):
        """
        Check if package has note and accommodate them

        :param pkg: Package
        :param load: Packages[]
        :return:
        """
        if "Must be delivered" in pkg.note:
            for pkg_id in pkg.note.replace(',', ' ').split():
                if pkg_id.isdigit():
                    if pkg_id not in load:
                        self.op_load.append(pkg_id)

        if "Can only be on truck" in pkg.note:
            for num in pkg.note.split():
                if num.isdigit():
                    if num == self.truck_num:
                        return False

    def chuck_and_sort_packages(self, graph, hash_package, load, order):
        """
        The chuck and sorted used dijkstra to find the shortest path and then
        get P amount of packages to load in the truck. For each package, it
        will use the dijkstra to find the shortest path and add them into
        a list to be delivered.

        Time Complexity: O(N^3 * Log N)

        Although re sorting is not
        needed, but I had to manually insert packages earlier due to deadline.

        :param graph: Graph
        :param hash_package: HashMap<Package>
        :param load: Packages[]
        :param order: Integer
        :return: Packages[]
        """
        self.op_load = []
        sorted_op_load = []
        cur = "HUB"
        end = ""
        min_distance = float("inf")
        stop = ""
        packages_in_truck = 0

        i = 0
        # O()
        while i < len(load) - 1:
            #
            for package_id in load:
                p = hash_package.get(package_id)
                datum = graph.Draw_Path(cur, p.address)
                if order == 1:
                    packages_in_truck = 15
                    if datum[1] < min_distance and package_id not in self.op_load \
                            and not "Delayed" in p.note \
                            and not "Wrong" in p.note:
                        if p.note:
                            self.need_special_adjustment(p, self.op_load)
                        min_distance = datum[1]
                        stop = package_id
                        end = p.address
                elif order == 2:
                    packages_in_truck = 16
                    if datum[1] < min_distance and package_id not in self.op_load \
                            and "Delayed" not in p.note \
                            and package_id != "30" \
                            and package_id != "9":
                        min_distance = datum[1]
                        stop = package_id
                        end = p.address
                elif order == 3:
                    packages_in_truck = 7
                    if datum[1] < min_distance and package_id not in self.op_load and package_id != "9":
                        min_distance = datum[1]
                        stop = package_id
                        end = p.address
                elif order == 4:
                    return load

            min_distance = float("inf")
            if len(self.op_load) == 16:
                break
            self.op_load.append(stop)
            cur = end
            i += 1

        cur = "HUB"
        end = ""
        stop = ""

        if order == 2:
            self.op_load.insert(10, '30')

        while len(self.op_load) != len(sorted_op_load):
            for package_id in self.op_load:
                p = hash_package.get(package_id)
                datum = graph.Draw_Path(cur, p.address)
                if datum[1] < min_distance and package_id not in sorted_op_load:
                    min_distance = datum[1]
                    stop = package_id
                    end = p.address

            min_distance = float("inf")
            sorted_op_load.append(stop)
            cur = end

        return sorted_op_load[:packages_in_truck]

    def start_delivery(self, graph, hash_package, sorted_load):
        """
        Get Report regarding the truck, the route taken, how long, mileage, and which packages was delivered

        :param graph: Graph
        :param hash_package: HashMap<Packages>
        :param sorted_load: Packages[]
        :return: String
        """

        trip = 0
        text = f"\n\nTruck {self.truck_num} heading out of HUB at {self.dt.strftime('%r')}"
        self.left_hub = self.dt.strftime('%I:%M %p')
        for idx, package_id in enumerate(sorted_load):
            package = hash_package.get(package_id)
            package.set_left_hub_time(self.left_hub)
            end_address = package.address
            trip += 1
            datum = graph.Draw_Path(self.start_address, end_address)
            self.total_distance += datum[1]
            self.total_time += round(datum[1] / 18 * 3600, 0)
            self.dt = self.dt + timedelta(0, seconds=round(datum[1] / 18 * 3600, 0))
            time_taken = datum[1] / 18 * 60
            package.set_delivered_time(self.dt.strftime('%I:%M %p'))
            package.set_status("delivered")
            package.set_truck(self.truck_num)
            package.set_distance(datum[1])
            text = text + f"\n-------------------\n\nPackage ID: {package_id} \n" \
                          f"\t{' --> '.join(datum[0])}\n\n" \
                          f"\t\t                  Trip:  {trip}\n" \
                          f"\t\t                 Truck:  {self.truck_num}\n" \
                          f"\t\t              Deadline:  {package.deadline}\n" \
                          f"\t\t     Distance Traveled:  {round(datum[1], 2)} miles\n" \
                          f"\t\t          Time Arrived:  {round(time_taken, 0)} minutes\n" \
                          f"\t\t           Time Elapse:  {self.dt.strftime('%I:%M %p')}\n" \
                          f"\t\tCurrent Total Distance:  {round(self.total_distance, 2)} miles"

            self.start_address = end_address

            if idx == len(sorted_load) - 1:
                datum = graph.Draw_Path(self.start_address, "HUB")
                self.total_distance += datum[1]
                self.total_time += round(datum[1] / 18 * 3600, 0)
                self.dt = self.dt + timedelta(0, seconds=round(datum[1] / 18 * 3600, 0))
                time_taken = datum[1] / 18 * 60

                text = text + f"\n-------------------\n\nBack To HUB \n" \
                              f"\t{' --> '.join(datum[0])}\n\n" \
                              f"\t\t     Distance Traveled:  {round(datum[1], 2)} miles\n" \
                              f"\t\tCurrent Total Distance:  {round(self.total_distance, 2)} miles\n" \
                              f"\t\t          Time Arrived:  {round(time_taken, 0)} minutes\n" \
                              f"\t\t           Time Elapse:  {self.dt.strftime('%r')}\n"

        return text
