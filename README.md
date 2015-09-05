**CustomizeTool** is a text process tool (replace , delete) **based on your own rules**.

## Support for
+ Self defined rules and file list
+ Regex support
+ Comment support
+ GBK support
+ Ignore rule Support

## How to use
1. Define your own rules in **rules.md**, prepare your file list in *mdFile.md*
2. run the script: `python core.py`, and the result file will be named *YOUR_FILE_NAME.bak*

## Configuration your own 'rules.md' (Important)
Here is the example of self defined rules:
```
  # Line starts with '#' is comment
  # Rules under [CONST] label will be treated as constant string,
  # until it reaches [REGEX] label which supports regex format
  [CONST]
  # Original string and replacing string is splitted with '='
  windows.net=chinacloudapi.cn
  # You can put spaces around '=' for beauty format
  http://msdn.microsoft.com/en-us/library/azure/  =  http://msdn.microsoft.com/zh-cn/library/azure/
  # If you want to delete some string, just put 'DELETE' at right position
  Azure.select = DELETE
  # If you want ignore some certain rules, just put '???' at right position
  http://myapps.microsoft.com = ???
  
  # Rules under [REGEX] label will be treated as regular expression
  [REGEX]
  # [link text](xxx-xxx-xxx.md) → [link text](/documentation/articles/xxx-xxx-xxx)
  (\[.*?\]\()(.*?)(\.md)(\)) = \1/documentation/articles/\2\4
  
  # [link text](/zh-cn/documentation/articles/xxx-xxx-xxx) → [link text](/documentation/articles/xxx-xxx-xxx)
  (\[.*?\]\()(\/zh-cn)(\/documentation\/articles\/.*?\)) = \1\3
```
## Configuration for 'mdFile.md'
This is very simple, just put file's **absolute path** or **relative path** in mdfile.md
Here is a example:
```
  D:/Mooncake/test/active-directory-aadconnect-account-summary.md
  test/keyword_test.md
```
## ISSUE
+ Problem with message's color when shown in **windows cmd**
+ I have tested two cases, one if *keyword test* and another is *normal text test*, but it still need more TEST

## TODO
+ Simplify **mdFile.md** rules, maybe we can use a variable to indicate our *working direcotry* or just pass a parameter
when running our script, just like `python core.py wd=C:\Documents\`
