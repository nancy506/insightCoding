"""Nancy Zhang, insight coding challenge
Each line of the top_10_states.txt file should contain these fields in this order:
TOP_STATES: State where the work will take place

NUMBER_CERTIFIED_APPLICATIONS: Number of applications that have been certified for work in that state. 
An application is considered certified if it has a case status of Certified

PERCENTAGE: % of applications that have been certified in that state compared to total number of certified 
applications regardless of state.
functions:
    #get all occupations/states with certified applications and return data as a list
"""
import os
import csv
import sys

class h1b_counting(object):
    def __init__(self, inputFile):
        self.input = inputFile
        self.total = 0
        self.frequencyDicts = {}
    
    def freqCount(self, data_column):
        """read input file, calculate frequency of given data column, return to frequencyDicts[data_column]
        """
        keyword = "WORKSITE_STATE" if data_column.upper() == "STATES" else "SOC_NAME"
        keyword2 = "WORKLOC1_STATE" if data_column.upper() == "STATES" else "invalid"

        # retrieve field name from first row
        with open(self.input) as file:
            reader = csv.reader(file, delimiter=';')
            titleRow = next(reader)
        for item in titleRow:
            if "STATUS" in item.upper():
                statusRowName = item
            elif keyword in item.upper():
                dataRowName = item
            elif keyword2 in item.upper():
                dataRowName = item

        # dump every applications in a list
        all = []
        with open(self.input) as file:
            # TODO: see if csv.reader can improve speed
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                try:
                    all.append([row[statusRowName], row[dataRowName]])
                except ValueError:
                    continue

        # pick certified applications and put them in a list
        # calculate total number of certified applications
        certified = []
        for item in all:
            if item[0].upper() == "CERTIFIED":
                certified.append(item[1])
        self.total = len(certified)
        
        # calculate frequency count and put them in a dictionary, store the dict in frequencyDicts[data_column]
        d = {}
        for item in certified:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        self.frequencyDicts[data_column] = d

    def top_10(self, type, outputfile):
        """output top10 list
        prerequisite: freqcount()
        """
        items = self.frequencyDicts[type].items()
        # sort the items based on % of applications first, alphaberically if there is a tie
        sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
        # if there are fewer than 10 lines, list all of them
        length = min(10, (len(sorted_items)))
        sorted_top_10 = sorted_items[:length]
        with open(outputfile, 'w') as file:
            file.write('TOP_'+str(type).upper() +
                       ';NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
            for d, v in sorted_top_10:
                total = float(self.total)
                percentage = round(v/total*100, 1)
                file.write(str(d)+";"+str(v) + ";" + str(percentage)+"%\n")

if __name__ == "__main__":
    inputFilename = sys.argv[1]
    outputFilenames = sys.argv[2:]
    dataColumns = ["occupations", "states"]
    newCount = h1b_counting(inputFilename)
    for i in range(len(dataColumns)):
        newCount.freqCount(dataColumns[i])
        newCount.top_10(dataColumns[i], outputFilenames[i])