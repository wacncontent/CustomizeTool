# compare with mooncake
from difflib import Differ, ndiff
import re
from setting import setting

def compareWithMooncake(relativePath, text):
    try:
        mooncakefile = open(setting["compare"]["path"]+relativePath)
    except IOError:
        return text
    mooncakeLines = mooncakefile.readlines()
    mooncakefile.close()
    if len(mooncakeLines) == 0 or mooncakeLines[0].strip() == "<!-- not suitable for Mooncake -->":
        return "".join(mooncakeLines)
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
    elif "<!-- deleted by customization" in diff[i] and "<!-- keep by customization: begin -->" in diff[i]:
        dele = diff[i].index("<!-- deleted by customization")
        keep = diff[i].index("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(diff[i+2], diff[i])
        else:
            delta_str = keepCompare(diff[i+1], diff[i])
    elif "<!-- deleted by customization" in diff[i]:
        delta_str = deleteCompare(diff[i+2], diff[i])
    else:
        delta_str = keepCompare(diff[i+1], diff[i])
    if i+3 < len(diff):
        if diff[i+3][0] == "?":
            delta_i = 3
    return [delta_str, delta_i]

def handleOneLine2(diff, i):
    if "<!-- deleted by customization" not in diff[i] and "<!-- keep by customization: begin -->" not in diff[i]:
        delta_str = diff[i+1]
    elif "<!-- deleted by customization" in diff[i] and "<!-- keep by customization: begin -->" in diff[i]:
        dele = diff[i].index("<!-- deleted by customization")
        keep = diff[i].index("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(diff[i+1], diff[i])
        else:
            delta_str = keepCompare(diff[i+1], diff[i])
    elif "<!-- deleted by customization" in diff[i]:
        delta_str = deleteCompare(diff[i+1], diff[i])
    else:
        delta_str = keepCompare(diff[i+1], diff[i])
    return [delta_str, 1]

def handleOneLine3(diff, i):
    if "<!-- deleted by customization" not in diff[i+1] and "<!-- keep by customization: begin -->" not in diff[i+1]:
        delta_str = diff[i]
    elif "<!-- deleted by customization" in diff[i+1] and "<!-- keep by customization: begin -->" in diff[i+1]:
        dele = diff[i+1].index("<!-- deleted by customization")
        keep = diff[i+1].index("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(diff[i], diff[i+1])
        else:
            delta_str = keepCompare(diff[i], diff[i+1])
    elif "<!-- deleted by customization" in diff[i+1]:
        delta_str = deleteCompare(diff[i], diff[i+1])
    else:
        delta_str = keepCompare(diff[i], diff[i+1])
    return delta_str

def deleteCompare(new, old):
    i = old.index("<!-- deleted by customization")
    j = old[i:].index("-->")
    deleted = old[i+30:i+j].strip()
    try: 
        k = new.index(deleted)
    except Exception:
        print deleted, new
        return new
    old_part = old[i+j+3:]
    kept=old[i:i+j+3]
    if old_part[:37] == "<!-- keep by customization: begin -->":
        end = old_part.index("<!-- keep by customization: end -->")
        kept = kept+old_part[:end+35]
        old_part = old_part[end+35:]
    new_part = new[k+len(deleted):]
    if "<!-- deleted by customization" not in old_part and "<!-- keep by customization: begin -->" not in old_part:
        delta_str = new_part
    elif "<!-- deleted by customization" in old_part and "<!-- keep by customization: begin -->" in old_part:
        dele = old_part.index("<!-- deleted by customization")
        keep = old_part.index("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "<!-- deleted by customization" in old_part:
        delta_str = deleteCompare(new_part, old_part)
    else:
        delta_str = keepCompare(new_part, old_part)
    return new[:k]+kept+delta_str

def keepCompare(new, old):
    i = old.index("<!-- keep by customization: begin -->")
    j = old.index("<!-- keep by customization: end -->")
    kept = old.replace(old[i:j+35])
    temp = removeDeleteAndKeep(old.replace(keep, "\033"))
    diff = list(ndiff(temp, new))
    count = 0
    for c in diff:
        if c == "- \033":
            break
        elif c[0] == ' ' or c[0] == '+':
            count+=1
    old_part = old[j+35:]
    new_part = new[count+1:]
    if "<!-- deleted by customization" not in old_part and "<!-- keep by customization: begin -->" not in old_part:
        delta_str = new_part
    elif "<!-- deleted by customization" in old_part and "<!-- keep by customization: begin -->" in old_part:
        dele = old_part.index("<!-- deleted by customization")
        keep = old_part.index("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "<!-- deleted by customization" in old_part:
        delta_str = deleteCompare(new_part, old_part)
    else:
        delta_str = keepCompare(new_part, old_part)
    return new[:count+1]+kept+delta_str

def removeDeleteAndKeep(old):
    old = old.replace("<!-- keep by customization: begin -->", "").replace("<!-- keep by customization: end -->", "")
    while True:
        try:
            i = old.index("<!-- deleted by customization")
            j = old[i:].index("-->")
        except Exception:
            return old
        old = old.replace(old[i:i+j+3], "")

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