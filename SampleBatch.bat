@echo off
start python ConnectToDB.py -g 50072 -s "prf01cavsmtp01" -q 1
pause
start python ConnectToDB.py -g 50073 -s "prf01cavsmtp01" -q 1
pause
start python ConnectToDB.py -g 50074 -s "prf01cavsmtp01" -q 1
pause