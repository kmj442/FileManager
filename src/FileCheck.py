import sys
import csv
import datetime
import glob

class FileManager():
    date = datetime.datetime.strftime(datetime.datetime.now(),'%m-%d-%Y %H:%M:%S')
    location = 'D:\\Test\\'
    csvfile = 'manager.csv'
    
    def __init__(self):
        f = glob.glob(self.location+'*.csv')
        if self.csvfile in f:
            self.csv_read()
        else:
            self.csv_create()
        
    
    def checkdates(self,lastdate):
        pass
    
    def csv_create(self):
        file = open('DateManager.csv','wb')
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(self.date)
            
    
    def csv_read(self):
        csv_l = list()
        with open(self.csvfile,'rb') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                csv_l.append(row)
                
    def csv_append(self):
        with open(self.csvfile,'wb') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(self.date)
            
    
    
    
    