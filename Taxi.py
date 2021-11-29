# Programmers: William Grimmer
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: [Name of output file, Long, Lat,Miles, Date]
# Program Outputs: [All trips in certain distance, all trips on a certain date, average cash and credit payments]

# IMPORTANT
# in order for the program to run, put the .csv files '2016_09.csv' and '2016_10.csv' into your temp directory
# The temp directory is usually C:\Users\YourName\AppData\Local\Temp
import os
import tempfile
import numpy as np
import math as m
import csv
def read_file(file):
    data_list=[]
    for line in file:
        data_list.append(line.split(","))
    file.close()
    return data_list
def fixlast(l):
    for x in l:
        x[-1] = x[-1].strip()
    return l
def average_payments(s,o):
    cashpayments=0
    cardpayments=0
    cashtotal=0
    cardtotal=0
    count=0
    for i in s:
        if i[6]=="Cash":
            # print(cashtotal)
            cashpayments =cashpayments+1
            cashtotal=cashtotal+float(i[5])
            count+=1
            # print(count)
        else:
            # print(cardtotal)
            cardpayments = cardpayments + 1
            cardtotal = cardtotal + float(i[5])
            count += 1
            # print(count)
    for i in o:
        if i[6]=="Cash":
            # print(cashtotal)
            cashpayments =cashpayments+1
            cashtotal=cashtotal+float(i[5])
            count += 1
            # print(count)
        else:
            # print(cardtotal)
            cardpayments = cardpayments + 1
            cardtotal = cardtotal + float(i[5])
            count += 1
            # print(count)
    print("average cost of cash payments was " + str(cashtotal/cashpayments))
    print("average cost of card payments was " + str(cardtotal / cardpayments))
def tripcount(s,o):
    on=False
    count=0
    date=input("input a date in Y-M-D format ex(2016-9-12) from 2016-9-~ to 2016-10-~")
    if date[5] == "9":
        for i in s:
            # print(date)
            # print(str(i[2]))
            if date in str(i[2]) or date in str(i[1]):
                count=count+1
    if date[5] == "1":
        date = "10/"+date[8:]+"/2016"
        print("in")
        for i in o:
            # print(date)
            # print(str(i[2]))
            if date in str(i[2]) or date in str(i[1]):
                count = count + 1
    print("total trips on " +date+ " were "+ str(count))
def tripsinrange(o,s):
    dist=float(input("distance in miles"))
    lat1=float(input("input latitude"))
    lon1=float(input("input longitude"))
    name=input("what would you like to name the file?")
    output=[]
    name=name+'.csv'
    for i in s:
        if (m.acos(m.sin(lat1) * m.sin(float(i[8])) + m.cos(lat1) * m.cos(float(i[8])) * m.cos(lon1 - float(i[9]))) * 3959) <= dist:
            output.append(i)
        elif (m.acos(m.sin(lat1) * m.sin(float(i[10])) + m.cos(lat1) * m.cos(float(i[10])) * m.cos(lon1 - float(i[11]))) * 3959) <= dist:
            output.append(i)
    for i in o:
        if (m.acos(m.sin(lat1) * m.sin(float(i[8])) + m.cos(lat1) * m.cos(float(i[8])) * m.cos(lon1 - float(i[9]))) * 3959) <= dist:
            output.append(i)
        elif (m.acos(m.sin(lat1) * m.sin(float(i[10])) + m.cos(lat1) * m.cos(float(i[10])) * m.cos(lon1 - float(i[11]))) * 3959) <= dist:
            output.append(i)
    np.savetxt(name, output, delimiter=", ", fmt="% s")



def main():
    path = os.path.join(tempfile.gettempdir(), '2016_09.csv')
    path2 = os.path.join(tempfile.gettempdir(), '2016_10.csv')
    f = open(path, 'r')
    f2 = open(path2, 'r')
    list_sept=read_file(f)
    list_oct=read_file(f2)
    list_oct=fixlast(list_oct)
    list_sept=fixlast(list_sept)
    # totallist=np.concatenate((list_sept, list_oct), axis=0)
    # print(list_sept)
    # print(list_oct)
    # print(totallist)
    average_payments(list_sept,list_oct)
    tripcount(list_sept,list_oct)
    tripsinrange(list_sept,list_oct)

main()
