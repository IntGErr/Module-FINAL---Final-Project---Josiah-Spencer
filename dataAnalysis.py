from bokeh.plotting import figure, show
dataDict = {}

with open("Qualitative and Quantitive data for GOA.csv",'r') as t:
    i = 0
    for line in t:
        if line[1] != "T":
            i += 1
            templist = []
            e = line
            tempval = e.split(',')
# find data for first question
            if tempval[1][5] == "w":    
                if tempval[1][0] == "1":
                    templist.append(7)
                if tempval[1][0] != "1":
                    templist.append(21)
            else:
                if tempval[1][0] == "1":
                    templist.append(1)
                if tempval[1][0] != "1":
                    templist.append(3)
# find data for second question
            if tempval[2][0] != "L":
                templist.append(int(tempval[2][1]) * 7)
            else:
                templist.append(0)
# find data for third question
            if tempval[3][1] != "Y":
                templist.append(0)
            else:
                if tempval[3][5] == "l":
                    templist.append(1)
                if tempval[3][5] == "m":
                    templist.append(2)
                if tempval[3][5] == "e":
                    templist.append(3)
# find data for fourth question
            supertemp = tempval[4].split('"')
            templist.append(int(supertemp[1]))

            dataDict["participant" + str(i)] = [templist]
print("")
print("data:")
print(dataDict)
print("")

print(dataDict['participant1'][0][0])
x = []
y = []
for d in range(len(dataDict)):
# x value = days spent on working legs / number of days skiing
    x.append(dataDict['participant' + str(d+1)][0][1] / dataDict['participant' + str(d+1)][0][0])
# y value = how often you get injured on a scale of 1-10
    y.append(dataDict['participant' + str(d+1)][0][3])

p = figure(
    title="Point Graph Example", x_axis_label="days spent on working legs / number of days skiing", y_axis_label="how often you get injured on a scale of 1-10"
)

p.scatter(x, y, size=10, color=(0, 0, 0), alpha=0.8)

show(p)