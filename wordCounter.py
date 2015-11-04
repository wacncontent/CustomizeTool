from os import popen4
from setting import setting

def wordCounts(filename):
    fin, fout = popen4("powershell -ExecutionPolicy Unrestricted -File ./fileSize.ps1 "+filename)
    count = int(fout.read())
    fin.close()
    fout.close()
    return count

def countAll():
    for folder in setting["folders"]:
        filename = "output/newDocList/"+folder.replace("/", "-")+".txt"
        count = wordCounts(filename)
        file = open(filename,"r")
        lines = file.read()
        file.close()
        file = open(filename,"w")
        file.write(lines.replace("{word_count_TODO}", str(count)))
        file.close()
