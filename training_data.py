import pandas as pd
import csv

with open('training_data.txt', 'a+') as f1:
    df1 = pd.read_csv("indiacom_target_csv.txt")  #reading files using pandas
    df2 = pd.read_csv("indiacom_grotal_csv.txt")
    df3 = pd.read_csv("indiacom_justdial_csv.txt")
    writer = csv.writer(f1, delimiter=',')
    writer.writerow(["name1", "name2", "address1", "address2", "phone1", "phone2", "bin"])
    count = 0
    for j in range(len(df1)):  #appending perfect data to a file for training data
        list1 = [df1["name1"][j], df1["name2"][j], df1["address1"][j], df1["address1"][j], df1["phone1"][j], df1["phone2"][j]]
        if (list1[0] >= 50.0) and (list1[1] >= 50.0) and (list1[2] > 0.0) and (list1[3] > 0.0) and list1[4] > 0.0 and list1[5] > 0.0:
            print(list1)
            count = count + 1
            writer.writerow(list1)
            if count > 10:
                break
    #"********TARGET_STUDY***********"
    print("**********************")
    for j in range(len(df2)):
        list2 = [df2["name1"][j], df2["name2"][j], df2["address1"][j], df2["address1"][j], df2["phone1"][j], df2["phone2"][j]]
        if (list2[0] >= 50.0) and (list2[1] >= 50.0) and (list2[2] > 0.0) and (list2[3] > 0.0) and (list2[4] != 0.0) and (list2[5] != 0.0):
            print(list2)
            count = count + 1
            writer.writerow(list2)
    #"***********GROTAL************"
    print("**********************")
    for j in range(len(df3)):
        list3 = [df3["name1"][j], df3["name2"][j], df3["address1"][j], df3["address1"][j], df3["phone1"][j], df3["phone2"][j]]
        if (list3[0] >= 50.0) and (list3[1] >= 50.0) and (list3[2] > 0.0) and (list3[3] > 0.0) and (list3[4] != 0.0) and (list3[5] != 0.0):
            print(list3)
            count = count + 1
            writer.writerow(list3)
    #"***********JUSTDIAL************"
    print("**********************")
    print(count)

