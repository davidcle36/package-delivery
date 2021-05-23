import csv

from model.Location import Distance
from model.Package import Package


def LoadPackageData(path):
    """
    From an packages cvs file, add row to list.

    :param path: String
    :return: Packages[]
    """
    data_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.append(Package(row[0], row[1], row[2], row[3], row[4],
                                     row[5], row[6], row[7]))

    return data_list


def LoadDistanceData(path):
    """
    From an distance cvs file, add row to list.

    :param path:
    :return: Location[]
    """
    data_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            location = row[0].lstrip().split("\n")
            for i in range(len(row) - 1):
                if row[i+1] == '':
                    del row[i+1:len(row)]
                    break
                else:
                    row[i+1] = float(row[i+1])
            data_list.append(Distance(location[0], row[1:], sum(not "".__eq__(x) for x in row) - 1))

    return data_list
