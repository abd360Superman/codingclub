from tkinter import *
import shutil
import os
from send2trash import send2trash

def new_file():
    print("location for new file")
    path = input()
    if not os.path.exists(path):
        print("Invalid location")
        return
    print('Enter new name for file')
    name = input()
    print('Enter the file type')
    ftype = input()
    final_path = os.path.join(path, name+'.'+ftype)
    with open(final_path, 'w') as fp:
        pass
    print("File created!")

def open_file():
    print("file to open")
    string = input()
    try:
        os.startfile(string)
    except:
        mprint("File not found!")

def copy_file():
    print("Enter file to copy")
    source = input()
    if not os.path.exists(source):
        print("Invalid file")
        return
    print("Enter folder for copied file")
    destination = input()
    if not os.path.exists(destination):
        print("Invalid folder")
        return
    shutil.copy(source, destination)
    print("File copied!")

def delete_file():
    print("Choose file to permanentley delete")
    del_file = input()
    if os.path.exists(del_file):
        os.remove(del_file)
        print("File deleted")
    else:
        print("File not found")

def send_file_to_trash():
    print("Choose file to send to trash")
    send = input()
    if os.path.exists(send):
        send2trash(send)
        print("File sent to trash")
    else:
        print("File not found")

def rename_file():
    print("Choose file to rename")
    chosen_file = input()
    if not os.path.exists(chosen_file):
        print("File not found")
        return
    old_path = os.path.dirname(chosen_file)
    extension = os.path.splitext(chosen_file)[1]
    print('Enter new file name')
    newname = input()
    path = os.path.join(old_path, newname+extension)
    os.rename(chosen_file, path)
    print("File renamed")

def move_file():
    print("Choose file to move")
    source = input()
    if not os.path.exists(source):
        print("File not found")
        return
    print("Choose new destination")
    destination = input()
    shutil.move(source, destination)
    mb.showinfo('confirmation', 'File moved!')

def file_size():
    print("Enter file to get it's size")
    file = input()
    if not os.path.exists(file):
        print("File not found")
        return
    print(os.path.getsize(file))

def list_file_with_specific_path():
    print("Enter folder")
    p = input()
    if not os.path.exists(p):
        print("File not found")
        return
    print('Enter file type')
    ftype = input()
    for folderName, subfolders, filenames in os.walk(p):
        print('Current folder: ' + folderName)

        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)

        for filename in filenames:
            if filename.endswith(ftype):
                print('File inside ' + folderName + ': ' + filename)

        print('')

def new_folder():
    print("Enter location for new folder")
    location = input()
    print('Enter name for the folder')
    name = input()
    path = os.path.join(location, name)
    os.mkdir(path)
    print("Folder made")

def delete_folder():
    print('Choose folder to permanently delete')
    delFolder = input()
    if os.path.exists(delFolder):
        shutil.rmtree(delFolder)
        print('Folder Deleted!')
    else:
        print("Folder not found")

def rename_folder():
    print('Choose folder to rename')
    refolder = input()
    if not os.path.exists(refolder):
        print("Invalid folder")
        return
    location = os.path.dirname(refolder)
    print('Enter new name for folder')
    nname = input()
    path = os.path.join(location, nname)
    os.rename(refolder, path)
    print('Folder Renamed!')

def list_files():
    print('Choose Folder')
    folder_list = input()
    if not os.path.exists(folder_list):
        print("Invalid folder name")
        return
    for folderName, subfolders, filenames in os.walk(folder_list):
        print('Current folder: ' + folderName)

        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('File inside ' + folderName + ': ' + filename)

        print('')

def move_folder():
    print('Choose folder to move')
    folder = input()
    if not os.path.exists(folder):
        print("Folder not found")
        return
    print('Choose new location for folder')
    nlocation = input()
    if not os.path.exists(nlocation):
        print("Folder not found")
        return
    if folder == nlocation:
        print('The Folder and Location are same!')
    else:
        shutil.move(folder, nlocation)
        print('Folder Moved!')

def copy_folder():
    print('Choose folder to copy')
    source = input()
    if not os.path.exists(source):
        print("Invalid folder")
        return
    print('Choose destination for copied folder')
    destination = input()
    if not os.path.exists(destination):
        print("Folder not found")
        return
    print('Enter name for copied folder')
    nname = input()
    fdestinataion = os.path.join(destination, nname)
    shutil.copytree(source, fdestinataion)
    print('Folder Copied!')

def folder_size():
    print('Choose Folder')
    folder = input()
    if not os.path.exists(folder):
        print("Invalid folder")
        return
    totalsize = 0
    for filename in os.listdir(folder):
        totalsize = totalsize + os.path.getsize(os.path.join(folder, filename))
    print(totalsize)

tk = Tk()
tk.geometry('470x295')
tk.title(' ')
tk.resizable(0, 0)
tk.update()
Label(tk, text='Filesh Exploresh', font=('Helvetica', 16), fg='blue').grid(row=5, column=2)

Button(tk, text='New File', command=new_file).grid(row=15, column=2)
Button(tk, text='Open File', command=open_file).grid(row=25, column=2)
Button(tk, text='Rename File', command=rename_file).grid(row=35, column=2)
Button(tk, text='Delete File', command=delete_file).grid(row=45, column=2)
Button(tk, text='Send File To Trash', command=send_file_to_trash).grid(row=55, column=2)
Button(tk, text='Move File', command=move_file).grid(row=65, column=2)
Button(tk, text='Copy File', command=copy_file).grid(row=75, column=2)
Button(tk, text='Get File Size', command=file_size).grid(row=85, column=2)

Button(tk, text='List All Files With Particular Format In Directory', command=list_file_with_specific_path).place(x = 20, y=265, anchor=NW)

Button(tk, text='New Folder', command=new_folder).grid(row=15, column=4)
Button(tk, text='List All Files And Paths in  ', command=list_files).grid(row=25, column=4)
Button(tk, text='directory tree(same as above)', command=list_files).grid(row=35, column=4)
Button(tk, text='Rename Folder', command=rename_folder).grid(row=45, column=4)
Button(tk, text='Delete Folder', command=delete_folder).grid(row=55, column=4)
Button(tk, text='Move Folder', command=move_folder).grid(row=65, column=4)
Button(tk, text='Copy Folder', command=copy_folder).grid(row=75, column=4)
Button(tk, text='Get Folder Size', command=folder_size).grid(row=85, column=4)

tk.mainloop()
