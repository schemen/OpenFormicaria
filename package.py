#!/usr/bin/python
from zipfile import ZipFile
import os
from os.path import split

EXPORT = "package/"

if not os.path.exists(EXPORT):
    os.makedirs(EXPORT)


# Connectors
with ZipFile(EXPORT + "connectors.zip", 'w') as zipObj:
    dir = "Connectors/STL/"
    zipObj.write("LICENSE")
   # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk("docs/"):
        for filename in filenames:
            if filename != "CNAME":
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, filePath)
    for folderName, subfolders, filenames in os.walk(dir):
        for filename in filenames:
            #create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            safename = filePath.replace(dir, "")
            # Add file to zip
            zipObj.write(filePath, safename)

# Modules
with ZipFile(EXPORT + "modules.zip", 'w') as zipObj:
    dir = "Modules/STL/"
    zipObj.write("LICENSE")
   # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk("docs/"):
        for filename in filenames:
            if filename != "CNAME":
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, filePath)
    for folderName, subfolders, filenames in os.walk(dir):
        for filename in filenames:
            #create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            safename = filePath.replace(dir, "")
            # Add file to zip
            zipObj.write(filePath, safename)

# Formicaria
with ZipFile(EXPORT + "formicaria.zip", 'w') as zipObj:
    dir = "Formicaria/STL/"
    zipObj.write("LICENSE")
   # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk("docs/"):
        for filename in filenames:
            if filename != "CNAME":
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath, filePath)
    for folderName, subfolders, filenames in os.walk(dir):
        for filename in filenames:
            #create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            safename = filePath.replace(dir, "")
            # Add file to zip
            zipObj.write(filePath, safename)
    for folderName, subfolders, filenames in os.walk("Formicaria/Inserts/"):
        for filename in filenames:
            #create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            safename = filePath.replace("Formicaria/", "")
            # Add file to zip
            zipObj.write(filePath, safename)