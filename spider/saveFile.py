import sys
import os


class saveFile:
    fileName = ""

    def __init__(self, path, con):
        print(con)
        f = open(path, 'a', encoding='utf-8')
        f.write(con)
        f.close()
