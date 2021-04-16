from url import Url
from spider import Spider
from data import Data

def spiderCommitM(mySpider, myData):
    mySpider.spiderCommitList()
    #commitList = myData.readCommit()
    #mySpider.spiderCommit(commitList)


if __name__ == '__main__':
    respose = {}
    respose['apollo'] = "ctripcorp"
    respose['tidb'] = 'pingcap'
    site = 'tidb'
    myUrl = Url(respose[site], site)
    mySpider = Spider(myUrl)
    myData = Data(myUrl)
    spiderCommitM(mySpider, myData)