"""
This is created for data logging!
You can select your data as list that you need log!
Data list can be updated and logged to created file as csv or text!
version 0.0.1
@keklikyusuf
"""

import datetime
import csv
import time
import random

dataFrame = ['First Data', 'Second Data', 'Third Data']
# Crete a dataframe that you want to log into csv file

txtFrame = "That can be any string to log!"
# Any type of variable can be pushed to log into txt file


class csvDataLogger:
    """
    It has been created to log CSV data type into TXT. Data can be adjusted according to user desire!
    """
    def __init__(self, fileName, dataFrame):
        """
        :param fileName: Enter desired file name for your log file. -String
        Log file is being created with that time time-stamp and closed as soon as object is being generated!
        """
        self.fileName = fileName
        self.dataFrame = dataFrame.insert(0, "TimeStamp")
        time = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
        self.finalName = f'{self.fileName} {time}.txt'
        open(f'{self.finalName}', "w+").close()

    def csvLogger(self):
        """
        :return: This function returns to data frame
        CSV file is being called to log with this method
        """
        csvFile = open(self.finalName, 'a', newline='')
        write = csv.writer(csvFile)
        write.writerow(dataFrame)
        csvFile.close()
        dataFrame[0] = time.strftime('%d-%m-%Y %H:%M:%S')
        return dataFrame


class txtDatalogger:
    """
        It has been created to log any data type into TXT as text. Data can be adjusted according to user desire!
    """

    def __init__(self, fileName):
        """
        :param fileName: Enter desired file name for your text file. -String
        """
        self.fileName = fileName
        time = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
        self.finalName = f'{self.fileName} {time}.txt'
        open(f'{self.finalName}', "w+").close()

    def txtLogger(self, message):
        """
        :param message: Text message that wanted to be loged and saved to text file
        :return: This function returns to logged text message
        Any message is being saved to created text file with this method
        """
        txtMessage = f'{message} \n'
        txtFile = open(self.finalName, 'a')
        txtFile.write(txtMessage)
        txtFile.close()
        return txtMessage


if __name__ == '__main__':
    csvLog = csvDataLogger('MyCSV', dataFrame)
    txtLog = txtDatalogger('MyTXT')
    print(csvLog.finalName)
    print(txtLog.finalName)
    while True:
        csvLog.csvLogger()
        txtLog.txtLogger(txtFrame)
        time.sleep(0.5)
        for i in range(1, len(dataFrame)):
            dataFrame[i] = random.randint(0, 100)