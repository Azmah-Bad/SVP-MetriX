import csv

DATASET_FILE = "dataset"


class Person:
    def __init__(self, id):
        self.id = id
        self.interestPoint = []
        self.rawData = []

    def addRawData(self, rawData):
        self.rawData.append(rawData)

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
