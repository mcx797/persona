from url import Url

if __name__ == '__main__':
    respose = {}
    respose['apollo'] = "ctripcorp"
    respose['tidb'] = 'pingcap'
    site = "apollo"
    myUrl = Url(respose[site], site)