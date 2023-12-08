import csv
import matplotlib.pyplot as mp
import statistics as st
import pygal
filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    #variable to store number of steps/day
    dictDate = dict()
    #number of steps per day
    dictInterval = dict()
    for row in reader:
        steps = row[0]
        if steps != 'NA':
            date = row[1]
            interval = int(row[2])
            dictDate.setdefault(str(date),[])
            dictDate[str(date)].append(int(steps))

            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
#number of steps per day
listDate = []
listTotal = []
for i in dictDate.keys():
    listDate.append(i)
    listTotal.append(sum(dictDate.get(i)))

#mean
print(f'Mean: {st.mean(listTotal)}')

#median
q = sorted(listTotal)
print(f'Median: {st.median(q)}')

#histogram
hist = pygal.Bar()
hist.title = "Total Steps"
hist._x_axis = "Steps per day"
hist._y_axis = "Frequency"
hist.x_labels = listDate
hist.add("Total number of steps",listTotal)
hist.render_to_file("StepsPerDay.svg")