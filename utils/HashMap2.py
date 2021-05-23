"""
E
    Develop a hash table, without using any additional libraries or classes, 
    that has an insertion function that takes the following components as input 
    and inserts the components into the hash table:

        •   package ID number
        •   delivery address
        •   delivery deadline
        •   delivery city
        •   delivery zip code
        •   package weight
        •   delivery status (e.g., delivered, en route)
"""


class HashMap:
    """
    The Fundamental of the storage is a list or array, and the program methods for building the
    Hash Table are creating buckets for each indices in the list. The buckets are
    needed for storing key and value pairs.

    Similar to list, they both can search specific elements. However, with list, one must
    know the exact index to get the value, which is impractical due to sorting and unknown
    index value without looping through it first. But with a hash table, if one knows the key,
    the value can be found no matter the position of the index. 
    
    Methods

        _get_hash(self, key):
            From a key, the method converts it into an index value for the
            list.
            Time Complexity is O(1)

        def insert(self, key, value):
            From a generated hash value from key, the method
            will find a bucket to insert the key - value pair
            Time Complexity is O(1)
            Space Complexity is O(N), where is is the number of buckets

        def get(self, key):
            Returns the value that match the key from the hash table
            Time Complexity is O(1)

        def delete(self, key):
            Remove the value that match the key from the hash table
            Time Complexity is O(1)

        def print(self):
            Print the key-value pair from the hash table
            Time Complexity is O(N)
    """

    def __init__(self, initial_capacity=10):
        """
            Initializes the Hash Table by the given size if one is present. If not,
        default to 10

        Time Complexity is O(N)

            Therefore, Time complexity is O(N)

        :param initial_capacity:
        """
        self.table = []

        for i in range(initial_capacity):
            self.table.append([])

    def __iter__(self):
        """
        When used in loops such as for loop, iterate through each item
        in map
        Time Complexity: O(N)

            Therefore, Time complexity is O(N)
        :return:
        """
        return iter(self.table)

    def _get_hash(self, key):
        """
        return the hash value based on the key and size of the hash table
        Time Complexity: O(1)

        :param key:
        :return:
        """
        bucket = hash(key) % len(self.table)
        return bucket

    def add(self, key, value):
        """
        If key found, Insert a key value pair into a bucket in the hash table when in
        empty bucket that is found.

        Time complexity is O(1)

            Else when collision occurs, append the key value into the bucket that already
        been preoccupied.

        Time complexity is O(N)

            Therefore, Time complexity is O(N)

        :param key:
        :param value:
        :return:
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def update(self, key, value):
        """
            Find the value that matched the key and update it.
        Return true is the value of key has been updated.

        Time Complexity is O(N)

            Therefore, Time complexity is O(N)

        :param key:
        :param value:
        :return:
        """
        key_hash = self._get_hash(key)

        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    def get(self, key):
        """
            Find the value that matched the key and get it.
        Return the value that been found.

        Time Complexity is O(N)

            Therefore, Time complexity is O(N)

        :param key:
        :return:
        """
        key_hash = self._get_hash(key)

        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
            Find the key and if not, return false.
        Time Complexity is O(1)

            Find the key and remove it from hash table.
        The for loop to check if collision has occurred.

            Time Complexity is O(1 + m), when m = numbers of collision in one specific bucket

        :param key:
        :return:
        """
        key_hash = self._get_hash(key)

        if self.table[key_hash] is None:
            return False

        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

    def print(self):
        """
            iterate through each item in the hash table
        and print the key-value

        Time Complexity is O(N)

        :return:
        """
        for item in self.table:
            if len(item) != 0:
                print(item)
