#!/usr/bin/env python
# coding: GBK
# This is the core part of Mooncake which is used for replacing text by regular expression.

import ruleReader
import mdReader
import re
import os
import sys
from fileListGen import genFileList
from fileCompare import compareWithMooncake, removeDeleteAndKeep, createComment, getDeletionAndReplacement, outputDeletionAndReplacement
from codecs import open
from setting import setting
from linkChecker import checkLinks, getOldLinks, findRedirect
from relativeLinkChecker import checkRelativeLink
from wordCounter import countAll

__author__ = 'Steven'

class Core:

    def multiple_replace(self, dict, text):
        # Get const dict and regex dict individually
        constDict = dict[0]
        regexDict = dict[1]
        correctDict = dict[2]

        # Do the const string substitution
        if len(constDict) > 0:
            constRegex = re.compile("(%s)" % "|".join(map(re.escape, constDict.keys())))
            # const = re.compile("(%s)" % "|".join(map(lambda x:x, constDict.keys())))
            # For each match, look-up corresponding value in dictionary
            text = constRegex.sub(lambda mo: constDict[mo.string[mo.start():mo.end()]], text)

        # Do the regex substitution
        # regex = re.compile("(%s)" % "|".join(map(lambda x:x, regexDict.keys())))
        for k, v in regexDict.items():
            text = re.sub(k,v,text)

        if len(correctDict) > 0:
            correctRegex = re.compile("(%s)" % "|".join(map(re.escape, correctDict.keys())))
            text = correctRegex.sub(lambda mo: correctDict[mo.string[mo.start():mo.end()]], text)

        return text


    def customize(self, pMdList, pRuleDict):
        # Create result directory
        # os.mkdir('Archive')
        # iterate the markdown file list and do the replacing
        links = []
        for mdFile in pMdList:
            result = ''
            print(mdFile)
            if setting["language"] == "zh-cn":
                text = open(mdFile, "r", "utf8")
                try:
                    result = text.read()
                except IOError:
                    text.close()
                    text = open(mdFile, "r", "gbk")
                    result = text.read()
                    text.close()
            else:
                with open(mdFile, "r") as text:
                    # for content in text.readlines():
                    result = text.read()
                    # print(result)
            # Write result into Archive/mdFile
            if setting["updateLinks"]:
                links.extend(checkLinks(result))
            result = self.multiple_replace(pRuleDict, result)
            mdFile = mdFile[len(setting["path"])-1:]
            print mdFile
            if setting["language"] == "zh-cn":
                if setting["compare"]["compare"]:
                    result = compareWithMooncake(mdFile, result)
                bakFile = open(setting["output_folder"]+mdFile, 'w', "utf8")
            else:
                if setting["compare"]["compare"]:
                    result = compareWithMooncake(mdFile, result)
                bakFile = open(setting["output_folder"]+mdFile, 'w')
            bakFile.write(result)
            bakFile.close()
            if setting["removeComment"]["remove"] == True:
                if setting["language"] == "zh-cn":
                    removeCommentFile = open(setting["removeComment"]["path"]+mdFile, 'w', "utf8")
                else:
                    removeCommentFile = open(setting["removeComment"]["path"]+mdFile, 'w')
                removeCommentResult = removeDeleteAndKeep(result)
                removeCommentFile.write(removeCommentResult)
                removeCommentFile.close()
                checkRelativeLink(removeCommentResult)
            print('\033[1;33m '+ mdFile+'\033[0m \033 customize success, the result file is: \033[1;32m'+ mdFile+'.bak\033[0m\n')
        if setting["updateLinks"]:
            newLinkSet = set(links)
            oldLinkSet = set(getOldLinks())
            findRedirect(list(newLinkSet-oldLinkSet))

def addComment(mdList):
    for mdFile in mdList:
        filename = mdFile[len(setting["path"]):]
        print filename
        global_file = open(setting["addComment"]["globalPath"]+filename, "r")
        mooncake_file = open(setting["addComment"]["mooncakePath"]+filename, "r")
        output_file = open(setting["addComment"]["outputPath"]+filename, "w")
        result = createComment(global_file.read(), mooncake_file.read())
        output_file.write(result)
        global_file.close()
        mooncake_file.close()
        output_file.close()

def getDAR(mdList):
    for mdFile in mdList:
        filename = mdFile[len(setting["path"]):]
        print "processing file: " + filename
        file = open(setting["getDeletionAndReplacement"]["input"]+filename, "r")
        result = file.read()
        file.close()
        deletion, replacement = getDeletionAndReplacement(result)
        if len(deletion) > 0 or len(replacement) > 0:
            outputDeletionAndReplacement(deletion, replacement, filename)


if __name__ == "__main__":
    if setting["updateFileList"] == True:
        genFileList("modified.txt")
    core = Core()
    rule = ruleReader.RuleReader()
    md = mdReader.MdReader()
    try:
        mdList = md.getMdList()
        if setting["customize"]:
            ruleDict = rule.getRules()
            core.customize(mdList, ruleDict)
        if setting["wordCount"]:
            countAll()
        if setting["addComment"]["add"]:
            addComment(mdList)
        if setting["getDeletionAndReplacement"]["get"]:
            getDAR(mdList)
    except IOError as e:
        print(e)
        sys.exit()

