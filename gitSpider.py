from spider.url import Url
from spider.Spider import Spider
from spider.data import Data
from res.myRes import myRes


def spiderCommit(mySpider, myData):
    shaList = myData.readSha()
    mySpider.spiderCommit(shaList)


def spiderIssue(mySpider, myData):
    issueNumberList = myData.readIssueNumber()
    mySpider.spiderIssue(issueNumberList)


def spiderLists(mySpider):
    mySpider.spiderIssueList()
    mySpider.spiderCommitList()


def spiderTree(mySpider, myData):
    treeList = myData.readTree()
    mySpider.spiderTree(treeList)


def spiderDev(mySpider, myData):
    commitList = myData.readCommitList()
    developer = {}
    for key in commitList:
        if key['author'] != None:
            developer[key['author']['login']] = 1
    developers = []
    for key in developer:
        developers.append(key)
    mySpider.spiderDevl(developers)


if __name__ == '__main__':
    [resposeAut, resposeNam] = \
        myRes().getRespose('tidb')

    myUrl = Url(resposeAut, resposeNam)
    mySpider = Spider(myUrl)
    myData = Data(myUrl)
    #spiderLists(mySpider)
    #spiderCommit(mySpider, myData)
    #spiderIssue(mySpider, myData)
    spiderTree(mySpider, myData)
    #spiderDev(mySpider, myData)
