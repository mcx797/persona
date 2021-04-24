import base64


class Decode64:

    def __init__(self):
        print("Initial decoder")

    def baDecoder(self, strIn):
        temp = base64.b64decode(strIn)
        return temp.decode()

    def containDecoder(self, strIn):
        strspl = strIn.split('\n')
        strReturn = ""
        for i in strspl:
            strReturn += self.baDecoder(i)
        return strReturn