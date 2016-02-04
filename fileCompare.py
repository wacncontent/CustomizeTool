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
            if diff[i][1:] == " ":
                if i+1<len(diff) and diff[i+1][0] == "-" and diff[i+1][1:].strip() == "":
                    result+="\n"
                i+=1
                continue
            elif i+1<len(diff) and diff[i+1].strip() == "- <!-- keep by customization: begin -->":
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
        dele = diff[i].find("<!-- deleted by customization")
        keep = diff[i].find("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i+2][2:], diff[i][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i+2][2:], diff[i][2:])+"\n"
    elif "<!-- deleted by customization" in diff[i]:
        delta_str = "  " + deleteCompare(diff[i+2][2:], diff[i][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i+2][2:], diff[i][2:])+"\n"
    if i+3 < len(diff):
        if diff[i+3][0] == "?":
            delta_i = 3
    return [delta_str, delta_i]

def handleOneLine2(diff, i):
    if "<!-- deleted by customization" not in diff[i] and "<!-- keep by customization: begin -->" not in diff[i]:
        delta_str = diff[i+1]
    elif "<!-- deleted by customization" in diff[i] and "<!-- keep by customization: begin -->" in diff[i]:
        dele = diff[i].find("<!-- deleted by customization")
        keep = diff[i].find("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i+1][2:], diff[i][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i+1][2:], diff[i][2:])+"\n"
    elif "<!-- deleted by customization" in diff[i]:
        delta_str = "  " + deleteCompare(diff[i+1][2:], diff[i][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i+1][2:], diff[i][2:])+"\n"
    return [delta_str, 1]

def handleOneLine3(diff, i):
    if "<!-- deleted by customization" not in diff[i+1] and "<!-- keep by customization: begin -->" not in diff[i+1]:
        delta_str = diff[i]
    elif "<!-- deleted by customization" in diff[i+1] and "<!-- keep by customization: begin -->" in diff[i+1]:
        dele = diff[i+1].find("<!-- deleted by customization")
        keep = diff[i+1].find("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = "  " + deleteCompare(diff[i][2:], diff[i+1][2:])+"\n"
        else:
            delta_str = "  " + keepCompare(diff[i][2:], diff[i+1][2:])+"\n"
    elif "<!-- deleted by customization" in diff[i+1]:
        delta_str = "  " + deleteCompare(diff[i][2:], diff[i+1][2:])+"\n"
    else:
        delta_str = "  " + keepCompare(diff[i][2:], diff[i+1][2:])+"\n"
    return delta_str

def deleteCompare(new, old):
    leadingblank = new[:new.find(new.strip())]
    new = new.strip()
    old = old.strip()
    i = old.find("<!-- deleted by customization")
    j = old[i:].find("-->")
    deleted = old[i+29:i+j].strip()
    k = new.find(deleted)
    if k == -1:
        return new
    old_part = old[i+j+3:]
    kept=old[i:i+j+3]
    if old_part[:37] == "<!-- keep by customization: begin -->":
        end = old_part.find("<!-- keep by customization: end -->")
        kept = kept+old_part[:end+35]
        old_part = old_part[end+35:]
    new_part = new[k+len(deleted):]
    if "<!-- deleted by customization" not in old_part and "<!-- keep by customization: begin -->" not in old_part:
        delta_str = new_part
    elif "<!-- deleted by customization" in old_part and "<!-- keep by customization: begin -->" in old_part:
        dele = old_part.find("<!-- deleted by customization")
        keep = old_part.find("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "<!-- deleted by customization" in old_part:
        delta_str = deleteCompare(new_part, old_part)
    else:
        delta_str = keepCompare(new_part, old_part)
    return leadingblank + new[:k]+kept+delta_str

def keepCompare(new, old):
    leadingblank = new[:new.find(new.strip())]
    new = new.strip()
    old = old.strip()
    i = old.find("<!-- keep by customization: begin -->")
    j = old.find("<!-- keep by customization: end -->")
    kept = old[i:j+35]
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
    old_part = old[j+35:]
    new_part = " "+" ".join(newList[count:])
    if "<!-- deleted by customization" not in old_part and "<!-- keep by customization: begin -->" not in old_part:
        delta_str = new_part
    elif "<!-- deleted by customization" in old_part and "<!-- keep by customization: begin -->" in old_part:
        dele = old_part.find("<!-- deleted by customization")
        keep = old_part.find("<!-- keep by customization: begin -->")
        if dele < keep:
            delta_str = deleteCompare(new_part, old_part)
        else:
            delta_str = keepCompare(new_part, old_part)
    elif "<!-- deleted by customization" in old_part:
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
    old = re.sub("\n[ \t\r\f\v]*\<\!\-\- keep by customization: (begin|end) \-\-\>[ \t\r\f\v]*\n", "\n", old)
    old = re.sub(r"[ \t\r\f\v]*\<\!\-\- keep by customization: (begin|end) \-\-\>[ \t\r\f\v]*([,.?!:;])", r"\2", old)
    old = re.sub("\<\!\-\- keep by customization: (begin|end) \-\-\>[ \t\r\f\v]*", "", old)
    while True:
        i = old.find("<!-- deleted by customization")
        if i == -1:
            return old
        j = old[i:].find("-->")
        deleted = old[i+4:i+j]
        i_del = deleted.find("<!--")
        i_c = i + 4
        while i_del != -1:
            j+=old[i+j+3:].find("-->")+3
            i_c += i_del + 4
            deleted = old[i_c:i+j]
            i_del = deleted.find("<!--")
            
        if i > 0 and old[i-1] == '\n':
            old = re.sub(re.escape(old[i:i+j+3])+"[ \t\r\f\v]*\n?", "", old)
        else:
            if i > 0 and old[i-1] != ' ':
                old = old.replace(old[i:i+j+3], "")
            elif i+j+4<len(old) and old[i+j+3] == " " and (old[i+j+4] == "," or old[i+j+4] == "." or old[i+j+4] == "?" or old[i+j+4] == "!" or old[i+j+4] == ":" or old[i+j+4] == ":"):
                old = re.sub(" *"+re.escape(old[i:i+j+3])+"[ \t\r\f\v]*", "", old)
            elif i+j+4<len(old) and (old[i+j+3] == "," or old[i+j+3] == "." or old[i+j+3] == "?" or old[i+j+3] == "!" or old[i+j+3] == ":" or old[i+j+3] == ":"):
                old = re.sub(" *"+re.escape(old[i:i+j+3]), "", old)
            else:
                old = re.sub(re.escape(old[i:i+j+3])+"[ \t\r\f\v]*", "", old)

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
    diff = list(differ.compare(globalLines, mooncakeLines))
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
                result.append("<!-- deleted by customization\n")
                while i < len(diff) and diff[i][0] == "-":
                    result.append(diff[i][2:])
                    i += 1
                result.append("-->\n")
        elif diff[i][0] == "+":
            
            if i+1 < len(diff) and diff[i][0+1] == "-":
                result.extend(mergeDiff(diff[i+1][2:len(diff[i+1])-1], diff[i][2:len(diff[i])-1]))
                i += 2
            else:
                result.append("<!-- keep by customization: begin -->\n")
                while i < len(diff) and diff[i][0] == "+":
                    result.append(diff[i][2:])
                    i += 1
                result.append("<!-- keep by customization: end -->\n")
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
        return ["<!-- keep by customization: begin -->\n", mooncake+"\n", "<!-- keep by customization: end -->\n"]
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
            result.append("<!-- deleted by customization")
            while i < len(diff) and diff[i][0] == "-":
                result.append(diff[i][2:])
                i += 1
            result.append("-->")
        elif diff[i][0] == "+":
            result.append("<!-- keep by customization: begin -->")
            while i < len(diff) and diff[i][0] == "+":
                result.append(diff[i][2:])
                i += 1
            result.append("<!-- keep by customization: end -->")
        else:
            i += 1
    text, count, percentage = mergeDeleteAndKeep2(result)
    if ((count < 0.1*float(len(globalText)) or count == 1) and percentage < 0.5) or global_.strip().find(mooncake.strip()) != -1 or mooncake.strip().find(global_.strip()) != -1:
        return [global_[:leadingBlank]+text.replace(" \b","").replace("\b","").replace("--> <!--", "--><!--")]
    
    return ["<!-- deleted by customization\n", global_+"\n", "-->\n", "<!-- keep by customization: begin -->\n", mooncake+"\n", "<!-- keep by customization: end -->\n"]

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
        if lines[i] == "<!-- deleted by customization":
            while i < length and lines[i] == "<!-- deleted by customization":
                i += 1
                while i < length and lines[i] != "-->":
                    deletes.append(lines[i])
                    i += 1
                i += 1
                if i < length and lines[i] == "<!-- keep by customization: begin -->":
                    i += 1
                    while i < length and lines[i] != "<!-- keep by customization: end -->":
                        keeps.append(lines[i])
                        i += 1
                    i+=1
        elif lines[i] == "<!-- keep by customization: begin -->":
            while i < length and lines[i] == "<!-- keep by customization: begin -->":
                i += 1
                while i < length and lines[i] != "<!-- keep by customization: end -->":
                    keeps.append(lines[i])
                    i += 1
                i += 1
                if i < length and lines[i] == "<!-- deleted by customization":
                    i += 1
                    while i < length and lines[i] != "-->":
                        deletes.append(lines[i])
                        i += 1
                    i+=1
        else:
            result.append(lines[i])
            i+=1
        if len(deletes) > 0:
            modificationCount += 1
            result.append("<!-- deleted by customization")
            len_del += len(deletes)+2
            result.extend(deletes)
            result.append("-->")
        if len(keeps) > 0:
            result.append("<!-- keep by customization: begin -->")
            len_kept += len(keeps)+2
            result.extend(keeps)
            result.append("<!-- keep by customization: end -->")
    text = re.sub("\s*\<\!\-\- keep by customization: begin \-\-\>\s*\<\!\-\- keep by customization: end \-\-\>\s*",""," ".join(result))
    return text+"\n", modificationCount, float(len_del+len_kept)/float(len(result))

def mergeDeleteAndKeep(lines):
    length = len(lines)
    result = []
    i = 0
    while i < length:
        j = i
        e = 0
        while j < length and (lines[j] == "<!-- deleted by customization\n" or lines[j] == "<!-- keep by customization: begin -->\n"):
            if lines[j] == "<!-- deleted by customization\n":
                j += 1
                while lines[j] != "-->\n":
                    j += 1
                j += 1
            e = 0
            while j < length and lines[j].strip() == "":
                e += 1
                j += 1
            if j >= length:
                break
            if lines[j] == "<!-- keep by customization: begin -->\n":
                j += 1
                while lines[j] != "<!-- keep by customization: end -->\n":
                    j += 1
                j += 1
                e = 0
                while j < length and lines[j].strip() == "":
                    e += 1
                    j += 1
            while j < length and lines[j] != "<!-- deleted by customization\n" and lines[j] != "<!-- keep by customization: begin -->\n" and (lines[j].find("<!-- deleted by customization") != -1 or lines[j].find("<!-- keep by customization: begin -->") != -1 or re.match("\s*\!\[.*\]\s*(\[.+\]|\(.+\))\s*",lines[j])) != None:
                j += 1
                e = 0
                while j < length and lines[j].strip() == "":
                    e += 1
                    j += 1
        j = j - e
        if j > i:
            deletes, keeps = handleMerge(lines, i, j)
            if "".join(deletes).strip() != "":
                result.append("<!-- deleted by customization\n")
                result.extend(deletes)
                result.append("-->\n")
            if "".join(keeps).strip() != "":
                result.append("<!-- keep by customization: begin -->\n")
                result.extend(keeps)
                result.append("<!-- keep by customization: end -->\n")
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
        if lines[k] == "<!-- deleted by customization\n":
            position = "d"
        elif lines[k] == "-->\n":
            position = "o"
        elif lines[k] == "<!-- keep by customization: begin -->\n":
            position = "k"
        elif lines[k] == "<!-- keep by customization: end -->\n":
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
    result = re.sub("\<\!\-\- keep by customization: begin \-\-\> [^<]* \<\!\-\- keep by customization: end \-\-\>","",line)
    result = re.sub(r"\<\!\-\- deleted by customization ([^<]*) \-\-\>",r"\1",result)
    return result

def removeDeletes(line):
    result = re.sub("\<\!\-\- deleted by customization [^<]* \-\-\>","",line)
    result = re.sub(r"\<\!\-\- keep by customization: begin \-\-\> ([^<]*) \<\!\-\- keep by customization: end \-\-\>",r"\1",result)
    return result

def getDeletionAndReplacement(result):
    replacement = []
    deletion = []
    while True:
        i = result.find("<!-- deleted by customization")
        if i == -1:
            return deletion, replacement
        j = result[i:].find("-->")
        deleted = result[i+4:i+j]
        i_del = deleted.find("<!--")
        i_c = i + 4
        while i_del != -1:
            j+=result[i+j+3:].find("-->")+3
            i_c += i_del + 4
            deleted = result[i_c:i+j]
            i_del = deleted.find("<!--")
        deleted = result[i+29:i+j].strip()
        if result[i+j+3:].strip()[:37] == "<!-- keep by customization: begin -->":
            begin = result[i+j+3:].find("<!-- keep by customization: begin -->") + 37 + i+j+3
            end = result[i+j+3:].find("<!-- keep by customization: end -->")+i+j+3
            replace = result[begin:end].strip()
            d = {"deleted":deleted, "replace":replace}
            replacement.append(d)
            result = result[end+35:]
        else:
            deletion.append(deleted)
            result = result[i+j+3:]
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