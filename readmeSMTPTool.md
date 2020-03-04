### Initial Configuration

1. Install python
2. Download and install SMTPTool and unzip in the folder SMTPTool
3. Change directory to SMTPTool
4. Install python packages by executing following commands:

```
$pip install markovify
$pip install textblob
$pip install tzlocal
$pip install pyodbc
```

5. Open Visual Studio Installer
6. Select the associated VS and click on modify
7. Install Python development component

***

### Executing the Tool

1. Right click and open the batch file SampleBatch.bat

SAMPLE TEXT
```
@echo off
start cmd.exe /K python ConnectToDB.py -g 50072 -s "prf01cavsmtp01" -q 1
start cmd.exe /K python ConnectToDB.py -g 50073 -s "prf01cavsmtp01" -q 1
start cmd.exe /K python ConnectToDB.py -g 50074 -s "prf01cavsmtp01" -q 1
```

2. Meaning of flags 

```
-g                                                     GroupID
-s                                                     SMTPServer to be used to exchange mail
-q                                                     Quantity of mails to be exchanged
```

3. Provide the group number, smtpServer and quantity of mails to be generated and update the text file and save

4. To execute, just double click the .bat file and this should open multiple windows(depending on number of groups provided) and mail data generation is started

NOTE: This tool has been configured to work in a windows environment only