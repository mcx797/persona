class Url:
    authorName = ""
    codeName = ""
    gitName = ""

    def __init__(self, name, code):
        self.authorName = name
        self.codeName = code
        self.gitName = name + "/" + code + "/"
        print("url Initial")

