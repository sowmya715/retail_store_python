"""
Problem Statement:
Write a Python program that reads a grade file (grades.txt) containing
assignment maximum points and student scores. Using this data, the program
should analyze and report:

1. How many assignments exist in the file.
2. The total number of available points for all assignments.
3. How many students are listed in the grade file.
4. Which student scored the highest overall total.
5. Which student scored the lowest overall total.
6. Which students are missing one or more grades.
7. Identify any grades that are invalid:
      - A grade higher than the assignment's maximum score
      - A negative grade
      - (Zero is allowed)

File Format:
- The first row of the file contains assignment maximum scores.
- Each following row contains a student number followed by their grades.
- Values are separated by TAB characters (\t).

Example:
00000000    10  20  15  25
12345678    9   18  15  20
11223344    10      12  25   <-- Missing grade
...

Your program must:
- Read the data
- Structure it into dictionaries/lists
- Perform calculations
- Print all required outputs clearly
"""

header_key="00000000"
def dataReading(file):
    with open("grades.txt") as file_reader:
        file_grades=file_reader.readlines()
    return file_grades
def slice(lst, start, end):
    output=list()
    for i in range(start, end):
        output.append(lst[i].strip())
    return output
def structrizeTheData(file_grades):
    final_dictionary=dict()
    for assignment_data in file_grades:
        assign=assignment_data.split("\t")
        for single_assingment in range(len(assign)):
            final_dictionary[assign[0]]=slice(assign,1,len(assign))
    return final_dictionary

data_read=dataReading("grades.txt")
structred_data=structrizeTheData(data_read)
print("How many assignments? :-",len(structred_data.get(header_key)),"\n")

total_points=0
for each_point in structred_data.get(header_key):
    total_points+=int(each_point)
print("What is the total number of available points? :-",total_points,"\n")

print("How many students were in the grade file? :-",len(structred_data.keys())-1,"\n")
index=0
structred_data_keys=list(structred_data.keys())
maximum_grades,maximum_grades_user,lowest_grades,lowest_grades_users=int(),str(),int(),str()
while index<len(structred_data_keys):
    grades=int()
    if structred_data_keys[index]==header_key:
        index+=1
        continue
    for each_grade in structred_data[structred_data_keys[index]]:
        if each_grade=="":
            each_grade=0
        else:
            each_grade=int(each_grade)
        grades+=each_grade
    if grades>maximum_grades:
        maximum_grades=grades
        maximum_grades_user=structred_data_keys[index]
    if index==1:
        lowest_grades=grades
        lowest_grades_users=structred_data_keys[index]
    else:
        if grades<lowest_grades:
            lowest_grades=grades
            lowest_grades_users=structred_data_keys[index]
    index+=1
    
print("Which student number scored the highest overall? :-",maximum_grades_user,maximum_grades,"\n")

print("Which student number scored the lowest overall? :-",lowest_grades_users,lowest_grades,"\n")

print("Which students are missing grades? :- ")
for key,value in structred_data.items():
    found=None
    for assigment in value:
        if assigment=="":
            found=True
    if found:
        print(key)

print("Identify any situation in which a student has a recorded grade that is either too high (higher than the maximum available for an assignment) or too low (a negative number). A zero is allowed.")
for key,value in structred_data.items():
    if key==header_key:
        continue
    for value_2 in range(len(structred_data.get(header_key))):
        if isinstance(value[value_2],str) and value[value_2]=="":
            value[value_2]=0
        value[value_2]=int(value[value_2])
        if value[value_2]>int(structred_data.get(header_key)[value_2]):
            print("too high",key)
        if value[value_2]<0:
            print("too low",key)
print()

