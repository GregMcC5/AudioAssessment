import metadata_utils as mu
from bs4 import BeautifulSoup

# for doc in xml_docs:

print("souping")
soup_file = open("mets.xml")
soup = BeautifulSoup(soup_file, features="xml")
print("done souping\n-----------")


# -processHistoy
ph_tag_list = []

ph_pe = soup.find("ph:processHistory")
print("len of ph:", len(ph_pe))
print(ph_pe.name)
print(ph_pe.descendants)
for item in ph_pe.descendants:
    if item.name is not None and item.is_empty_element is not True:
        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
        ph_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")

ph_tag_counts = [["tag", "package count", "total count"]]

for tag in ph_tag_list:
    print(tag)
    if tag in [x[0] for x in ph_tag_counts]:
        [x for x in ph_tag_counts if x[0] == tag][0][2] += 1
    else:
        ph_tag_counts.append([tag, 1, 1])

# -audioObject
ao_tag_list = []

ao = soup.find("aes:audioObject")
for item in ao.descendants:
    if item.name is not None and item.is_empty_element is not True:
        print('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")
        ao_tag_list.append('/'.join([parent.name for parent in item.find_parents()][::-1]) + f"/{item.name}")

ao_tag_counts = [["tag", "package count", "total count"]]

for tag in ao_tag_list:
    if tag in [x[0] for x in ao_tag_counts]:
        [x for x in ao_tag_counts if x[0] == tag][0][2] += 1
    else:
        ao_tag_counts.append([tag, 1, 1])

# -Writing documetns
mu.write_csv("ph_tag_tabulation.csv", ph_tag_counts)
mu.write_csv("ao_tag_tabulation.csv", ao_tag_counts)

print("done")