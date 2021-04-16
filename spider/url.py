class Url:
    authorName = ""
    codeName = ""
    gitName = ""

    def __init__(self, name, code):
        self.authorName = name
        self.codeName = code
        self.gitName = name + "/" + code + "/"
        print("url Initial")

    def accessToken(self):
        return "82bc8acf6de0cda714a17151c2ada6ce79fe1e26"

################################
#   path类本地
################################

    def commitListPath(self):
        return "../data/" + self.codeName + "/commitList"

    def comLstConPath(self, i):
        return self.commitListPath() + '/' + str(i) + '.json'

######################################
#   github API
######################################
    def comLstiUrl(self, page):
        return "https://api.github.com/repos/" + self.gitName + \
               "commits?per_page=100&page=" + str(page) + \
               "&access_token=" + self.accessToken()
