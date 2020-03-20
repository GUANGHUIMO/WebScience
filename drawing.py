import csv
import matplotlib.pyplot as plt

accurate_list = []
excitement_list = []
happy_list = []
pleasant_list = []
surprise_list = []
fear_list = []
angry_list = []

f = open('D:\Twitter Crawler\Twitter Crawler\excitement_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0

for i in range(1,len(column)):
    if column[i] == 'Excitement':
        count += 1
        excitement_count +=1
    elif column[i] == 'Happy':
        happy_count += 1
    elif column[i] == 'Pleasant':
        pleasant_count += 1
    elif column[i] == 'Surprise':
        surprise_count += 1
    elif column[i] == 'Fear':
        fear_count += 1
    elif column[i] == 'Angry':
        angry_count += 1
excite_accuracy = count/len(column)
accurate_list.append(excite_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)

f = open('D:\Twitter Crawler\Twitter Crawler\happy_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0
for i in range(1,len(column)):
    if column[i] == 'Happy':
        count += 1
        happy_count += 1
    elif column[i] == 'Pleasant':
        pleasant_count += 1
    elif column[i] == 'Surprise':
        surprise_count += 1
    elif column[i] == 'Fear':
        fear_count += 1
    elif column[i] == 'Angry':
        angry_count += 1
    elif column[i] == 'Excitement':
        excitement_count += 1

happy_accuracy = count/len(column)
accurate_list.append(happy_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)

f = open('D:\Twitter Crawler\Twitter Crawler\pleasant_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0
for i in range(1,len(column)):
    if column[i] == 'Pleasant':
        count += 1
        pleasant_count += 1
    elif column[i] == 'Happy':
        happy_count += 1
    elif column[i] == 'Surprise':
        surprise_count += 1
    elif column[i] == 'Fear':
        fear_count += 1
    elif column[i] == 'Angry':
        angry_count += 1
    elif column[i] == 'Excitement':
        excitement_count += 1
pleasant_accuracy = count/len(column)
accurate_list.append(pleasant_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)

f = open('D:\Twitter Crawler\Twitter Crawler\surprise_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0
for i in range(1,len(column)):
    if column[i] == 'Surprise':
        count += 1
        surprise_count += 1
    elif column[i] == 'Excitement':
        excitement_count += 1
    elif column[i] == 'Pleasant':
        pleasant_count += 1
    elif column[i] == 'Happy':
        happy_count += 1
    elif column[i] == 'Fear':
        fear_count += 1
    elif column[i] == 'Angry':
        angry_count += 1

surprise_accuracy = count/len(column)
accurate_list.append(surprise_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)

f = open('D:\Twitter Crawler\Twitter Crawler\\fear_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0
for i in range(1,len(column)):
    if column[i] == 'Fear':
        count += 1
        fear_count += 1
    elif column[i] == 'Excitement':
        excitement_count += 1
    elif column[i] == 'Pleasant':
        pleasant_count += 1
    elif column[i] == 'Happy':
        happy_count += 1
    elif column[i] == 'Surprise':
        surprise_count += 1
    elif column[i] == 'Angry':
        angry_count += 1

fear_accuracy = count/len(column)
accurate_list.append(fear_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)

f = open('D:\Twitter Crawler\Twitter Crawler\\angry_crowdsourcing.csv')
reader = csv.reader(f)
column = [row[28] for row in reader]
count = 0
excitement_count = 0
happy_count = 0
pleasant_count = 0
surprise_count = 0
fear_count = 0
angry_count = 0
for i in range(1,len(column)):
    if column[i] == 'Angry':
        count += 1
        angry_count += 1
    elif column[i] == 'Excitement':
        excitement_count += 1
    elif column[i] == 'Pleasant':
        pleasant_count += 1
    elif column[i] == 'Happy':
        happy_count += 1
    elif column[i] == 'Surprise':
        surprise_count += 1
    elif column[i] == 'Fear':
        fear_count += 1

angry_accuracy = count/len(column)
accurate_list.append(angry_accuracy)
excitement_list.append(excitement_count)
happy_list.append(happy_count)
pleasant_list.append(pleasant_count)
surprise_list.append(surprise_count)
fear_list.append(fear_count)
angry_list.append(angry_count)


print(excitement_list)
print(happy_list)
print(pleasant_list)
print(surprise_list)
print(fear_list)
print(angry_list)

name_list = ['Excitement','Happy','Pleasant','Surprise','Fear','Angry']
plt.bar(range(len(accurate_list)), accurate_list,color='rgb',tick_label=name_list)
plt.show()


cum1 =list(map(sum, zip(list(excitement_list),list(happy_list))))
cum2 =list(map(sum, zip(list(excitement_list),list(happy_list),list(pleasant_list))))
cum3 =list(map(sum, zip(list(excitement_list),list(happy_list),list(pleasant_list),list(surprise_list))))
cum4 =list(map(sum, zip(list(excitement_list),list(happy_list),list(pleasant_list),list(surprise_list),list(fear_list))))
name_list = ['Excitement','Happy','Pleasant','Surprise','Fear','Angry']
plt.bar(range(len(excitement_list)), excitement_list, label='excitement',fc = 'yellow')
plt.bar(range(len(happy_list)), happy_list, bottom=excitement_list, label='happy',tick_label = name_list,fc = 'red')
plt.bar(range(len(pleasant_list)), pleasant_list, bottom=cum1, label='pleasant',tick_label = name_list,fc = 'green')
plt.bar(range(len(surprise_list)), surprise_list, bottom=cum2, label='surprise',tick_label = name_list,fc = 'black')
plt.bar(range(len(fear_list)), fear_list, bottom=cum3, label='fear',tick_label = name_list,fc = 'blue')
plt.bar(range(len(angry_list)), angry_list, bottom=cum4, label='angry',tick_label = name_list,fc = 'orange')
plt.legend()
plt.show()





