import shelve


class myRes:
    allRespose = {}

    def __init__(self):
        file = shelve.open('res/respose.dat')
        self.allRespose = file['allRespose']
        file.close()
        return

    def getRespose(self, res):
        return [self.allRespose[res], res]

    def addRespose(self, autName, resName):
        self.allRespose[resName] = autName
        self.loadRespose()
        return

    def loadRespose(self):
        file = shelve.open('res/respose.dat')
        file['allRespose'] = self.allRespose
        file.close()
        return

if __name__ == "__main__":
    res = myRes()
    autName = input("input authorName")
    resName = input("imput resName")
    res.addRespose(autName, resName)