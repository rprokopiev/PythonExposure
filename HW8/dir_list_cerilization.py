import json
import csv
import pickle


def to_json(json_file: str, dir_list: list):
    with open(json_file, 'w', encoding='UTF-8') as j_file:
        json.dump(dir_list, j_file, indent=4, ensure_ascii=False)


def to_csv(csv_file: str, dir_list: list):
    with open(csv_file, 'w', encoding='UTF-8') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerows(dir_list)


def to_bytefile(byte_file: str, dir_list: list):
    with open(byte_file, 'wb') as b_file:
        pickle.dump(dir_list, b_file)