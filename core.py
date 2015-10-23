#!/usr/bin/env python
# coding: GBK
# This is the core part of Mooncake which is used for replacing text by regular expression.

import ruleReader
import mdReader
import re
import os
import sys
from fileListGen import genFileList, global_article_path

__author__ = 'Steven'

class Core:

    def multiple_replace(self, dict, text):
        # Get const dict and regex dict individually
        constDict = dict[0]
        regexDict = dict[1]

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

        return text


    def customize(self, pMdList, pRuleDict):

        # Create result directory
        # os.mkdir('Archive')
        # iterate the markdown file list and do the replacing
        for mdFile in pMdList:
            result = ''
            print(mdFile)
            with open(mdFile, "r") as text:
                # for content in text.readlines():
                result = self.multiple_replace(pRuleDict, text.read())
                # print(result)
            # Write result into Archive/mdFile
            mdFile = mdFile[len(global_article_path)+1:]
            with open('output/'+mdFile, 'w') as bakFile:
                bakFile.write(result)
                print('\033[1;33m '+ mdFile+'\033[0m \033 customize success, the result file is: \033[1;32m'+ mdFile+'.bak\033[0m\n')

if __name__ == "__main__":
    genFileList("modified.txt")
    core = Core()
    rule = ruleReader.RuleReader()
    md = mdReader.MdReader()
    try:
        ruleDict = rule.getRules()
        mdList = md.getMdList()

        core.customize(mdList, ruleDict)
    except IOError as e:
        print(e)
        sys.exit()
