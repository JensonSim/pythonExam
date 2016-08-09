import os
import platform
import time
now = time.localtime()
t = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

sysLog = open("C:/Users/JBM/AppData/Local/ICIDO/IDOSystem/Temp/sysLog.log", "r")
Report = open("c:/users/jbm/desktop/testEx.txt","w")
logData = ""
for a in sysLog:
	logData = logData+a
error_log = open("C:/Users/JBM/AppData/Local/ICIDO/IDOSystem/Temp/error.log", "r")

logData = logData+"----------- Error.log --------------"
for a in error_log:
	logData = logData+a



sysLog.close()
error_log.close()

Report.write(t)
Report.write(str(platform.win32_ver(release='', version='', csd='', ptype='')))
Report.write(logData)

Report.close()
