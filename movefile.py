import os
import re

class mvpic:
    destDir = r'D:\pic'

    def __init__(self):
        self.number = 0
        self.jpg = re.compile(r'\.jpg')
        try:
            os.mkdir(self.destDir)
        except:
            pass

    def getFlie(self, dirPath):
        try:
            #os.chdir(dirPath)
            #unitList = os.listdir(r'.')
            unitList = os.listdir(dirPath)
            for i in unitList:
                filePath = os.path.join(dirPath, i)
                if os.path.isdir(filePath):
                    self.getFlie(filePath)
                else:
                    print(filePath)
                    if self.jpg.search(i):
                        self.cpFile(filePath)
            #os.chdir('..')
        except Exception as e:
            print(e)

    def cpFile(self, filePath):
        self.number += 1
        open(os.path.join(self.destDir, str(self.number) + r'.jpg'), "wb").write(open(filePath, "rb").read())

if __name__ == '__main__':
    t = mvpic()
    t.getFlie(r'D:\download\chrome download\fd0151a39e86aa7f3af98bc93d28792f')
    print('all %d'%t.number)