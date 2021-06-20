![logo2](https://user-images.githubusercontent.com/33743193/122555900-2bb71a00-d03b-11eb-8b01-92e194bd4d86.png)

## Data Logger

This is a created class for functinal data logging.

* Creating logger files with definitive time stamp.
* Adding types of logging data inside the txt file.
* CSV format logging can be implemented together with timestamp row.
* Text logger can be implemented for any message that is wanted to be stored with timestamps.

### Used external modules
1. [Datetime Module / import datetime](https://docs.python.org/3/library/datetime.html)
2. [CSV Module / import sys](https://docs.python.org/3/library/csv.html)
3. [Time Module / import sys](https://docs.python.org/3/library/time.html)
4. [Random Module / import sys](https://docs.python.org/3/library/random.html)

### Avaliable logging options
1. CSV type logging from list type dataframe, with time stamps
2. Text type data logging for any type of data that is stored inside text file with time stamps.


__Note__: For both logging txt format has been used. Extension of the file can be changed. With txt, it can be opened while logging without permission crash!

---
### Code and Syntax

> It must has datetime, csv, time, random modules with `import datetime, csv, time, random`

```python
import datetime
import csv
import time
import random
```
> After than that, necessary data types has been added for testing of the code. That is why we also have time and random modules.

```python
dataFrame = ['First Data', 'Second Data', 'Third Data']
# Crete a dataframe that you want to log into csv file

txtFrame = "That can be any string to log!"
# Any type of variable can be pushed to log into txt file
```

> First class is being created which is csvDataLogger for csv format logging together with time stamp (TimeStamp, Data1, Data2 ...).

```python
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

```
> Second class which is txtDataLogger is being created for any type of message together with time stamp. 

```python
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
        timeStamp = time.strftime('%d-%m-%Y %H:%M:%S')
        txtMessage = f'{timeStamp}: {message} \n'
        txtFile = open(self.finalName, 'a')
        txtFile.write(txtMessage)
        txtFile.close()
        return txtMessage
```
> Any of the classes and their methods can be called for usage together with proper given arguments.

> As final test implementation, `if __name__ == '__main__':` has been added to test each functinallty.

```python
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

```

> `random.randint(0, 100)` has been used to genera random values in the range of 0 to 100. <br /> 
> And when you run the code, output will be like; <br />
> For csv file MyCSV 20_06_2021-01_55_59  <br />

> TimeStamp,First Data,Second Data,Third Data <br />
> 20-06-2021 01:55:59,17,87,27 <br />
> 20-06-2021 01:55:59,60,61,94 <br />
> 20-06-2021 01:56:00,89,48,46 <br />
> 20-06-2021 01:56:00,1,2,46 <br />
> 20-06-2021 01:56:01,84,23,86 <br />
> 20-06-2021 01:56:01,23,54,5 <br />

> For text file MyTXT 20_06_2021-01_55_59 <br />
20-06-2021 01:55:59: That can be any string to log! <br />
20-06-2021 01:55:59: That can be any string to log! <br />
20-06-2021 01:56:00: That can be any string to log! <br /> 
20-06-2021 01:56:00: That can be any string to log! <br /> 
20-06-2021 01:56:01: That can be any string to log! <br />
20-06-2021 01:56:01: That can be any string to log! <br /> 
20-06-2021 01:56:02: That can be any string to log! <br /> 

__Note__: All files are generated as txt for main logging. CSV logs as csv format. 
Idea is preventing PermissionError: [Errno 13] that comes from interrupting file while system is running.
