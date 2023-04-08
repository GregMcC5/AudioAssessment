import metadata_utils as mu
import zipfile as zf
from bs4 import BeautifulSoup
import os

#--initialize aggregator--
ph_tag_aggregator = [["tag", "package count", "average occurences per package", "min", "max"]]
ao_tag_aggregator = [["tag", "package count", "average occurrence per package", "min", "max"]]

#--navigate to external drive--
print(os.getcwd())
os.chdir("/Volumes/Backup/Audio Assessment")
os.system("ls")

#--access, unzip, and soup each directory--
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
                ph_tag_list = []
                ph_pe = soup.find("ph:processHistory")
                print("len of ph:", len(ph_pe))
                for item in ph_pe.find_all(True):
                        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
                        ph_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")

                ph_tag_counts = [["tag", "package count", "total count"]]
                for tag in ph_tag_list:
                    print(tag)
                    if tag in [x[0] for x in ph_tag_counts]:
                        [x for x in ph_tag_counts if x[0] == tag][0][2] += 1
                    else:
                        ph_tag_counts.append([tag, 1, 1])

                for entry in ph_tag_counts[1:]:
                    if entry[0] in [x[0] for x in ph_tag_aggregator[1:]]:
                        #-presence in record
                        [x for x in ph_tag_aggregator if x[0] == entry[0]][0][1] += 1
                        #total count
                        [x for x in ph_tag_aggregator if x[0] == entry[0]][0][2] += entry[2]
                        #-minimum
                        if entry[2] < [x for x in ph_tag_aggregator if x[0] == entry[0]][0][3]:
                            [x for x in ph_tag_aggregator if x[0] == entry[0]][0][3] = entry[2]
                        #-maximum
                        if entry[2] > [x for x in ph_tag_aggregator if x[0] == entry[0]][0][4]:
                            [x for x in ph_tag_aggregator if x[0] == entry[0]][0][4] = entry[2]

                    else:
                        ph_tag_aggregator.append(entry + [entry[2], entry[2]])

                # -audioObject
                ao_tag_list = []
                ao = soup.find("aes:audioObject")
                for item in ao.find_all(True):
                        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
                        ao_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")

                ao_tag_counts = [["tag", "package count", "total count"]]
                for tag in ao_tag_list:
                    print(tag)
                    if tag in [x[0] for x in ao_tag_counts]:
                        [x for x in ao_tag_counts if x[0] == tag][0][2] += 1
                    else:
                        ao_tag_counts.append([tag, 1, 1])

                for entry in ao_tag_counts[1:]:
                    if entry[0] in [x[0] for x in ao_tag_aggregator[1:]]:
                       #-presence in record
                        [x for x in ao_tag_aggregator if x[0] == entry[0]][0][1] += 1
                        #-total count
                        [x for x in ao_tag_aggregator if x[0] == entry[0]][0][2] += entry[2]
                        #-minimum
                        if entry[2] < [x for x in ao_tag_aggregator if x[0] == entry[0]][0][3]:
                            [x for x in ao_tag_aggregator if x[0] == entry[0]][0][3] = entry[2]
                        #-maximum
                        if entry[2] > [x for x in ao_tag_aggregator if x[0] == entry[0]][0][4]:
                            [x for x in ao_tag_aggregator if x[0] == entry[0]][0][4] = entry[2]

                    else:
                        ao_tag_aggregator.append(entry + [entry[2], entry[2]])
    except:
        continue

#--divide per--
for list in [ph_tag_aggregator, ao_tag_aggregator]:
    for entry in list[1:]:
        entry[2] = round(entry[2]/65, 1)

#--Writing documents--
os.chdir("/Users/gregorymccollum/Documents/GitHub/AudioAssessment")

mu.write_csv("ph_tag_tabulation.csv", ph_tag_aggregator)
mu.write_csv("ao_tag_tabulation.csv", ao_tag_aggregator)

print("done")