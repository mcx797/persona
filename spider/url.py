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

################################
#   path类本地
################################

    def commitListPath(self):
        return "../data/" + self.codeName + "/commitList"

    def issueListPath(self):
        return "../data/" + self.codeName + "/issueList"

    def comLstConPath(self, i):
        return self.commitListPath() + '/' + str(i) + '.json'

    def issueLstConPath(self, i):
        return self.issueListPath() + '/' + str(i) + '.json'

    def commitPath(self, sha):
        return "../data/" + self.codeName + '/commit/' + sha + '.json'

    def issuePath(self, number):
        return "../data/" + self.codeName + '/issue/' + str(number) + '.json'

    def treePath(self, sha):
        return "../data/" + self.codeName + '/tree/' + str(sha) + '.json'

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

    def treeUrl(self, sha):
        return sha + "?access_token=" + self.accessToken()


