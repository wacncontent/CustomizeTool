import glob
from setting import setting
import re
from os.path import isfile
from filecmp import cmp


ms_date_reg = 'ms.date="(?P<date>[^"]+)"'

def genFileList(fileName):
    output = open(fileName, 'w')
    inlcudeFileList = []
    for folder in setting["folders"]:
        fileList = glob.glob(setting["path"]+folder+"/*.md")
        newDocList = ""
        newDocCount = 0
        updatedDocList = ""
        updatedDocCount = 0
        wordCount = 0
        for file in fileList:
            file = file.replace("\\", "/")
            fileType = isUpdatedOrNew(file)
            if fileType == "new":
                newDocCount += 1
                newDocList += file[len(setting["path"]):]+"\n"
                output.writelines(file+"\n")
            elif fileType == "updated":
                updatedDocCount += 1
                updatedDocList += file[len(setting["path"]):]+"\n"
                output.writelines(file+"\n")
        newIncludes = ""
        newIncludeCount = 0
        updatedIncludes = ""
        updatedIncludeCount = 0
        for key in setting["includes_search_keys"][folder]:
            serviceFileList = [file.replace("\\", "/") for file in glob.glob(setting["path"]+"includes/*"+key+"*.md")]
            for file in serviceFileList:
                if file not in inlcudeFileList:
                    inlcudeFileList.append(file)
                    if isNew(file):
                        newIncludeCount += 1
                        newIncludes += file[len(setting["path"]):]+"\n"
                        output.writelines(file+"\n")
                    elif isUpdated(file):
                        updatedIncludeCount += 1
                        updatedIncludes += file[len(setting["path"]):]+"\n"
                        output.writelines(file+"\n")
        newDocListFile = open("output/newDocList/"+folder.replace("/", "-")+".txt", "w")
        updatedDocListFile = open("output/updatedDocList/"+folder.replace("/", "-")+".txt", "w")
        newDocListFile.writelines("new docs: "+str(newDocCount)+", word count: {word_count_TODO}\n"+newDocList+"\n"+"new includes: "+str(newIncludeCount)+"\n"+newIncludes)
        updatedDocListFile.writelines("updated docs: "+str(updatedDocCount)+"\n"+updatedDocList+"\n"+"updated includes: "+str(updatedIncludeCount)+"\n"+updatedIncludes)
        newDocListFile.close()
        updatedDocListFile.close()
    output.close()


def isUpdatedOrNew(file):
    if not setting["check_dates"]:
        return "new"
    cmpFile = setting["compare"]["path"]+file[len(setting["path"])-1:]
    try:
        oldFile = open(cmpFile,"r")
        old = oldFile.read()
        oldFile.close()
        if "<!-- not suitable for Mooncake -->" in old:
            return "not_suitable"
    except IOError:
        return "new"
    newFile = open(file,"r")
    new = newFile.read()
    newFile.close()
    
    newDate = re.findall(ms_date_reg, new)
    oldDate = re.findall(ms_date_reg, old)
    if newDate != oldDate:
        return "updated"
    return "not_changed"


def isNew(file):
    if not setting["check_dates"]:
        return True
    cmpFile = "lastMonth/"+file[len(setting["path"])-1:]
    return not isfile(cmpFile)

def isUpdated(file):
    if not setting["check_dates"]:
        return True
    cmpFile = "lastMonth/"+file[len(setting["path"])-1:]
    if cmp(file,cmpFile):
        return False
    cmpFile = setting["compare"]["path"]+file[len(setting["path"])-1:]
    oldFile = open(cmpFile,"r")
    old = oldFile.read()
    oldFile.close()
    if "<!-- not suitable for Mooncake -->" in old:
        return False
    return True
        