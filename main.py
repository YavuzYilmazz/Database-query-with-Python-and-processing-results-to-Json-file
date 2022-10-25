# Yavuz_Yilmaz_2019510086
# Fatih_Varol_2019510081

import csv
import operator
import json


def Ordering(Dictionary, Order):     #sorting part
    if Order == 'ASC':
        dictionary_items = Dictionary.items()
        sorted_items = sorted(dictionary_items)
        return sorted_items
    elif Order == 'DSC':
        dictionary_items = Dictionary.items()
        sorted_items = sorted(dictionary_items, key=operator.itemgetter(0), reverse=True)
        return sorted_items


def JSON(Dictionary, Col_name, Col_name2, index):       #Create and Write json file
    NewDict1 = {}
    file_name = 'Students' + str(index) + '.json'
    Dictionary = dict(Dictionary)
    if Col_name == None and Col_name2 == None:
        for key, value in Dictionary.copy().items():
            NewDict1[key] = ["name: " + value[0], "lastname: " + value[1], "email: " + value[2], "grade: " + value[3]]
        with open(file_name, 'w') as json_file:
            json.dump(NewDict1, json_file)
    elif Col_name != None and Col_name2 == None:
        if Column_control(Col_name) == 5:
            Wrong_input()
        else:
            for key, value in Dictionary.copy().items():
                NewDict1[key] = [Col_name + ": " + value[Column_control(Col_name) - 1]]
            with open(file_name, 'w') as json_file:
                json.dump(NewDict1, json_file)
    elif Col_name2 != None:
        if Column_control(Col_name2) == 5:
            Wrong_input()
        else:
            for key, value in Dictionary.copy().items():
                NewDict1[key] = [Col_name + ": " + value[Column_control(Col_name) - 1],
                                 Col_name2 + ": " + value[Column_control(Col_name2) - 1]]
            with open(file_name, 'w') as json_file:
                json.dump(NewDict1, json_file)


def Select1(Word, Punc, Data, Dictionary): #The select operation used unless the and condition exists
    Data = Data.replace("’", "")          #removes those that do not fit the condition from the dictionary
    Data = Data.replace("‘", "")
    flag = True
    Dictionary = dict(Dictionary)
    if Word == 'name':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data != value[0]:
                    Dictionary.pop(key)

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data == value[0]:
                    Dictionary.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word == 'lastname':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data != value[1]:
                    Dictionary.pop(key)

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data == value[1]:
                    Dictionary.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word == 'email':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data != value[2]:
                    Dictionary.pop(key)

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data == value[2]:
                    Dictionary.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word == 'grade':
        if Punc == 2:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Dictionary.pop(key)

        elif Punc == 3:
            for key, value in Dictionary.copy().items():
                if int(Data) != int(value[3]):
                    Dictionary.pop(key)

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if int(Data) == int(value[3]):
                    Dictionary.pop(key)

        elif Punc == 1:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Dictionary.pop(key)

        elif Punc == 5:
            for key, value in Dictionary.copy().items():
                if int(value[3]) > int(Data):
                    Dictionary.pop(key)

        elif Punc == 6:
            for key, value in Dictionary.copy().items():
                if int(value[3]) < int(Data):
                    Dictionary.pop(key)

        elif Punc == 7:
            for key, value in Dictionary.copy().items():
                if int(value[3]) < int(Data):
                    Dictionary.pop(key)

        elif Punc == 8:
            for key, value in Dictionary.copy().items():
                if int(value[3]) > int(Data):
                    Dictionary.pop(key)

        else:
            flag = False
            Wrong_input()
    else:
        flag = False
        Wrong_input()

    if flag:
        return Dictionary


def Select_and1(Word, Punc, Data, Word2, Punc2, Data2, Dictionary): #select operation used only when and condition exists
    flag = True #it first assigns the first condition to a new dictionary, then checks this dictionary for the second condition and returns
    Newdict = {}
    Dictionary = dict(Dictionary)
    Data = Data.replace("’", "")
    Data = Data.replace("‘", "")
    if Word == 'name':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[0]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[0]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'lastname':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[1]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[1]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'email':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[2]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[2]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'grade':
        if Punc == 2:
            for key, value in Dictionary.copy().items():
                if int(value[3]) > int(Data):
                    Newdict[key] = value
        elif Punc == 3:
            for key, value in Dictionary.copy().items():
                if int(Data) == int(value[3]):
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if int(Data) != int(value[3]):
                    Newdict[key] = value
        elif Punc == 1:
            for key, value in Dictionary.copy().items():
                if int(value[3]) < int(Data):
                    Newdict[key] = value
        elif Punc == 5:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Newdict[key] = value
        elif Punc == 6:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Newdict[key] = value

        elif Punc == 7:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Newdict[key] = value

        elif Punc == 8:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Newdict[key] = value
        else:
            flag = False
            Wrong_input()
    else:
        flag = False
        Wrong_input()

    Data2 = Data2.replace("’", "")
    Data2 = Data2.replace("‘", "")
    if Word2 == 'name':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[0]:
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[0]:
                    Newdict.pop(key)
        else:
            flag = False
            Wrong_input()
    elif Word2 == 'lastname':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[1]:
                    Newdict.pop(key)

            return Dictionary
        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[1]:
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word2 == 'email':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[2]:
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[2]:
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word2 == 'grade':
        if Punc2 == 2:
            for key, value in Newdict.copy().items():
                if int(value[3]) <= int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 3:
            for key, value in Newdict.copy().items():
                if int(Data2) != int(value[3]):
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if int(Data2) == int(value[3]):
                    Newdict.pop(key)

        elif Punc2 == 1:
            for key, value in Newdict.copy().items():
                if int(value[3]) >= int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 5:
            for key, value in Newdict.copy().items():
                if int(value[3]) > int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 6:
            for key, value in Newdict.copy().items():
                if int(value[3]) < int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 7:
            for key, value in Newdict.copy().items():
                if int(value[3]) < int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 8:
            for key, value in Newdict.copy().items():
                if int(value[3]) > int(Data2):
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    else:
        flag = False
        Wrong_input()

    if flag:
        return Newdict


def Insert(id, name, surname, mail, grade, Dictionary): #insertion method
    if id.isnumeric() == True and grade.isnumeric() == True and int(grade) <= 100 and int(grade)>=0:
        id = int(id)
        Dictionary[id] = [name, surname, mail, grade]
        return Dictionary
    else:
        Wrong_input()


def Delete(Word, Punc, Data, Dictionary):#The select operation used unless the and condition exists
    Data = Data.replace("’", "")        #removes those matching the delete condition from the dictionary
    Data = Data.replace("‘", "")
    Dictionary = dict(Dictionary)
    if Word == 'name':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[0]:
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[0]:
                    Dictionary.pop(key)

            return Dictionary
        else:
            Wrong_input()
    elif Word == 'lastname':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[1]:
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[1]:
                    Dictionary.pop(key)

            return Dictionary
        else:
            Wrong_input()
    elif Word == 'email':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[2]:
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[2]:
                    Dictionary.pop(key)

            return Dictionary
        else:
            Wrong_input()
    elif Word == 'grade':
        if Punc == 2:
            for key, value in Dictionary.copy().items():
                if int(value[3]) > int(Data):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 3:
            for key, value in Dictionary.copy().items():
                if int(Data) == int(value[3]):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if int(Data) != int(value[3]):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 1:
            for key, value in Dictionary.copy().items():
                if int(value[3]) < int(Data):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 5:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 6:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 7:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Dictionary.pop(key)

            return Dictionary
        elif Punc == 8:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Dictionary.pop(key)

            return Dictionary
        else:
            Wrong_input()
    else:
        Wrong_input()


def DeleteAnd(Word, Punc, Data, Word2, Punc2, Data2, Dictionary):#delete method used only for and condition
    flag = True #stores the ones that meet the first condition in a new dictionary.
    Newdict = {}# then it checks the second condition inside the dictionary. Finally, it extracts all the data in this dictionary from the original dictionary.
    Dictionary = dict(Dictionary)
    Data = Data.replace("’", "")
    Data = Data.replace("‘", "")
    if Word == 'name':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[0]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[0]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'lastname':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[1]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[1]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'email':
        if Punc == 3:
            for key, value in Dictionary.copy().items():
                if Data == value[2]:
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if Data != value[2]:
                    Newdict[key] = value

        else:
            flag = False
            Wrong_input()
    elif Word == 'grade':
        if Punc == 2:
            for key, value in Dictionary.copy().items():
                if int(value[3]) > int(Data):
                    Newdict[key] = value
        elif Punc == 3:
            for key, value in Dictionary.copy().items():
                if int(Data) == int(value[3]):
                    Newdict[key] = value

        elif Punc == 4:
            for key, value in Dictionary.copy().items():
                if int(Data) != int(value[3]):
                    Newdict[key] = value
        elif Punc == 1:
            for key, value in Dictionary.copy().items():
                if int(value[3]) < int(Data):
                    Newdict[key] = value
        elif Punc == 5:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Newdict[key] = value
        elif Punc == 6:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Newdict[key] = value

        elif Punc == 7:
            for key, value in Dictionary.copy().items():
                if int(value[3]) >= int(Data):
                    Newdict[key] = value

        elif Punc == 8:
            for key, value in Dictionary.copy().items():
                if int(value[3]) <= int(Data):
                    Newdict[key] = value
        else:
            flag = False
            Wrong_input()
    else:
        flag = False
        Wrong_input()

    Data2 = Data2.replace("’", "")
    Data2 = Data2.replace("‘", "")
    if Word2 == 'name':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[0]:
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[0]:
                    Newdict.pop(key)
        else:
            flag = False
            Wrong_input()
    elif Word2 == 'lastname':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[1]:
                    Newdict.pop(key)

            return Dictionary
        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[1]:
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word2 == 'email':
        if Punc2 == 3:
            for key, value in Newdict.copy().items():
                if Data2 != value[2]:
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if Data2 == value[2]:
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    elif Word2 == 'grade':
        if Punc2 == 2:
            for key, value in Newdict.copy().items():
                if int(value[3]) <= int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 3:
            for key, value in Newdict.copy().items():
                if int(Data2) != int(value[3]):
                    Newdict.pop(key)

        elif Punc2 == 4:
            for key, value in Newdict.copy().items():
                if int(Data2) == int(value[3]):
                    Newdict.pop(key)

        elif Punc2 == 1:
            for key, value in Newdict.copy().items():
                if int(value[3]) >= int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 5:
            for key, value in Newdict.copy().items():
                if int(value[3]) > int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 6:
            for key, value in Newdict.copy().items():
                if int(value[3]) < int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 7:
            for key, value in Newdict.copy().items():
                if int(value[3]) < int(Data2):
                    Newdict.pop(key)

        elif Punc2 == 8:
            for key, value in Newdict.copy().items():
                if int(value[3]) > int(Data2):
                    Newdict.pop(key)

        else:
            flag = False
            Wrong_input()
    else:
        flag = False
        Wrong_input()

    if flag:
        for key in Newdict.keys():
            Dictionary.pop(key)
        print()
        return Dictionary


def Column_control(Column_name):
    if Column_name == 'name':
        return 1
    elif Column_name == 'lastname':
        return 2
    elif Column_name == 'email':
        return 3
    elif Column_name == 'grade':
        return 4
    else:
        return 5


def punc(punctuation):
    if punctuation == '<':
        return 1
    elif punctuation == '>':
        return 2
    elif punctuation == '=':
        return 3
    elif punctuation == '!=':
        return 4
    elif punctuation == '<=':
        return 5
    elif punctuation == '>=':
        return 6
    elif punctuation == '!<':
        return 7
    elif punctuation == '!>':
        return 8
    else:
        return 9


def Wrong_input():
    print('Wrong input Please try again!!!!')


with open("students.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # başlıktaki sütun isimlerinin tutulduğu değişken
    Students = file.readlines()

StudentsDict = {}

for Student in Students:
    split_lines = Student.split(";")
    split_lines[0] = int(split_lines[0])
    StudentsDict[split_lines[0]] = [split_lines[1], split_lines[2], split_lines[3], split_lines[4].replace("\n", "")]
    # reading csv file
index = 0
tempdict = {}
tempdict2 = {}#temp dictionaries for select 'OR' parts

#We provided a control
#with if conditions on the length of the given input and
#the correctness of the data, and we proceeded in this way.


while True:
    print('Enter the action you want to do: ')
    User_input = input()
    if User_input == 'exit':
        JSON(StudentsDict, None, None, index)  # write json file
        break
    splitted_input = User_input.split(" ")

    if len(splitted_input) < 4:
        Wrong_input()
    elif splitted_input[0] == 'SELECT' and splitted_input[1].__contains__(',') == False and splitted_input[2] + ' ' + \
            splitted_input[3] == 'FROM STUDENTS':
        if len(splitted_input) == 11:
            if splitted_input[1] == 'ALL':
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER':
                    StudentsDict = Select1(splitted_input[5], punc(splitted_input[6]), splitted_input[7], StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, None, None, index)
                    index = index + 1
                else:
                    Wrong_input()
            elif Column_control(splitted_input[1]) == 5:
                Wrong_input()

            else:
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER':
                    StudentsDict = Select1(splitted_input[5], punc(splitted_input[6]), splitted_input[7], StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input[1], None, index)
                    index = index + 1
                else:
                    Wrong_input()
        elif len(splitted_input) == 15:
            if splitted_input[1] == 'ALL':
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'AND':
                    StudentsDict = Select_and1(splitted_input[5], punc(splitted_input[6]), splitted_input[7],
                                               splitted_input[9], punc(splitted_input[10]), splitted_input[11],
                                               StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, None, None, index)
                    index = index + 1
                elif (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'OR':
                    tempdict = Select1(splitted_input[5], punc(splitted_input[6]), splitted_input[7], StudentsDict)
                    tempdict2 = Select1(splitted_input[9], punc(splitted_input[10]), splitted_input[11],
                                        StudentsDict)
                    tempdict.update(tempdict2)
                    StudentsDict = tempdict
                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, None, None, index)
                    index = index + 1
                else:
                    Wrong_input()
            elif Column_control(splitted_input[1]) == 5 or Column_control(splitted_input[5]) == 5 or Column_control(
                    splitted_input[9]) == 5 or punc(splitted_input[6]) == 9 or punc(splitted_input[10]) == 9:
                Wrong_input()
            else:
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'AND':
                    StudentsDict = Select_and1(splitted_input[5], punc(splitted_input[6]), splitted_input[7],
                                               splitted_input[9], punc(splitted_input[10]), splitted_input[11],
                                               StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input[1], None, index)
                    index = index + 1
                elif (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'OR':
                    tempdict = Select1(splitted_input[5], punc(splitted_input[6]), splitted_input[7], StudentsDict)
                    tempdict2 = Select1(splitted_input[9], punc(splitted_input[10]), splitted_input[11],
                                        StudentsDict)
                    tempdict.update(tempdict2)
                    StudentsDict = tempdict
                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input[1], None, index)
                    index = index + 1
                else:
                    Wrong_input()
        else:
            Wrong_input()



    elif splitted_input[0] == 'SELECT' and splitted_input[1].__contains__(',') and splitted_input[2] + ' ' + \
            splitted_input[3] == 'FROM STUDENTS':
        if len(splitted_input) == 11:
            splitted_input_2 = splitted_input[1].split(',')
            if Column_control(splitted_input_2[0]) == 5 or Column_control(splitted_input_2[1]) == 5 or len(
                    splitted_input_2) != 2:
                Wrong_input()
            else:
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER':
                    StudentsDict = Select1(splitted_input[5], punc(splitted_input[6]),
                                           splitted_input[7], StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input_2[0], splitted_input_2[1], index)
                    index = index + 1
                else:
                    Wrong_input()
        elif len(splitted_input) == 15:
            splitted_input_2 = splitted_input[1].split(',')
            if Column_control(splitted_input_2[0]) == 5 or Column_control(splitted_input_2[1]) == 5 or len(
                    splitted_input_2) != 2:
                Wrong_input()
            else:
                if (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'AND':
                    StudentsDict = Select_and1(splitted_input[5], punc(splitted_input[6]), splitted_input[7],
                                               splitted_input[9], punc(splitted_input[10]), splitted_input[11],
                                               StudentsDict)

                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input_2[0], splitted_input_2[1], index)
                    index = index + 1
                elif (splitted_input[-1] == 'ASC' or splitted_input[-1] == 'DSC') and splitted_input[-2] == 'BY' and \
                        splitted_input[-3] == 'ORDER' and splitted_input[8] == 'OR':
                    tempdict = Select1(splitted_input[5], punc(splitted_input[6]),
                                       splitted_input[7], StudentsDict)
                    tempdict2 = Select1(splitted_input[9], punc(splitted_input[10]),
                                        splitted_input[11], StudentsDict)
                    tempdict.update(tempdict2)
                    StudentsDict = tempdict
                    StudentsDict = Ordering(StudentsDict, splitted_input[-1])
                    JSON(StudentsDict, splitted_input_2[0], splitted_input_2[1], index)
                    index = index + 1

                else:
                    Wrong_input()
        else:
            Wrong_input()



    elif splitted_input[0] + ' ' + splitted_input[1] + ' ' + splitted_input[2] + ' ' + splitted_input[
        3] == 'DELETE FROM STUDENT WHERE':
        if len(splitted_input) == 11:
            if Column_control(splitted_input[4]) == 5 or punc(splitted_input[5]) == 9 or Column_control(
                    splitted_input[8]) == 5 or punc(splitted_input[9]) == 9:
                Wrong_input()
            else:
                if splitted_input[7] == 'AND':
                    StudentsDict = DeleteAnd(splitted_input[4], punc(splitted_input[5]), splitted_input[6],
                                             splitted_input[8],
                                             punc(splitted_input[9]), splitted_input[10], StudentsDict)  # Delete
                    print()
                elif splitted_input[7] == 'OR':
                    StudentsDict = Delete(splitted_input[4], punc(splitted_input[5]), splitted_input[6],
                                          StudentsDict)  # DELETE
                    StudentsDict = Delete(splitted_input[8], punc(splitted_input[9]), splitted_input[10], StudentsDict)
                else:
                    Wrong_input()
        elif len(splitted_input) == 7:
            if Column_control(splitted_input[4]) == 5 or punc(splitted_input[5]) == 9:
                Wrong_input()
            else:
                StudentsDict = Delete(splitted_input[4], punc(splitted_input[5]), splitted_input[6],
                                      StudentsDict)  # DELETE
        else:
            Wrong_input()



    elif splitted_input[0] + ' ' + splitted_input[1] + ' ' + splitted_input[2] == 'INSERT INTO STUDENT':
        splitted_input_2 = splitted_input[3].split('(')
        if (splitted_input_2[0] == 'VALUES'):
            splitted_input = splitted_input_2[1].split(')')
            splitted_input_2 = splitted_input[0].split(',')
            if len(splitted_input_2) == 5:
                StudentsDict = Insert(splitted_input_2[0], splitted_input_2[1], splitted_input_2[2],
                                      splitted_input_2[3], splitted_input_2[4], StudentsDict)  # Insert
            else:
                Wrong_input()
        else:
            Wrong_input()
    else:
        Wrong_input()
