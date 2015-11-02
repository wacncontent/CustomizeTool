import glob
from setting import setting

def genFileList(fileName):
    output = open(fileName, 'w')
    for folder in setting["folders"]:
        fileList = glob.glob(setting["path"]+folder+"/*.md")
        for file in fileList:
            output.writelines(file+"\n")
    fileList = glob.glob(setting["path"]+"includes/*.md")
    for file in fileList:
        output.writelines(file+"\n")
    output.close()
