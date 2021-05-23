class Distance:
    def __init__(self, location, paths, size):
        self.location = location
        self.paths = paths
        self.size = size

    def __repr__(self):
        return f"Location: {self.location}   Paths: {self.paths}\n"

