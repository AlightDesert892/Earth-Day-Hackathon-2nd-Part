#Importing packages
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pan





#Initializing the data that needs to be initialized
Co2Data = []
validMonthlyYears = []
Years = set()
yearlyMonthlyCo2Dict = {}
secondYearlyMonthlyCo2Dict = {}
yearlyAverageCo2Dict = {}
validYears = []
personalizedYears = []
yearlyCo2Dict = {}
variatingYearlyMonthlyCo2Dict = {}
def bulbs(sort):
  for i in range(len(sort)):
    for i in range(1, len(sort)):
      if sort[i - 1] > sort[i]:
        sort[i - 1], sort[i] = sort[i], sort[i - 1]
  return sort





#Creating the data
f = open('Co2Data.csv', 'r', encoding = "utf-8")
Temp2Co2Data = csv.DictReader(f)
for row in Temp2Co2Data:
  Co2Data.append(row)
for i in range(len(Co2Data)):
  if Co2Data[i]['Carbon Dioxide (ppm)'] != '':
    yearlyMonthlyCo2Dict[int(Co2Data[i]['Year'])] = []
    secondYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = 0
    yearlyCo2Dict[int(Co2Data[i]['Year'])] = []
    variatingYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = 0
for i in range(len(Co2Data)):
  Years.add(int(Co2Data[i]['Year']))
  if Co2Data[i]['Carbon Dioxide (ppm)'] != '':
    yearlyMonthlyCo2Dict[int(Co2Data[i]['Year'])].append(float(Co2Data[i]['Carbon Dioxide (ppm)']))
    secondYearlyMonthlyCo2Dict[float(Co2Data[i]['Decimal Date'])] = float(Co2Data[i]['Carbon Dioxide (ppm)'])
    validMonthlyYears.append(float(Co2Data[i]['Decimal Date']))
    validYears.append(int(Co2Data[i]['Year']))
    yearlyCo2Dict[int(Co2Data[i]['Year'])].append(float(Co2Data[i]['Carbon Dioxide (ppm)']))
Years = list(Years)
Years = bulbs(Years)
tempYears = Years
for i in range(len(Years)):
  Years[i] = str(Years[i])
mean = sum(secondYearlyMonthlyCo2Dict.values()) / len(secondYearlyMonthlyCo2Dict.values())
if len(str(mean).split('.')[1]) > 2:
    mean = float(str(mean).split('.')[0] + '.' + str(mean).split('.')[1][0 : 2])
for i in range(len(validMonthlyYears)):
  if mean > secondYearlyMonthlyCo2Dict[validMonthlyYears[i]]:
    variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]] = mean - secondYearlyMonthlyCo2Dict[validMonthlyYears[i]]
  else:
    variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]] = secondYearlyMonthlyCo2Dict[validMonthlyYears[i]] - mean
for j in validMonthlyYears:
  if len(str(variatingYearlyMonthlyCo2Dict[j]).split('.')[1]) > 2:
    variatingYearlyMonthlyCo2Dict[j] = float(str(variatingYearlyMonthlyCo2Dict[j]).split('.')[0] + '.' + str(variatingYearlyMonthlyCo2Dict[j]).split('.')[1][0 : 2])
startAndEndDates = {'Start Date': input('Please type a start year between 1958 and 2017 for a range of data to plot: '), 'End Date': input('Please type a end year higher than your start years and between 1958 and 2017 for a range of data to plot: ')}
while startAndEndDates['Start Date'] == startAndEndDates['End Date'] or (startAndEndDates['Start Date'] not in Years or startAndEndDates['End Date'] not in Years) or (int(startAndEndDates['Start Date']) > int(max(tempYears)) or int(startAndEndDates['Start Date']) < int(min(tempYears))) or (int(startAndEndDates['End Date']) > int(max(tempYears)) and int(startAndEndDates['End Date']) < int(min(tempYears))):
  print('Dates Invalid!')
  startAndEndDates = {'Start Date': input('Please type a start year between 1958 and 2017 for a range of data to plot: '), 'End Date': input('Please type a end year higher than your start years and between 1958 and 2017 for a range of data to plot: ')}
startAndEndDates['Start Date'] = int(startAndEndDates['Start Date'])
startAndEndDates['End Date'] = int(startAndEndDates['End Date'])
if startAndEndDates['Start Date'] > startAndEndDates['End Date']:
  startAndEndDates['Start Date'], startAndEndDates['End Date'] = startAndEndDates['End Date'], startAndEndDates['Start Date']
  print('You set the start year greater than the end year, start year and end year swapped:\n  Start Year: ' + str(startAndEndDates['Start Date']) + '\n  End Year: ' + str(startAndEndDates['End Date']))
barplotLength = input('How long would you like a bar graph and a box plot to be with a averaged co2 level representing each bar and regular co2 level representing each box(Type a integer greater than 0): ')
while not barplotLength.isnumeric() or int(barplotLength) <= 0:
  print('Invalid Number!')
  barplotLength = input('How long would you like a bar graph and a box plot to be with a averaged co2 level representing each bar and regular co2 level representing each box(Type a integer greater than 0): ')
barplotLength = int(barplotLength)
for i in range(barplotLength):
  personalizedYear = input('Type a year from 1958 to 2017 to include in your bar graph: ')
  while (personalizedYear not in Years or (int(personalizedYear) > int(max(tempYears)) or int(personalizedYear) < int(min(tempYears))) or (int(startAndEndDates['End Date']) > int(max(tempYears)) or int(personalizedYear) in personalizedYears)):
    print('Invalid Date/Already have date!')
    personalizedYear = input('Type a year from 1958 to 2017 to include in your bar graph: ')
  personalizedYears.append(int(personalizedYear))
for i in range(len(Years)):
  Years[i] = int(Years[i])
for j in Years:
  temp = 0
  for i in yearlyMonthlyCo2Dict[j]:
    temp += i
  yearlyAverageCo2Dict[j] = temp / len(yearlyMonthlyCo2Dict[j])
  if len(str(yearlyAverageCo2Dict[j]).split('.')[1]) > 2:
    yearlyAverageCo2Dict[j] = float(str(yearlyAverageCo2Dict[j]).split('.')[0] + '.' + str(yearlyAverageCo2Dict[j]).split('.')[1][0 : 2])
lineplotYearlyAverageCo2Dict = {'Years': Years, 'Co2' : []}
for i in Years:
  lineplotYearlyAverageCo2Dict['Co2'].append(yearlyAverageCo2Dict[i])
df = pan.DataFrame(data = lineplotYearlyAverageCo2Dict)
scatterplotYearlyMonthlyCo2Dict = {'Years': validMonthlyYears, 'Co2': []}
for i in range(len(validMonthlyYears)):
  scatterplotYearlyMonthlyCo2Dict['Co2'].append(secondYearlyMonthlyCo2Dict[validMonthlyYears[i]])
df2 = pan.DataFrame(data = scatterplotYearlyMonthlyCo2Dict)
lineplotPersonalizedYearlyAverageCo2Dict = {'Years': [], 'Co2' : []}
for i in range(startAndEndDates['Start Date'], startAndEndDates['End Date'] + 1):
  lineplotPersonalizedYearlyAverageCo2Dict['Years'].append(i)
  lineplotPersonalizedYearlyAverageCo2Dict['Co2'].append(yearlyAverageCo2Dict[i])
df3 = pan.DataFrame(data = lineplotPersonalizedYearlyAverageCo2Dict)
scatterplotPersonalizedYearlyMonthlyCo2Dict = {'Years': [], 'Co2': []}
for i in range(len(validMonthlyYears)):
  if int(str(validMonthlyYears[i]).split('.')[0]) == startAndEndDates['Start Date']:
    startDateIndex = i
    break
for i in range(len(validMonthlyYears) - 1, 0, -1):
  if int(str(validMonthlyYears[i]).split('.')[0]) == startAndEndDates['End Date']:
    endDateIndex = i
    break
for i in range(startDateIndex, endDateIndex + 1):
  scatterplotPersonalizedYearlyMonthlyCo2Dict['Years'].append(validMonthlyYears[i])
  scatterplotPersonalizedYearlyMonthlyCo2Dict['Co2'].append(secondYearlyMonthlyCo2Dict[float(validMonthlyYears[i])])
df4 = pan.DataFrame(data = scatterplotPersonalizedYearlyMonthlyCo2Dict)
barGraphPersonalizedAveragedCo2Dict = {'Years': personalizedYears, 'Co2': []}
for i in range(len(personalizedYears)):
  barGraphPersonalizedAveragedCo2Dict['Co2'].append(yearlyAverageCo2Dict[personalizedYears[i]])
df5 = pan.DataFrame(data = barGraphPersonalizedAveragedCo2Dict)
boxPlotPersonalizedAveragedCo2Dict = {'Years': [], 'Co2': []}
for j in range(len(personalizedYears)):
  for i in range(len(yearlyCo2Dict[personalizedYears[j]])):
    boxPlotPersonalizedAveragedCo2Dict['Years'].append(personalizedYears[j])
    boxPlotPersonalizedAveragedCo2Dict['Co2'].append(yearlyCo2Dict[personalizedYears[j]][i])
df6 = pan.DataFrame(data = boxPlotPersonalizedAveragedCo2Dict)
lineplotVariatingYearlyMonthlyCo2Dict = {'Years': validMonthlyYears, 'Co2': []}
for i in range(len(validMonthlyYears)):
  lineplotVariatingYearlyMonthlyCo2Dict['Co2'].append(variatingYearlyMonthlyCo2Dict[validMonthlyYears[i]])
df7 = pan.DataFrame(data = lineplotVariatingYearlyMonthlyCo2Dict)





#All code responsible for plotting
Co2AvgLevelsLineplot = sns.lineplot(x = 'Years', y = 'Co2', data = df)
Co2AvgLevelsLineplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2AvgLevelsLineplot.png')
plt.clf()
Co2LevelsScatterplot = sns.scatterplot(x = 'Years', y = 'Co2', data = df2)
Co2LevelsScatterplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2LevelsScatterplot.png')
plt.clf()
Co2PersonalizedAvgLevelsLineplot = sns.lineplot(x = 'Years', y = 'Co2', data = df3)
Co2PersonalizedAvgLevelsLineplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedAvgLevelsLineplot.png')
plt.clf()
Co2LevelsPersonalizedScatterplot = sns.scatterplot(x = 'Years', y = 'Co2', data = df4)
Co2LevelsPersonalizedScatterplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedLevelsScatterplot.png')
plt.clf()
Co2LevelsPersonalizedBarplot = sns.barplot(x = 'Years', y = 'Co2', data = df5)
Co2LevelsPersonalizedBarplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Averaged', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2PersonalizedLevelsBarplot.png')
plt.clf()
Co2LevelsBoxplot = sns.boxplot(x = 'Years', y = 'Co2', data = df6)
Co2LevelsBoxplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2LevelsBoxplot.png')
plt.clf()
Co2VariatingLevelsLineplot = sns.lineplot(x = 'Years', y = 'Co2', data = df7)
Co2VariatingLevelsLineplot.set(title = 'Years Vs. Carbon Dioxide in ppm at Mauna Loa Observatory Variability', ylabel = "Co2", xlabel = "Years")
plt.savefig('Co2VariatingLevelsLineplot.png')
plt.clf()





#Printing the key
print('Key in ppm of carbon dioxide levels:\n  <450 = Best\n  450-700 = Great\n  700-1000 = Okay\n  1000-2500 = Bad\n  2500-5000 = Horrible\n  >5000 = Intolerable')





#Printing the instructions
print('Analysis:\n  From the data in "Co2AvgLevelsLineplot.png" and "Co2LevelsScatterplot.png" I observed that there is a positive trend between the years and the co2 levels. The difference between "Co2AvgLevelsLineplot.png" and "Co2LevelsScatterplot.png" is that in "Co2LevelsScatterplot.png", the data is more spread out but the analysis is the same.\n  In "Co2PersonalizedAvgLevelsLineplot.png" and "Co2PersonalizedLevelsScatterplot.png", the data can be adjusted to your favor, focusing on the part you want to see.\n  In "Co2PersonalizedLevelsBarplot.png"')





#If you forget to close the file then your code will mess up
f.close()





#To-Do:
#Analysis
#Presentation