import csv
import json
import os

#--------------------------------------------
#use with csvs

def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data

def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)

#--------------------------------------------
#use with jsons

def read_json(filepath, encoding='utf-8'):
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

#--------------------------------------------
#use for any

def read_file(filepath):
  # check extension
  _, extension = os.path.splitext(filepath)

  # if CSV
  if extension == ".csv":
    with open(filepath, "r") as file:
      reader = csv.reader(file)
      data = [row for row in reader]

  # if JSON
  elif extension == ".json":
    with open(filepath, "r") as file:
      data = json.load(file)

  return data

