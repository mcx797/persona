from url import Url
from spider import Spider
from data import Data
from myRes import myRes


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


if __name__ == '__main__':
    [resposeAut, resposeNam] = \
        myRes().getRespose('tidb')

    myUrl = Url(resposeAut, resposeNam)
    mySpider = Spider(myUrl)
    myData = Data(myUrl)
    spiderLists(mySpider)
    spiderCommit(mySpider, myData)
    spiderIssue(mySpider, myData)
    spiderTree(mySpider, myData)


