import psycopg2
import pandas as pd
import re as re

df = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio1.csv", delimiter= ',')
df2 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio1.csv", delimiter = ",")
df3 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio1_short.csv", delimiter = ",")
df4 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts_short.csv", delimiter = ",")
id = df4.sessionid.to_list()
num = df4.id.to_list()

ids = []
version = []
for i in id:
    x = i.split(".")
    var = x[0]
    ids.append(var)
    version.append(0)
print(ids)
# Connect to your postgres DB
conn = psycopg2.connect("dbname=emudata user=qa3ad23 password=cvV-awq-K6L-fdg host=localhost port=5432")

print("connected")
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query

PHQ = []
phq1 = []
phq2 = []
phq3 = []
phq4 = []
phq5 = []
phq6 = []
phq7 = []
phq8 = []
phq9 = []
for element in ids:


    values = []
    values2 = []
    cur.execute(
        "SELECT DISTINCT json from data where type like %s and source like %s and sessionid like %s ESCAPE '' ",
        ('phq', 'summerDepreST', element))
    ans = cur.fetchall()
    print(ans)
    count = len(ans)
    if count > 0:
        string = ""
        for x in ans:
            string = x[0]

        string = string.split('content":"')

        for i in string:
            if '\"Q0\\' in i:
                string = i
            else:
                continue

        string2 = ''.join(string)
        string2 = string2.split(",")


        for seq in string2:
            string3 = "".join(seq)
            string3 = string3.split(":")
            for variable in string3:

                if "Q" not in variable:

                    temp = re.findall(r'\d+', variable)
                    result = list(map(int, temp))
                    values.append(result)

                else:
                    continue


        for small in values:
            for value in small:
                values2.append(value)
        print(values2)
        q1 = values2[0]
        q2 = values2[1]
        q3 = values2[2]
        q4 = values2[3]
        q5 = values2[4]
        q6 = values2[5]
        q7 = values2[6]
        q8 = values2[7]
        q9 = values2[8]
        score = sum(values2)
        if score >= 10:
            phq = 1
        else:
            phq = 0


    else:
        phq = "error"

    PHQ.append(phq)

print("PHQ done")

gadQ1 = []
gadQ2 = []
gadQ3 = []
gadQ4 = []
gadQ5 = []
gadQ6 = []
gadQ7 = []
gad7 = []
for ele in ids:


    values = []
    values2 = []
    cur.execute(
        "SELECT DISTINCT json from data where type like %s and source like %s and sessionid like %s ESCAPE '' ",
        ('gad', 'summerDepreST', ele))

    ans = cur.fetchall()
    print(ans)
    count = len(ans)
    if count > 0:
        string = ""
        for x in ans:
            string = x[0]

        string = string.split('content":"')

        for i in string:
            if '\"Q0\\' in i:
                string = i
            else:
                continue

        string2 = ''.join(string)
        string2 = string2.split(",")

        for seq in string2:
            string3 = "".join(seq)
            string3 = string3.split(":")
            for variable in string3:

                if "Q" not in variable:

                    temp = re.findall(r'\d+', variable)
                    result = list(map(int, temp))
                    values.append(result)

                else:
                    continue

        for small in values:
            for value in small:
                values2.append(value)
        print(values2)
        q1 = values2[0]
        q2 = values2[1]
        q3 = values2[2]
        q4 = values2[3]
        q5 = values2[4]
        q6 = values2[5]
        q7 = values2[6]
        gscore = sum(values2)
        if gscore >= 10:
            gad = 1
        else:
            gad = 0
    else:
        gad = "error"
    gad7.append(gad)
print("GAD done")

data = pd.DataFrame()
data["sessionid"] = ids
data["num"] = num

data["PHQ"] = PHQ

data["GAD"] = gad7




data.to_csv('/Users/miranda/PycharmProjects/pythonProject9/new_architecture/label_audio3_gad_phq_2.csv')

cur.close()
conn.close()
