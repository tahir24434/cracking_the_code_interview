class tmpr_tracker(object):
    """A class that makes various tasty fruits."""
    def __init__(self):
        self.min = None
        self.max = None

        # Mean data
        self.mean = None
        self.total_numbers = 0
        self.total_sum = 0.0

        # Mode data
        self.occurrences = [0] * (111)
        self.max_occurrences = 0
        self.mode = None

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_mean(self):
        print "Get Mean"

    def get_mode(self):
        print "Mode"

    def insert(self, new_temp):
        # For Min
        if (self.min is None) or (new_temp < self.get_min()):
            self.min = new_temp

        # For Max
        if (self.min is None) or (new_temp > self.get_max()):
            self.max = new_temp

        # For mean
        self.total_numbers += 1
        self.total_sum += new_temp
        self.mean = self.total_sum/self.total_numbers

        # For Mode
        self.occurrences[new_temp] += 1
        if (self.occurrences[new_temp] > self.max_occurrences):
            self.max_occurrences = self.occurrences[new_temp]
            self.mode = new_temp

        print "min=%d max=%d mean=%f mode=%f" %(self.min, self.max, self.mean, self.mode)

my_temperature_tracker = tmpr_tracker()
while (1):
    response = input("Please enter temperature: ")
    my_temperature_tracker.insert(response)
