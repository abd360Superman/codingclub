## PLEASE PLEASE PLEASE Do this code in your own developing environment while viewing this file


#importing os and shutil
import os
import shutil
# Helps in making a type of file explorer

"""
#Opening File
os.startfile('test.docx')

# Files exists
print(os.path.exists('test.docx'))
print(os.path.exists('test.png'))

#File Size
if os.path.exists('test.xlsx'):
    print('xlsx')
    print(os.path.getsize('test.xlsx'))
else:
    print('xls')
    print(os.path.getsize('test.xls')) 

#Copy File
shutil.copy('test.txt', 'test')

#Move File
shutil.move('test.pptx', 'test')

#Delete File
# PLEASENOTE - by running this command, the file is removed FOREVER. 
# NEXT Time, I'll teach how to send files to trash
os.remove('test.xlsx')

#Get current directory and joins the path
print(os.path.join(os.getcwd(), 'test'))

#DIRNAME
print(os.path.dirname(os.getcwd()))
print(os.path.dirname(os.path.join(os.getcwd(), 'test.txt')))

#Get File Extension
print(os.path.splitext('test.docx')[1])

#Rename Files
fpath = os.path.join(os.getcwd(), 'test.txt')
maindir = os.path.dirname(fpath)
ext = os.path.splitext(fpath)[1]
newFilename = 'teest'

finalPath = os.path.join(maindir, newFilename+ext)
os.rename(fpath, finalPath)

#Create Folder
os.mkdir('test_by_py')

#Change Directory
os.chdir('test')
print(os.getcwd())

#LISTDIR
print(os.listdir('test'))

#Folder Size
totalsize = 0
for filename in os.listdir(): #No parameter means current directory
    totalsize += os.path.getsize(filename)
print(totalsize)

# Delete Folder
# This deletes folder FOREVER
shutil.rmtree('test_by_py')

# MOVE FOLDER
orgFolder = os.path.join(os.getcwd(), 'test')
foldToMove = os.path.join(os.getcwd(), 'test_by_py')
shutil.move(foldToMove, orgFolder)

# Copy Folder
foldToCopy = os.path.join(os.getcwd(), 'test_by_py')
copyDest = os.path.join(os.getcwd(), 'test')

#Copying a folder needs to give the folder a new name
finalCopyDest = os.path.join(copyDest, 'teste')

shutil.copytree(foldToCopy, finalCopyDest)
"""

#Rename Folder
foldToRename = os.path.join(os.getcwd(), 'test_by_py')
locationOfFolderToRename = os.path.dirname(foldToRename)
npath = os.path.join(locationOfFolderToRename, 'test_py')
os.rename(foldToRename, npath)