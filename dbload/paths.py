import os


class Path:
    authorName = "pingcap"
    codeName = "tidb"
    resName = "pingcap/tidb/"

    def __init__(self, aut, name):
        self.authorName = aut
        self.codeName = name
        self.resName = '/' + self.authorName + '/' + self.codeName

    def rootData(self):
        return "data/"

    def commitListPath(self):
        return self.rootData() + self.codeName + "/commitList"

    def issueListPath(self):
        return self.rootData() + self.codeName + "/issueList"

    def comLstConPath(self, i):
        return self.commitListPath() + '/' + str(i) + '.json'

    def issueLstConPath(self, i):
        return self.issueListPath() + '/' + str(i) + '.json'

    def commitPath(self, sha):
        return self.rootData() + self.codeName + '/commit/' + sha + '.json'

    def issuePath(self, number):
        return self.rootData() + self.codeName + '/issue/' + str(number) + '.json'

    def treePath(self, sha):
        return self.rootData() + self.codeName + '/tree/' + str(sha) + '.json'

    def blobPath(self, sha):
        return self.rootData() + self.codeName + '/blob/' + str(sha) + '.json'

    def nowPath(self):
        return self.rootData() + "now.txt"