

class PeakFinder:

    def __init__(self):
        pass

    def find_peak(self, data):
        length = len(data)
        location = 0
        maximum = 0.0
        for i in range(length):
            if data[i] > maximum:
                location = i
                maximum = data[i]
        return location
