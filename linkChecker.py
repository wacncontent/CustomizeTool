import urllib2
import re
url_reg = r'("|\()\s*(?P<url>https*://[^"|^\s|^\)]+)\s*("|\))'
url_reg2 = '\[([^\[|^\]]*)\]:\s*(?P<url>https*://[^"|^\s]+)\s*("[^"]*")\s*(\n|$)'
def checkLinks(text):
    links =  [a[1] for a in re.findall(url_reg, text)]
    links.extend([a[1] for a in re.findall(url_reg2, text)])
    return links

def findRedirect(urllist):
    output = open("newLinks.txt", "w")
    errorOut = open("errorLinks.txt", "w")
    oldLinkFile = open("oldLinks.txt", "a")
    for url in urllist:
        print("processing: "+url)
        oldLinkFile.write(url+"\n")
        try:
            link = urllib2.urlopen(url)
            finalurl = link.geturl()
        except Exception as e:
            errorOut.writelines("url: "+url+"\nerror: "+str(e)+"\n")
            continue
        if not urlEqual(url, finalurl):
            print("replaced by: "+finalurl+"\n")
            output.writelines(url.replace("=", "{equal}")+" = "+finalurl.replace("=", "{equal}")+"\n")
        else:
            print("not replaced\n")
    output.close()
    errorOut.close()
    oldLinkFile.close()

def getOldLinks():
    input = open("oldLinks.txt", "r")
    return [link.strip() for link in input.readlines()]

def urlEqual(url, finalurl):
    url_pure1 = r"https?://(?P<domain>.+)(en-us/)(?P<path>.+)"
    url_pure2 = r"https?://(?P<url>.+)"
    m1 = re.match(url_pure1, url)
    if m1 == None:
        m1 = re.match(url_pure2, url)
        d1 = m1.groupdict()
        url1 = d1["url"]
    else:
        d1 = m1.groupdict()
        url1 = d1["domain"] + d1["path"]
    m2 = re.match(url_pure1, finalurl)
    if m2 == None:
        m2 = re.match(url_pure2, finalurl)
        d2 = m2.groupdict()
        url2 = d2["url"]
    else:
        d2 = m2.groupdict()
        url2 = d2["domain"] + d2["path"]
    return url1 == url2