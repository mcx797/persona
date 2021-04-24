from res.myRes import myRes
from dbload.paths import Path
from dbload.loadData import loadData
from dbload.neodb import neoDB
from dbload.Base64decode import Decode64


def addCommitDB(myNeoDB, CommitList):
    myNeoDB.addCommitNodes(CommitList)
    myNeoDB.addCommitParents(CommitList)


def addCommitRoot(myNeoDB, commitList):
    for i in commitList:
        if i['parents'] == []:
            print(i['sha'])
            print('-----------')
            myNeoDB.addCommitRoot(i['sha'])
            break


def addTreeBlobDB(myNeoDB, commitList, myLoad):
    n = myLoad.readNow()
    print(n)
    print(n)
    listN = []
    for i in range(len(commitList)):
        if i <= n:
            continue
        listN.append(commitList[i])
    myNeoDB.addTree(listN)


if __name__ == "__main__":
    [ resposeAut, resposeNam] = \
        myRes().getRespose('tidb')
    myPath = Path(resposeAut, resposeNam)
    myLoad = loadData(myPath)
    commitList = myLoad.readCommitList()
    myNeoDB = neoDB(myLoad)
    #addCommitDB(myNeoDB, commitList)
    #addCommitRoot(myNeoDB, commitList)
    addTreeBlobDB(myNeoDB, commitList, myLoad)





