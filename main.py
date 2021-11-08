import csv
from pprint import pprint
from progress.bar import Bar

DATASET_FILE = "dataset"
TILE_SIZE = 0.01


class Person:
    def __init__(self, id):
        self.id = id
        self.interestPoint = {}
        self.rawData = []

    def addRawData(self, rawData):
        # self.rawData.append(rawData)
        tile = int(rawData["longitude"] / TILE_SIZE), int(rawData["latitude"] / TILE_SIZE)
        if tile not in self.interestPoint:
            self.interestPoint[tile] = 1
        else:
            self.interestPoint[tile] += 1

    # def moves(self):
    #     for data in self.rawData:
    #         tileX = int(data["longitude"] / TILE_SIZE)
    #         tileY = int(data["latitude"] / TILE_SIZE)
    #         if (tileX, tileY) not in self.interestPoint:
    #             self.interestPoint[(tileX, tileY)] = [data]
    #         else:
    #             self.interestPoint[(tileX, tileY)].append(data)
    #
    #     print(self.interestPoint)

    def __str__(self):
        return f"user {self.id}"


Users = []


def isNewUser(id, users):
    for user in users:
        if user.id == id:
            return False
    return True


with open(DATASET_FILE, 'r', newline="") as file:
    reader = csv.reader(file, delimiter="	")
    bar = Bar('Loading', fill='=', suffix='%(percent).1f%% - %(eta)s s', max=34_551_849)
    for row in reader:
        # is new User
        id = int(row[0])
        if isNewUser(id, Users, ):
            mUser = Person(id)
            Users.append(mUser)
        else:
            mUser = [user for user in Users if user.id == id][0]
        mUser.addRawData({
            "timestamp": int(row[1]),
            "longitude": float(row[2]),
            "latitude": float(row[3]),
        })
        bar.next()
    bar.finish()

pprint(Users[0].interestPoint)
