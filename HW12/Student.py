import csv


class Student:


    def __init__(self, name, file_csv):
        self.name = name
        self.subjects = load_subjects(file_csv)


    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for line in csv_file:
                for i in line:
                    self.subjects.setdefault(i)

    def add_grade(self, subject, grade):
        self.subjects[subject] = grade

# s = Student('Kjsadf')
# print(s.subjects)




def load_subjects(subjects_file):
    subjects = {}
    with open(subjects_file, 'r', newline='', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        grade = []
        test_score = []
        for line in csv_file:
            for i in line:
                subjects[i] = grade, test_score
    return subjects

mydict = load_subjects('subjects.csv')

print(mydict)
# for key in mydict.keys():
#     print(item)
    # mydict[key][1].append('a')

for key, value in mydict.items():
    print(f'{key} - {value}')
    value[1].append(1)

print(mydict)