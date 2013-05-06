import os
from os.path import isfile, join, getsize
import pprint
import datetime
import time

'''
Gathers all the entries based on the directory
'''
entryLocation = '/Users/kellyhays/Dropbox/Notes/work/'
entries = os.listdir(entryLocation)

class entry(object):
    def __init__(self, filename):
        self.filename = filename

    def date(self):
        d = self.filename.split('-')[0:3]
        return d
            
    def project(self):
        p = self.filename.split('-')
        pclean = str(p[3:4])[2:][:-2].title().replace('_', ' ')
        return pclean

    def topic(self):
        t = self.filename.split('-')
        tclean =  str(t[4:5])[2:][:-2].title().replace('_', ' ')
        return tclean

allEntries = []

for e in entries:
    if ".md" in e:
        f = entry(e)
        allEntries.append([f.date(), f.project(), f.topic()])

printdate = ''
for line in allEntries:
    year = line[0][0]
    month = line[0][1]
    day = line[0][2]
    noteDate = int(year), int(month), int(day), 0, 0, 0, 0, 0, 0
    #TODO make the day of the week work, which requires noteDate to have a read date
    d = time.strftime('%B %d, %Y', noteDate)

    if noteDate == printdate:
        print line[1], ' - ', line[2]
    else:
        print '##', d
        printdate = noteDate
        print line[1], ' - ', line[2]

    



