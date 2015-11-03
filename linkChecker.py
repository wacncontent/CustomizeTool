import urllib2
import re
url_reg = r'("|\()\s*(?P<url>https*://[^"|^\s]+)\s*("|\))'
def checkLinks(text):
    return [a[1] for a in re.findall(url_reg, text)]

def findRedirect(urllist):
    output = open("newLinks.txt", "w")
    errorOut = open("errorLinks.txt", "w")
    oldLinkFile = open("oldLinks.txt", "a")
    for url in urllist:
        oldLinkFile.write(url+"\n")
        print("processing: "+url)
        try:
            link = urllib2.urlopen(url)
            finalurl = link.geturl()
        except Exception as e:
            errorOut.writelines("url: "+url+"\nerror: "+str(e)+"\n")
            continue
        if url != finalurl:
            output.writelines(url.replace("=", "{equal}")+" = "+finalurl.replace("=", "{equal}")+"\n")
    output.close()
    errorOut.close()
    oldLinkFile.close()

def getOldLinks():
    input = open("oldLinks.txt", "r")
    return [link.strip() for link in input.readlines()]

def urlEqual(url, finalurl):
    url_pure = r"https?://(www\.)?(?P<domain>.+)(en-us/)?(?P<path>.+)"
    m1 = re.match(url_pure, url)
    m2 = re.match(url_pure, finalurl)
    d1 = m1.groupdict()
    d2 = m2.groupdict()
    return d1["domain"]!=d2["domain"] or d1["path"]!=d2["path"]