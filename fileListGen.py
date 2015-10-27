import glob

global_article_path = "C:/Users/Administrator/Documents/GitHub/azure-content-pr"

service_folders = []

def genFileList(fileName):
    output = open(fileName, 'w')
    for folder in service_folders:
        fileList = glob.glob(global_article_path+"/articles/"+folder+"/*.md")
        for file in fileList:
            output.writelines(file+"\n")
    fileList = glob.glob(global_article_path+"/includes/*.md")
    for file in fileList:
        output.writelines(file+"\n")
    output.close()
