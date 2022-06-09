# Zipfile Module
import zipfile

# Open and List
zipped_file = zipfile.ZipFile("Archive.zip", "r")
print(zipped_file.namelist())

# Metadata in the zip folder
for meta in zipped_file.infolist():
    print(meta)

info = zipped_file.getinfo("purchased.txt")
print(info)

# Access to files in zip folder
print(zipped_file.read("wishlist.txt"))
with zipped_file.open("wishlist.txt") as f:
    print(f.read())

# Extracting files
# zipped_file.extract("purchased.txt")
zipped_file.extractall()

# Closing the zip
zipped_file.close()
