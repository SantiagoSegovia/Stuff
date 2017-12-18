@echo off
set argC=0
set zero=0
for %%x in (%*) do Set /A argC+=1

if "%argC%" == "%zero%" (
    	set path="."
) ELSE (
	set path=%1
)
cd %path%
if exist "*.log"\ (
	del /f /q *.log
)
if exist "*.pyc"\ (
	del /f /q *.pyc
)
if exist "*.txt"\ (
	del /f /q *.txt
)
