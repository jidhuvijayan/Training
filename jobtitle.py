import csv
f = open('/home/cpu-089/Documents/python/jobtitle.csv')
t = open('outputjobtitle.csv', 'w')
person_data_list = []
reader = csv.reader(f)
    
for item in reader:
    person_data_list.append(item)
    writer = csv.writer(t)
    writer.writerows(person_data_list)
print "every thing k...GO TO THE FILE outputjobtitle.csv in your Documents/python"