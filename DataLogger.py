"""
This is created for data logging!
You can select your data as list that you need log!
Data list can be updated and logged to created file!
version 0.0.1
@keklikyusuf
"""

import datetime
import csv
import time
import random

data = ['First Data', 'Second Data', 'Third Data']


class DataLogger:
    """
    It has been created to log CSV data type into TXT. Data can be adjusted according to user desire!
    """
    def __init__(self, fileName, data):
        """
        :param fileName: Enter desired file name for your log file. -String
        Log file is being created with that time time-stamp and closed as soon as object is being generated!
        """
        self.fileName = fileName
        now = datetime.datetime.now()
        time = now.strftime("%d_%m_%Y-%H_%M_%S")
        self.finalName = f'{self.fileName} {time}.txt'
        self.newfile = open(f'{self.finalName}', "w+")
        self.newfile.close()
        self.data = data

        self.data.insert(0, "TimeStamp")

    def csvLogger(self):
        """
        :param data: Data which is being logged! -List
        :return: This function returns nothing
        It opens created log file and logs it according to desired logging.
        """
        self.newfile = open(self.finalName, 'a', newline='')
        write = csv.writer(self.newfile)
        write.writerow(data)
        self.newfile.close()
        data[0] = time.strftime('%d-%m-%Y %H:%M:%S')
        return data


if __name__ == '__main__':
    Data = DataLogger('Mylog', data)
    while True:
        print(Data.finalName)
        Data.csvLogger()
        time.sleep(0.5)
        for i in range(1, len(data)):
            data[i] = random.randint(0, 100)
