import json
from dbload.paths import Path
import os

class loadData:
    myPath = Path("", "")

    def __init__(self, pathIn):
        self.myPath = pathIn

    def openLocalFile(self, fileUrl):
        f = open(fileUrl, 'r', encoding='utf-8')
        fileC = json.loads(f.read())
        f.close()
        return fileC

    def readCommitList(self):
        commitListPath = self.myPath.commitListPath()
        commitList = []
        for name in os.listdir(commitListPath):
            print(name)
            listC = self.openLocalFile(commitListPath + '/' + name)
            for i in listC:
                commitList.append(i)
        return commitList

    def readTreeF(self, sha):
        treePath = self.myPath.treePath(sha)
        listC = self.openLocalFile(treePath)
        return listC

    def readBlobF(self, sha):
        blobPath = self.myPath.blobPath(sha)
        listC = self.openLocalFile(blobPath)
        return listC

    def loadNow(self, n):
        nowPath = self.myPath.nowPath()
        f = open(nowPath, "w", encoding='utf-8')
        f.write(str(n))
        f.close()

    def readNow(self):
        nowPath = self.myPath.nowPath()
        ReC = self.openLocalFile(nowPath)
        print(ReC)
        return ReC

