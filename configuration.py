import csv


class Configuration(object):
    def __init__(self):
        self.categoryByRFC = {}

    def readFrom(self, filename):
        file = open(filename)

        reader = csv.DictReader(file)
        for row in reader:
            self.categoryByRFC[row['rfc']] = row['category']

        file.close()
