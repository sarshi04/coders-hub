import pandas as pd
import string
import ast
import csv

#creating dataframe of two files one is indiacom and other is justdial

df1 = pd.read_csv(r"C:\Users\Arshi Sinha\PycharmProjects\day6\indiacom_scapped_data.txt", delimiter="\t")
df2 = pd.read_csv(r"C:\Users\Arshi Sinha\PycharmProjects\day6\data.txt", delimiter=",")


def string_matching(str1, str2):   #string matching function
    scrapper = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'your', 'yours', 'yourself', 'a', 'an',
                'the',
                'and', 'at', 'by', 'against', 'between', 'before', 'after', 'above', 'below', 'to', 'from', 'of',
                'down',
                'in', 'out', 'on', 'off', 'over', 'under', 'only', 'very', 'now', 'classes', 'home', 'tutors',
                'company',
                'tutor', 'tutorials', 'academy', 'classes', 'pvt', 'ltd', 'institute', 'exams', 'education', 'coaching',
                'tutorial', 'point', 'center', 'centre', 'opp', 'near', 'behind', 'square', 'opposite', 'above',
                'below']
    for c in string.punctuation:   #remove puctuations from the data
        str1, str2 = str1.replace(c, ""), str2.replace(c, "")
    stop1 = [i for i in str1.lower().split() if i not in scrapper]   #to remove unnecessary stop words
    stop2 = [j for j in str2.lower().split() if j not in scrapper]
    l1, l2 = len(stop1), len(stop2)
    set1, set2 = set(stop1), set(stop2)  #removing duplicates using set
    a = 0
    for i in set1:
        for j in set2:
            if i == j:
                a = a + 1
    try:
        p12 = (float(a) / l1) * 100
    except ZeroDivisionError:
        p12 = 0
    try:
        p21 = (float(a) / l2) * 100
    except ZeroDivisionError:
        p21 = 0
    return round(p12, 2), round(p21, 2)


def read_df(df1, df2):   #this function is built to get the match percent of the scrapped data
    match_percent = []
    for i in range(1, len(df1)):
        for j in range(1, len(df2)):
            np12, np21 = string_matching(df1.name[i], df2.name[j])
            add1 = str(ast.literal_eval(df1["address"][i])["address line1"]) + "," + str(ast.literal_eval(df1["address"][i])["address line2"])
            add2 = str(ast.literal_eval(df2["address"][j])["address line 1"]) + "," + str(ast.literal_eval(df2["address"][j])["address line 2"])
            mp12, mp21 = string_matching(add1, add2)
            a = ast.literal_eval(df1["phones"][i])["phone"]
            a = a.split()
            dict = df2["phone"][j].replace('[', '').replace(']', '')
            b = ast.literal_eval(dict)["phone"]
            len1, len2 = len(a), len(b)
            k = 0
            for m in a:
                for n in b:
                    if m == n:
                        k = k+1
            try:
                ph1 = (float(k) / len1) * 100
            except ZeroDivisionError:
                ph1 = 0
            try:
                ph2 = (float(k) / len2) * 100
            except ZeroDivisionError:
                ph2 = 0
            list3 = [np12, np21, mp12, mp21, round(ph1, 2), round(ph2, 2)]
            match_percent.append(list3)
    with open('indiacom_justdial_csv.txt', 'w') as f:   #writing the match percentage in a text file
        writer = csv.writer(f, delimiter=',')
        writer.writerow(["name1", "name2", "address1", "address2", "phone1", "phone2"])
        for p in match_percent:
            writer.writerow(p)
    print(match_percent)


read_df(df1, df2)


