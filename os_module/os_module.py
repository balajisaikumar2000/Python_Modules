import os

#get the current working directory
print(os.getcwd())

#Change current working Directory
os.chdir("C:/ANY_PATH")

#Delete Any Directory
os.rmdir("Desktop_News_Notifier")       #you have to mention the full directory path

#Create New Directory
os.mkdir("NEWFOLDER")

#Rename Any Directory
os.rename("NEWFOLDER","MYFOLDER")
