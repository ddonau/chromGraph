import os

files = []
folders = []
path = r'C:\Users\damien\Documents\Melbourne\WORK\files'
for (path, dirnames, filenames) in os.walk(path):
    folders.extend(os.path.join(path, name) for name in dirnames)
    files.extend(os.path.join(path, name) for name in filenames)

#print(files)
print(folders)