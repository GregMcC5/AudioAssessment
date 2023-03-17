import metadata_utils as mu
import zipfile as zf
from bs4 import BeautifulSoup
import os

ph_tag_list = []
ao_tag_list = []

#navigate to external drive
print(os.getcwd())
os.chdir("/Volumes/Backup/Audio Assessment")
os.system("ls")

#access, unzip, and soup each directory
for package in os.listdir():
    folder = package.strip(".zip")
    print(package)
    try:
        with zf.ZipFile(package, 'r') as zip_file:
            file_info = zip_file.getinfo(f'data/mets.xml')
            with zip_file.open(file_info) as file:
                xml_file = file.read()
                soup = BeautifulSoup(xml_file, 'xml')
                print(f"souped - {package}")

                # -processHistoy
                ph_pe = soup.find("ph:processHistory")
                print("len of ph:", len(ph_pe))
                print(ph_pe.name)
                print(ph_pe.descendants)
                for item in ph_pe.descendants:
                    if item.name is not None and item.is_empty_element is not True:
                        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
                        ph_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")

                # -audioObject
                ao = soup.find("aes:audioObject")
                for item in ao.descendants:
                    if item.name is not None and item.is_empty_element is not True:
                        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
                        ao_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
    except:
        continue

# -tabulating proceessHistory tags
ph_tag_counts = [["tag", "package count", "total count"]]

for tag in ph_tag_list:
    print(tag)
    if tag in [x[0] for x in ph_tag_counts]:
        [x for x in ph_tag_counts if x[0] == tag][0][2] += 1
    else:
        ph_tag_counts.append([tag, 1, 1])


# -tabulating proceessHistory tags
ao_tag_counts = [["tag", "package count", "total count"]]

for tag in ao_tag_list:
    if tag in [x[0] for x in ao_tag_counts]:
        [x for x in ao_tag_counts if x[0] == tag][0][2] += 1
    else:
        ao_tag_counts.append([tag, 1, 1])


# -Writing documents
os.chdir("/Users/gregorymccollum/Documents/GitHub/AudioAssessment")

mu.write_csv("ph_tag_tabulation.csv", ph_tag_counts)
mu.write_csv("ao_tag_tabulation.csv", ao_tag_counts)

print("done")