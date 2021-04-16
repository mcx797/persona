import os

class Path:
    pathUrl = ""

    def __init__(self, fileUrl):
        self.pathUrl = fileUrl

    def createPath(self):
        if os.path.exists(self.pathUrl):
            return True
        print(self.pathUrl)
        os.makedirs(self.pathUrl)
        return False

    def pathExs(self):
        return os.path.exists(self.pathUrl)