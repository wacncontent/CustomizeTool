#!/usr/bin/env python
# coding: GBK
# Date  : 2015/09/03
# Version: 0.1
import sys
from collections import OrderedDict

__author__ = 'Steven'

ESCAPE_RULES = {"{equal}":"="}

class RuleReader:
    def __init__(self):
        # Initialize empty rule dictionary
        self.ruleDict = OrderedDict()
        # ruleDict just for regex substitution
        self.regexDict = OrderedDict()
        self.lineNum = 0
        # Default area is const string's substitution
        self.isConst = True
    # Function to get rules from "rules.txt"
    def getRules(self):
        RULE_FILE = 'rules.md'
        COMMENT_PREFIX = '#'
        RULE_SEP = '='
        UNSURE = '???'
        DELETE_FLAG = 'DELETE'
        DELETE_CONTENT = ''
        CONST_FLAG = '[CONST]'
        REGULAR_FLAG = '[REGEX]'
        try:
            with open(RULE_FILE, 'r') as fRule:
                for line in fRule:
                    # Increase our line count
                    self.lineNum += 1
                    trimedLine = line.strip()
                    # Check if the line is comment or space
                    if trimedLine == "" or trimedLine.startswith(COMMENT_PREFIX) or trimedLine == CONST_FLAG:
                        continue
                    # Add for check REGULAR EXPRESSION area, when find it just update the isRegex flag
                    if trimedLine == REGULAR_FLAG:
                        self.isConst = False
                        continue
                    # Check if the line is in good format
                    if trimedLine.find(RULE_SEP) == -1 or trimedLine.startswith(RULE_SEP) or trimedLine.endswith(RULE_SEP):
                        sys.stderr.write('\033[1;31m Warning: Line %d has bad rule format!\033[0m\n' %(self.lineNum))
                        # print('\033[31m Warning: Line %d has bad rule format!\033[0m\n' %(self.lineNum))
                        sys.exit()
                    # Check format OK, let's add it to our rules dictionary
                    ruleList = trimedLine.split("=", 1)
                    # ??? would be skipped too if it is written in rule file by accident
                    key = self.escape(ruleList[0].strip())
                    value = self.escape(ruleList[1].strip())
                    if value == UNSURE:
                        continue
                    elif self.isConst == True:
                        # TODO Check for reduplicated key?
                        # Trim spaces in key & value
                        self.ruleDict[key] = (DELETE_CONTENT if value == DELETE_FLAG else value)
                    else:
                        self.regexDict[key] = (DELETE_CONTENT if value == DELETE_FLAG else value)
                # print(self.ruleDict, self.regexDict)
                print('\033[1;32m Finish reading all rules, keep moving...\033[0m')
                return self.ruleDict, self.regexDict
        except IOError as e:
            print("\033[1;31m rules.md doesn't exists!\033[0m\n")
            # print(e)
            # sys.exit()

    def escape(self,str):
        for k, v in ESCAPE_RULES.items():
            str = str.replace(k,v)
        return str

# only running when direct run this script
if '__main__' == __name__:
    ruleReader = RuleReader()
    ruleReader.getRules()

