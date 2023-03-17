import os
import os.path
import zipfile as zf
from bs4 import BeautifulSoup


# Open the zip file in read mode
with zf.ZipFile('39015083611809.zip', 'r') as zip_file:

    # Get information about the file you want to access
    file_info = zip_file.getinfo('39015083611809/marc.xml')

    # Open the file using the file name and the 'open' method of the zip file object
    with zip_file.open(file_info) as file:
        # Do something with the file
        xml_file = file.read()
        soup = BeautifulSoup(xml_file, 'xml')
        print("souped!")

print("done")