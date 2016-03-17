# compare with mooncake
from difflib import Differ, ndiff
import re
from setting import setting
from codecs import open

def compareWithMooncake(relativePath, text):
    try:
        mooncakefile = open(setting["compare"]["path"]+relativePath, 'r', "utf8")
    except IOError:
        return text
    mooncakeLines = mooncakefile.readlines()
    mooncakefile.close()
    if len(mooncakeLines) == 0 or mooncakeLines[0].strip() == "<!-- not suitable for Mooncake -->":
        return "<!-- not suitable for Mooncake -->\n\n"+text
    i=0
    remodeKeepLines = []
    keepCount = 0
    keeps = {}
    while i < len(mooncakeLines):
        if mooncakeLines[i].strip() == "\x10":
            remodeKeepLines.append("\x10\n")
            remodeKeepLines.append(str(keepCount)+"\n")
            keepCount+=1
            i+=1
            keepStr = ""
            while mooncakeLines[i].strip() != "\x11":
                keepStr +=  mooncakeLines[i]
                i+=1
            keeps["\x10\n"+str(keepCount-1)+"\n"+mooncakeLines[i]] = "\x10\n"+keepStr+"\x11\n"
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
            if diff[i][1:] == " ":
                if i+1<len(diff) and diff[i+1][0] == "-" and diff[i+1][1:].strip() == "":
                    result+="\n"
                i+=1
                continue
            elif i+1<len(diff) and diff[i+1].strip() == "- \x10":
                i+=1
                continue
            elif i+1<len(diff) and diff[i+1][0] == "-":
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
        elif diff[i][1:].strip() == "\x0e":
            return handleDeletion(diff, i)
        elif diff[i][1:].strip() == "\x10":
            return handleKeeping(diff, i)
        elif diff[i+1][0] == "+":
            return handleOneLine2(diff, i)
    return ["  ",0]

def handleOneLine(diff, i):
    delta_i = 2
    if "\x0e" not in diff[i] and "\x10" not in diff[i]:
        delta_str = diff[i+2]
    elif "\x0e" in diff[i] and "\x10" in diff[i]:
        dele = diff[i].find("\x0e")
        keep = diff[i].find("\x10")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i+2][2:], diff[i][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i+2][2:], diff[i][2:])+"\n"
    elif "\x0e" in diff[i]:
        delta_str = "  " + deleteCompare(diff[i+2][2:], diff[i][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i+2][2:], diff[i][2:])+"\n"
    if i+3 < len(diff):
        if diff[i+3][0] == "?":
            delta_i = 3
    return [delta_str, delta_i]

def handleOneLine2(diff, i):
    if "\x0e" not in diff[i] and "\x10" not in diff[i]:
        delta_str = diff[i+1]
    elif "\x0e" in diff[i] and "\x10" in diff[i]:
        dele = diff[i].find("\x0e")
        keep = diff[i].find("\x10")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i+1][2:], diff[i][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i+1][2:], diff[i][2:])+"\n"
    elif "\x0e" in diff[i]:
        delta_str = "  " + deleteCompare(diff[i+1][2:], diff[i][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i+1][2:], diff[i][2:])+"\n"
    return [delta_str, 1]

def handleOneLine3(diff, i):
    if "\x0e" not in diff[i+1] and "\x10" not in diff[i+1]:
        delta_str = diff[i]
    elif "\x0e" in diff[i+1] and "\x10" in diff[i+1]:
        dele = diff[i+1].find("\x0e")
        keep = diff[i+1].find("\x10")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i][2:], diff[i+1][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i][2:], diff[i+1][2:])+"\n"
    elif "\x0e" in diff[i+1]:
        delta_str = "  " + deleteCompare(diff[i][2:], diff[i+1][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i][2:], diff[i+1][2:])+"\n"
    return delta_str

def deleteCompare(new, old):
    leadingblank = new[:new.find(new.strip())]
    new = new.strip()
    old = old.strip()
    i = old.find("\x0e")
    j = old[i:].find("\x0f")
    deleted = old[i+1:i+j].strip()
    k = new.find(deleted)
    if k == -1:
        return new
    old_part = old[i+j+1:]
    print i, ", ", j
    print old_part
    kept=old[i:i+j+1]
    if old_part[:1] == "\x10":
        end = old_part.find("\x11")
        kept = kept+old_part[:end+1]
        old_part = old_part[end+1:]
    new_part = new[k+len(deleted):]
    if "\x0e" not in old_part and "\x10" not in old_part:
        delta_str = new_part
    elif "\x0e" in old_part and "\x10" in old_part:
        dele = old_part.find("\x0e")
        keep = old_part.find("\x10")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "\x0e" in old_part:
        delta_str = deleteCompare(new_part, old_part)
    else:
        delta_str = keepCompare(new_part, old_part)
    return leadingblank + new[:k]+kept+delta_str

def keepCompare(new, old):
    leadingblank = new[:new.find(new.strip())]
    new = new.strip()
    old = old.strip()
    i = old.find("\x10")
    j = old.find("\x11")
    kept = old[i:j+1]
    temp = removeDeleteAndKeep(old.replace(kept, " \033 "))
    differ = Differ()
    oldList = handlePunctuation(filter(lambda a: a != "", temp.split(" ")))
    newList = handlePunctuation(new.split(" "))
    diff = list(ndiff(oldList, newList))
    count = 0
    for c in diff:
        if c == "- \033":
            break
        elif c[0] == ' ' or c[0] == '+':
            count+=1
    old_part = old[j+1:]
    new_part = " "+" ".join(newList[count:])
    if "\x0e" not in old_part and "\x10" not in old_part:
        delta_str = new_part
    elif "\x0e" in old_part and "\x10" in old_part:
        dele = old_part.find("\x0e")
        keep = old_part.find("\x10")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "\x0e" in old_part:
        delta_str = deleteCompare(new_part, old_part)
    else:
        delta_str = keepCompare(new_part, old_part)
    if count == 0:
        result = leadingblank+kept+" "+delta_str
    else:
        result = leadingblank+" ".join(newList[:count])+" "+kept+" "+delta_str
    result = result.replace(" \b", "")
    return result

def removeDeleteAndKeep(old):
    old = re.sub("\n[ \t\r\f\v]*(\x10|\x11|\x0e[^\x0f]+\x0f)[ \t\r\f\v]*\n", "\n", old)
    old = re.sub(r"[ \t\r\f\v]*(\x10|\x11|\x0e[^\x0f]+\x0f)[ \t\r\f\v]*([,.?!:;])", r"\2", old)
    old = re.sub("(\x10|\x11|\x0e[^\x0f]+\x0f)[ \t\r\f\v]*", "", old)
    return old

def handleDeletion(diff, i):
    delta_i=1
    delta_str = diff[i]
    while diff[i+delta_i][2:].strip() != "\x0f":
        if diff[i+delta_i][0] == "+" or diff[i+delta_i][0] == " ":
             delta_str += diff[i+delta_i][2:]
        delta_i+=1
    if delta_str[len(delta_str)-1] != "\n":
        delta_str += "\n\x0f\n"
    else:
        delta_str += "\x0f\n"
    return [delta_str, delta_i]

def handleKeeping(diff, i):
    delta_i=1
    delta_str = diff[i]
    extra = []
    while diff[i+delta_i][2:].strip() != "\x11":
        if diff[i+delta_i][0] == "-" or diff[i+delta_i][0] == " ":
             delta_str += diff[i+delta_i][2:]
        elif diff[i+delta_i][0] == "+":
            extra.append(diff[i+delta_i][2:])
        delta_i+=1
    
    if delta_str[len(delta_str)-1] != "\n":
        delta_str += "\n\x11\n"
    else:
        delta_str += "\x11\n"
    #for line in extra:
     #   delta_str+=line
    return [delta_str, delta_i]

def createComment(globalText, mooncakeText):
    differ = Differ()
    mooncakeIndex = mooncakeText.find("/>")+2
    mooncakeIndex = mooncakeIndex + mooncakeText[mooncakeIndex:].find("/>")+2
    globalIndex = globalText.find("/>")+2
    globalIndex = globalIndex + globalText[globalIndex:].find("/>")+2

    mooncakeTags = re.search("\<tags\s*\n?(.*\n)*.*/\>", mooncakeText[:mooncakeIndex])
    globalTags = re.search("\<tags\s*\n?(.*\n)*.*/\>", globalText[:globalIndex])
    tagS = ""
    if globalTags != None:
        tagS = globalText[:globalTags.span()[1]]
        globalText = globalText[globalTags.span()[1]:]
        mooncakeText = mooncakeText[mooncakeTags.span()[1]:]
        
    globalLines = [line+"\n" for line in globalText.split("\n")]
    mooncakeLines = [line+"\n" for line in mooncakeText.split("\n")]
    print globalLines
    print mooncakeLines
    diff = list(differ.compare(globalLines, mooncakeLines))
    print "\n".join(diff)
    if len(diff) == 0:
        return ""
    i = 0
    result = []
    while i < len(diff):
        if diff[i][0] == " ":
            result.append(diff[i][2:])
            i += 1
        elif diff[i][0] == "-":
            if i+1 < len(diff) and diff[i+1][0] == "?":
                result.extend(mergeDiff(diff[i][2:len(diff[i])-1], diff[i+2][2:len(diff[i+2])-1]))
                i += 3
            elif i+1 < len(diff) and diff[i+1][0] == "+":
                result.extend(mergeDiff(diff[i][2:len(diff[i])-1], diff[i+1][2:len(diff[i+1])-1]))
                i += 2
            else:
                result.append("\x0e\n")
                while i < len(diff) and diff[i][0] == "-":
                    result.append(diff[i][2:])
                    i += 1
                result.append("\x0f\n")
        elif diff[i][0] == "+":
            
            if i+1 < len(diff) and diff[i][0+1] == "-":
                result.extend(mergeDiff(diff[i+1][2:len(diff[i+1])-1], diff[i][2:len(diff[i])-1]))
                i += 2
            else:
                result.append("\x10\n")
                while i < len(diff) and diff[i][0] == "+":
                    result.append(diff[i][2:])
                    i += 1
                result.append("\x11\n")
        else:
            i += 1
    return tagS + mergeDeleteAndKeep(result)

def handlePunctuation(words):
    result = []
    for word in words:
        word = word.strip()
        if word[len(word)-1:len(word)] == "." or word[len(word)-1:len(word)] == "?" or word[len(word)-1:len(word)] == "," or word[len(word)-1:len(word)] == ":" or word[len(word)-1:len(word)] == ";":
            if word[:len(word)-1] != "":
                result.append(word[:len(word)-1])
            result.append("\b"+word[len(word)-1])
        else:
            result.append(word)
    return result

def mergeDiff(global_, mooncake):
    if global_.strip() == "":
        return ["\x10\n", mooncake+"\n", "\x11\n"]
    leadingBlank = global_.find(global_.strip())
    if global_.strip() == mooncake.strip():
        return [global_ + "\n"]
    globalText = handlePunctuation(global_.strip().split(" "))
    mooncakeText = handlePunctuation(mooncake.strip().split(" "))
    differ = Differ()
    diff = list(differ.compare(globalText, mooncakeText))
    i = 0
    result = []
    while i < len(diff):
        if diff[i][0] == " ":
            result.append(diff[i][2:])
            i += 1
        elif diff[i][0] == "-":
            result.append("\x0e")
            while i < len(diff) and diff[i][0] == "-":
                result.append(diff[i][2:])
                i += 1
            result.append("\x0f")
        elif diff[i][0] == "+":
            result.append("\x10")
            while i < len(diff) and diff[i][0] == "+":
                result.append(diff[i][2:])
                i += 1
            result.append("\x11")
        else:
            i += 1
    text, count, percentage = mergeDeleteAndKeep2(result)
    if ((count < 0.1*float(len(globalText)) or count == 1) and percentage < 0.5) or global_.strip().find(mooncake.strip()) != -1 or mooncake.strip().find(global_.strip()) != -1:
        return [global_[:leadingBlank]+text.replace(" \b","").replace("\b","").replace("\x0f \x10", "\x0f\x10")]
    
    return ["\x0e\n", global_+"\n", "\x0f\n", "\x10\n", mooncake+"\n", "\x11\n"]

def mergeDeleteAndKeep2(lines):
    length = len(lines)
    result = []
    i = 0
    modificationCount = 0
    len_del = 0
    len_kept = 0
    while i < length:
        deletes = []
        keeps = []
        if lines[i] == "\x0e":
            while i < length and lines[i] == "\x0e":
                i += 1
                while i < length and lines[i] != "\x0f":
                    deletes.append(lines[i])
                    i += 1
                i += 1
                if i < length and lines[i] == "\x10":
                    i += 1
                    while i < length and lines[i] != "\x11":
                        keeps.append(lines[i])
                        i += 1
                    i+=1
        elif lines[i] == "\x10":
            while i < length and lines[i] == "\x10":
                i += 1
                while i < length and lines[i] != "\x11":
                    keeps.append(lines[i])
                    i += 1
                i += 1
                if i < length and lines[i] == "\x0e":
                    i += 1
                    while i < length and lines[i] != "\x0f":
                        deletes.append(lines[i])
                        i += 1
                    i+=1
        else:
            result.append(lines[i])
            i+=1
        if len(deletes) > 0:
            modificationCount += 1
            result.append("\x0e")
            len_del += len(deletes)+2
            result.extend(deletes)
            result.append("\x0f")
        if len(keeps) > 0:
            result.append("\x10")
            len_kept += len(keeps)+2
            result.extend(keeps)
            result.append("\x11")
    text = re.sub("\s*\x10\s*\x11\s*",""," ".join(result))
    text = addContext(text)
    return text+"\n", modificationCount, float(len_del+len_kept)/float(len(result))

def addContext(text):
    replaceReg = "(\x0e ([^\>]+) \x0f \x10 ([^\>]+) \x11)"
    matches = re.findall(replaceReg, text)
    for match in matches:
        replactions = re.findall(re.escape(match[1]), text[:text.find(match[0])])
        if len(replactions)>0:
            added = re.findall("(( [^\s]+ )?"+re.escape(match[0])+"( [^\s]+ )?)", text)
            if added[0][1] == "":
                added_first = " "
                beginSpace = ""
            else:
                added_first = added[0][1]
                beginSpace = " "
            if added[0][2] == "":
                added_second = " "
                endingSpace = ""
            else:
                added_second = added[0][2]
                endingSpace = " "
            text = text.replace(added[0][0], beginSpace+"\x0e"+added_first+match[1]+added_second+"\x0f "+"\x10"+added_first+match[2]+added_second+"\x11"+endingSpace)
    return text

def mergeDeleteAndKeep(lines):
    length = len(lines)
    result = []
    i = 0
    while i < length:
        j = i
        e = 0
        while j < length and (lines[j] == "\x0e\n" or lines[j] == "\x10\n"):
            if lines[j] == "\x0e\n":
                j += 1
                while lines[j] != "\x0f\n":
                    j += 1
                j += 1
            e = 0
            while j < length and lines[j].strip() == "":
                e += 1
                j += 1
            if j >= length:
                break
            if lines[j] == "\x10\n":
                j += 1
                while lines[j] != "\x11\n":
                    j += 1
                j += 1
                e = 0
                while j < length and lines[j].strip() == "":
                    e += 1
                    j += 1
            while j < length and lines[j] != "\x0e\n" and lines[j] != "\x10\n" and (lines[j].find("\x0e") != -1 or lines[j].find("\x10") != -1 or re.match("\s*\!\[.*\]\s*(\[.+\]|\(.+\))\s*",lines[j])) != None:
                j += 1
                e = 0
                while j < length and lines[j].strip() == "":
                    e += 1
                    j += 1
        j = j - e
        if j > i:
            deletes, keeps = handleMerge(lines, i, j)
            if "".join(deletes).strip() != "":
                result.append("\x0e\n")
                result.extend(deletes)
                result.append("\x0f\n")
            if "".join(keeps).strip() != "":
                result.append("\x10\n")
                result.extend(keeps)
                result.append("\x11\n")
            i = j
        else:
            result.append(lines[i])
            i += 1
    l = len(result)
    if len(result[l-1]) != 0 and result[l-1][len(result[l-1])-1] == "\n":
        result[l-1] = result[l-1][:len(result[l-1])-1]
    return "".join(result)

def handleMerge(lines, i, j):
    k = i
    position = "o"
    deletes = []
    keeps = []
    while k < j:
        if lines[k] == "\x0e\n":
            position = "d"
        elif lines[k] == "\x0f\n":
            position = "o"
        elif lines[k] == "\x10\n":
            position = "k"
        elif lines[k] == "\x11\n":
            position = "o"
        else:
            if position == "d":
                deletes.append(lines[k])
            elif position == "k":
                keeps.append(lines[k])
            elif position == "o":
                deletes.append(removeKeeps(lines[k]))
                keeps.append(removeDeletes(lines[k]))
        k += 1
    return deletes, keeps

def removeKeeps(line):
    result = re.sub("\x10 [^<]* \x11","",line)
    result = re.sub("\x0e ([^<]*) \x0f",r"\1",result)
    return result

def removeDeletes(line):
    result = re.sub("\x0e [^<]* \x0f","",line)
    result = re.sub("\x10 ([^<]*) \x11",r"\1",result)
    return result

def getDeletionAndReplacement(result):
    replaceReg = "\x0e ([^\x0f]+) \x0f\x10 ([^\x11]+) \x11"
    deletionReg = "\x0e ([^\x0f]+) \x0f"

    replaceMatch = re.findall(replaceReg,result)
    deletionMatch = re.findall(deletionReg,result)
    replacement = [{"deleted":match[0], "replace":match[1]} for match in replaceMatch]
    deletion = [match for match in deletionMatch]
    return deletion, replacement

def outputDeletionAndReplacement(deletion, replacement, mdFile):
    file = open(setting["getDeletionAndReplacement"]["path"]+mdFile,"w")
    if len(deletion) > 0:
        file.write("deletion:\n\n")
    for deleted in deletion:
        deleted = "\t\t"+"\n\t\t".join(deleted.split("\n"))
        file.write("deleted:\n\n"+deleted+"\n\nreason: ()\n\n")
    if len(replacement) > 0:
        file.write("replacement:\n\n")
    for replace in replacement:
        deleted = "\t\t"+"\n\t\t".join(replace["deleted"].split("\n"))
        replaced = "\t\t"+"\n\t\t".join(replace["replace"].split("\n"))
        file.write("deleted:\n\n"+deleted+"\n\nreplaced by:\n\n"+replaced+"\n\nreason: ()\n\n")
    file.close()