@echo off

set yy=%DATE:~0,4%
set mm=%DATE:~5,2%
set dd=%DATE:~8,2%

::前一天的日期，格式化输出
echo Wscript.echo dateadd("d",-1,date)>vbs.vbs
for /f %%a in ('cscript //nologo vbs.vbs') do del vbs.vbs&&set yyyymmdd=%%a
for /f "tokens=1,2,3* delims=// " %%i in ('echo %yyyymmdd%') do set yyyy=%%i&set mm=%%j&set dd=%%k
::if   %mm%   LSS   9   set   mm=0%mm%
::if   %dd%   LSS   9   set   dd=0%dd%

echo "D:\Apache24\htdocs\device_manager\backup\%yyyy%%mm%%dd%"

xcopy /y /i "D:\Apache24\htdocs\device_manager\device_manger.db" "D:\Apache24\htdocs\device_manager\backup\%yyyy%%mm%%dd%\"

:: schtasks /create /sc daily /st 00:00 /tn backup_db /tr "D:\Apache24\htdocs\device_manager\backup_db.bat"