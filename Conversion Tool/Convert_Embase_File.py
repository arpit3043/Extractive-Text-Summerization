import pandas as pd
import xlrd
import time
#print(xlrd.__VERSION__)
import os
try:
    BASE_PATH="C:\\Users\\hp\\Desktop\\New Folder"  
    lis=os.listdir(BASE_PATH)
    Custom_File_Name=input("Hey Buddy ,\nFirst of all rename the file to \nEnter Name For Resultant Converted File\n")
    Custom_File_Name=BASE_PATH+"\\Results\\"+Custom_File_Name+".csv"
    FILE_NAME=str(lis[0])
    #print(FILE_NAME)
    FILE_NAME=BASE_PATH+"\\"+FILE_NAME
    EXTENSION_OF_FILE=FILE_NAME.split('.')
    #print(EXTENSION_OF_FILE[1])
    dataset=pd.read_excel(FILE_NAME)
    df=pd.DataFrame({'Combined':dataset['Title'].str.cat(dataset['Author Names'],sep=". ")})
    df['Combined']=df['Combined'].str.cat(dataset['Source'],sep=" ")

    sub=pd.DataFrame({"Combined Info for Embase Abstracts":df['Combined']})
    sub.to_csv(Custom_File_Name,index=False)
    print("File Converted Successfully !!")
    time.sleep(4)
except :
    print("File cannot be Converted !!")
    print("Possible Problems : \n1.) File not pasted in the directory\n2.) File has extension problem")
    time.sleep(5)
