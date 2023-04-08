# SI 581 Final Project (Winter 2023)

Gregory McCollum, Shelby Jeffrey, Emma Heck
Last Updated: April 8th, 2023

## Introduction
This repository contains the scripts and resulting files associated with the three authors final project for the SI581 course from the University of Michigan School of Information's SI581 course from the 2023 Winter semester.

Our project was a collaboration with the University of Michigan Library's Digital Preservation Unit. Specifically, our project analyze the metadata resulting from the DPU's audio digitizaiton program. The DPU's digitized audio packages include METS metadata files. Within these METS files two additional schemes: AES-X098-B ("AudioObject") and AES-X098-C ("ProcessHistory"). These two standards, developed by the Audio Engineers Society, were of most interest to DPU staff.

Becuase DPU's metadata files come from a third-party vendor and DPU is uncertain as to how this vendor has implemented these two standards. Our project soughts to reveal how these two schemes are being implemented. To do so, we performed an analysis of a sampling of 65 of the DPU's digtized audio packages and recorded what XML tags (with full Xpath) are used in the AudioObject and ProcessHistory schemes, how many packages they appear in, the average number of times it appears in a packagae, the maxmimum and minimum number of times it appears in any package.

Our intention is to enable the DPU to have better control over their metadata and to be able to access with greater efficency the content recorded in their metadata

## Inventory

 - **README.md** - This document.
 - **METS_tag_extraction.py** - The script which accesses and performs our calculations on the METS files. This script accesses the packages, finds all the tags with both scheme's perfixes and tabulates them per package before aggregating their stats across all packages. It then writes the calculated tabulations to the "ao_tag_tabulation.csv" and the "ph_tag_tabulation.csv" files.
 - **metadata_utils.py** - A utility document used to store functions necessary to read and write CSVs. Referred to by METS_tag_extraction.py.
- **"ao_tag_tabulation.csv"** - This file contains the tabulations for all tags from the AES-X098-B scheme. It provides the xpath for each scheme tag, the number of packages the tag appears in, an average number of times the tag appears per package, the mnimum number of times it appears in a package and the maxmimum number of times is appear in a packages.
- **"ph_tag_tabulation.csv"** - This file contains the tabulations for all tags from the AES-X098-c scheme. It provides the xpath for each scheme tag, the number of packages the tag appears in, an average number of times the tag appears per package, the mnimum number of times it appears in a package and the maxmimum number of times is appear in a packages.

## Contact
For more information, please contact Gregory McCollum at gregmcc@umich.edu. More details on this project are available in our final report.