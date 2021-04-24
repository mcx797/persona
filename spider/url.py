class Url:
    authorName = ""
    codeName = ""
    gitName = ""

    def __init__(self, name, code):
        self.authorName = name
        self.codeName = code
        self.gitName = name + "/" + code + "/"

    def accessToken(self):
        return "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"

    def rootData(self):
        return "data/"

################################
#   path类本地
################################

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

    def developerPath(self, id):
        return self.rootData() + self.codeName + '/developer/' + id + '.json'

######################################
#   github API
######################################
    def comLstiUrl(self, page):
        return "https://api.github.com/repos/" + self.gitName + \
               "commits?per_page=100&page=" + str(page) + \
               "&access_token=" + self.accessToken()

    def issueLstiUrl(self, page):
        return "https://api.github.com/repos/" + self.gitName + \
               "issues?per_page=100&page=" + str(page) + \
               "&access_token=" + self.accessToken()

    def commitUrl(self, Sha):
        return "https://api.github.com/repos/" + self.gitName + "commits/" + str(Sha) + "?access_token=" + self.accessToken()

    def issueUrl(self, number):
        return "https://api.github.com/repos/" + self.gitName + "issues/" + str(number) + "?access_token=" + self.accessToken()

    def treeUrl(self, urlInitial):
        return urlInitial + "?access_token=" + self.accessToken()

    def blobUrl(self, urlInitial):
        return urlInitial + "?access_token=" + self.accessToken()

    def developerUrl(self, id):
        return "https://api.github.com/users/" + id + "?access_token=" + self.accessToken()




