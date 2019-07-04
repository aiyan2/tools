@echo off
SET DIR=%~dp0%
SET ARGS=%*
@echo on

set PROXY_VM= -x 172.18.43.64:8080 -k 
set PROXY_100D= -x 172.18.43.202:8080 -k

set SERVER= https://172.18.43.21
echo " start.."%PROXY_VM%  "%PROXY_100D%



:start

REM dir v:
REM dir z:
REM more v:\test.bat

curl %PROXY_VM% %SERVER% 
curl %PROXY_100D% %SERVER%

timeout 1 
goto start
