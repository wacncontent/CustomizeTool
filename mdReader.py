#!/usr/bin/env python
# coding: GBK
# Date  : 2015/09/03
# Version: 0.1
__author__ = 'Steven'

class MdReader:
    def __init__(self):
        self.mdList = []

    # Function to get markdown file list
    def getMdList(self):
        MD_FILE = "mdFile.md"

        try:
            with open(MD_FILE, "r") as fMd:
                for line in fMd:
                    trimedLine = line.strip()
                    if trimedLine == '':
                        continue
                    # add file name to our markdown file list
                    self.mdList.append(trimedLine)

                # print(self.mdList)
                print('\033[1;32m Finish reading markdown files list, keep moving...\033[0m\n')
                return self.mdList
        except IOError as e:
            print('\033[1;31m Can not find mdFile.md \033[0m\n')

if '__main__' == __name__:
    mdReader = MdReader()
    mdReader.getMdList()
