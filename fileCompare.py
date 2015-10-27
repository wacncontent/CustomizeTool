# compare with mooncake
from difflib import Differ
import re

mooncake_path = "C:/Users/Administrator/Documents/GitHub/azure-content-mooncake-pr"

def compareWithMooncake(relativePath, text):
    try:
        mooncakefile = open(mooncake_path+"/"+relativePath)
    except IOError:
        return text
    mooncakeLines = mooncakefile.readlines()
    mooncakefile.close()
    if len(mooncakeLines) == 0 or mooncakeLines[0].strip() == "<!-- not suitable for Mooncake -->":
        return text
    i=0
    remodeKeepLines = []
    keepCount = 0
    keeps = {}
    while i < len(mooncakeLines):
        if mooncakeLines[i].strip() == "<!-- keep by customization: begin -->":
            remodeKeepLines.append("<!-- keep by customization: begin -->\n")
            remodeKeepLines.append(str(keepCount)+"\n")
            keepCount+=1
            i+=1
            keepStr = ""
            while mooncakeLines[i].strip() != "<!-- keep by customization: end -->":
                keepStr +=  mooncakeLines[i]
                i+=1
            keeps["<!-- keep by customization: begin -->\n"+str(keepCount-1)+"\n"+mooncakeLines[i]] = "<!-- keep by customization: begin -->\n"+keepStr+"<!-- keep by customization: end -->\n"
        remodeKeepLines.append(mooncakeLines[i])
        i+=1
    differ = Differ()
    lines = [x+"\n" for x in text.split("\n")]
    lines[len(lines)-1] = lines[len(lines)-1][0:len(lines[len(lines)-1])-1]
    diff = list(differ.compare(remodeKeepLines, lines))
    i = 0
    result = ""
    while i<len(diff):
        if diff[i][0] == " ":
            result+=diff[i][2:]
        elif diff[i][0] == "+":
            if i+1<len(diff) and diff[i+1][0] == "-":
                result+=handleOneLine3(diff, i)[2:]
                i+=1
            else:
                result+=diff[i][2:]
        elif diff[i][0] == "-":
            update = checkUpdate(diff, i)
            result+=update[0][2:]
            i+=update[1]
        i+=1
    for k, v in keeps.items():
        result = result.replace(k,v);
    return result

def checkUpdate(diff, i):
    if i < len(diff)-2:
        if diff[i+1][0] == "?":
            return handleOneLine(diff, i)
        elif diff[i][1:].strip() == "<!-- deleted by customization":
            return handleDeletion(diff, i)
        elif diff[i][1:].strip() == "<!-- keep by customization: begin -->":
            return handleKeeping(diff, i)
        elif diff[i+1][0] == "+":
            return handleOneLine2(diff, i)
    return ["  ",0]

def handleOneLine(diff, i):
    delta_i = 2
    if "<!-- deleted by customization" not in diff[i] and "<!-- keep by customization: begin -->" not in diff[i]:
        delta_str = diff[i+2]
    elif "<!-- deleted by customization" in diff[i]:
        # TODO
        delta_str = diff[i]
    else:
        # TODO
        delta_str = diff[i]
    if i+3 < len(diff):
        if diff[i+3][0] == "?":
            delta_i = 3
    return [delta_str, delta_i]

def handleOneLine2(diff, i):
    if "<!-- deleted by customization" not in diff[i] and "<!-- keep by customization: begin -->" not in diff[i]:
        delta_str = diff[i+1]
    elif "<!-- deleted by customization" in diff[i]:
        # TODO
        delta_str = diff[i]
    else:
        # TODO
        delta_str = diff[i]
    return [delta_str, 1]

def handleOneLine3(diff, i):
    if "<!-- deleted by customization" not in diff[i+1] and "<!-- keep by customization: begin -->" not in diff[i+1]:
        delta_str = diff[i]
    elif "<!-- deleted by customization" in diff[i+1]:
        # TODO
        delta_str = diff[i+1]
    else:
        # TODO
        delta_str = diff[i+1]
    return delta_str

def handleDeletion(diff, i):
    delta_i=1
    delta_str = diff[i]
    while diff[i+delta_i][2:].strip() != "-->":
        if diff[i+delta_i][0] == "+" or diff[i+delta_i][0] == " ":
             delta_str += diff[i+delta_i][2:]
        delta_i+=1
    if delta_str[len(delta_str)-1] != "\n":
        delta_str += "\n-->\n"
    else:
        delta_str += "-->\n"
    return [delta_str, delta_i]

def handleKeeping(diff, i):
    delta_i=1
    delta_str = diff[i]
    extra = []
    while diff[i+delta_i][2:].strip() != "<!-- keep by customization: end -->":
        if diff[i+delta_i][0] == "-" or diff[i+delta_i][0] == " ":
             delta_str += diff[i+delta_i][2:]
        elif diff[i+delta_i][0] == "+":
            extra.append(diff[i+delta_i][2:])
        delta_i+=1
    if delta_str[len(delta_str)-1] != "\n":
        delta_str += "\n<!-- keep by customization: end -->\n"
    else:
        delta_str += "<!-- keep by customization: end -->\n"
    #for line in extra:
     #   delta_str+=line
    return [delta_str, delta_i]