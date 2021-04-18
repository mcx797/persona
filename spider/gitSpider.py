from url import Url
from spider import Spider
from data import Data


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
    respose = {}
    respose['apollo'] = 'ctripcorp'
    respose['tidb'] = 'pingcap'
    site = 'tidb'
    
    myUrl = Url(respose[site], site)
    mySpider = Spider(myUrl)
    myData = Data(myUrl)
    spiderLists(mySpider)
    spiderCommit(mySpider, myData)
    spiderIssue(mySpider, myData)
    spiderTree(mySpider, myData)


