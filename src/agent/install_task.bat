:: Coded by yuangezhizao

@echo off
if exist "%SystemRoot%\SysWOW64" path %path%;%windir%\SysNative;%SystemRoot%\SysWOW64;%~dp0
bcdedit >nul
if '%errorlevel%' NEQ '0' (goto UACPrompt) else (goto UACAdmin)
:UACPrompt
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
exit /B
:UACAdmin
cd /d "%~dp0"

echo -------------------------------------------------------------------
echo                device_manager_report Agent V1.0.0
echo         Copyright (c) 2021 ALSI ES.  All rights reserved.
echo -------------------------------------------------------------------

xcopy /y /i "%~dp0*.*" "C:\Program Files\ALSI ES"

::schtasks /delete /TN device_manager_report
schtasks /create /sc minute /mo 10 /tn device_manager_report /tr "C:\Program Files\ALSI ES\device_manager_report.exe"
schtasks /query /TN device_manager_report

@pause