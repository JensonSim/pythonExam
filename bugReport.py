import os
import platform
import time
import math


def convertSize(size):
   if (size == 0):
       return '0B'
   size_name = ("Byte","KB", "MB", "GB", "TB", "PB", "EB", "ZB" )
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   return '%s %s' % (s,size_name[i])

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


now = time.localtime()
t = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

sysLog = open("C:/Users/"+os.getlogin()+"/AppData/Local/ICIDO/IDOSystem/Temp/sysLog.log", "r")
Report = open("c:/users/"+os.getlogin()+"/desktop/"+str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+str(now.tm_hour)+str(now.tm_min)+".txt","w")


logData = ""
for a in sysLog:
	logData = logData+a
	b=""
	if a.startswith("Log: (Level 05) [    Reading session from") == True:
		b = a.split("'")
		print (b[1])
		idoPath = b[1]
		c = idoPath.rsplit('/',1)
		print (c)
		fPath = c[0]
	elif a.startswith("Log: (Level 05) [OpenGL renderer string  :") == True:
		d = a.rsplit(':')
		gcName = d[2]

	elif a.startswith("Log: (Level 05) [OpenGL version string   :")== True:
		e = a.rsplit(':')
		gcVersion = e[2]


#mfTime ="last used: %s" % time.ctime(os.path.getmtime("C:/Users/"+os.getlogin()+"/AppData/Local/ICIDO/IDOSystem/Temp/sysLog.log")) 
mfTime ="last used: %s" % time.ctime(os.path.getmtime("C:/Users/"+os.getlogin()+"/AppData/Local/ICIDO/IDOSystem/Temp/sysLog.log"))

#print (mfTime)
#print ("created: %s" % time.ctime(os.path.getctime("C:/Users/"+os.getlogin()+"/AppData/Local/ICIDO/IDOSystem/Temp/sysLog.log")))

error_log = open("C:/Users/"+os.getlogin()+"/AppData/Local/ICIDO/IDOSystem/Temp/error.log", "r")

logData = logData+"----------- Error.log --------------"
for a in error_log:
	logData = logData+a



userName = str(os.getlogin())
machineName = str(platform.node())
idoSize = os.path.getsize(idoPath)

print (convertSize(get_size(fPath)))



sysLog.close()
error_log.close()

Report.write("Reported: "+t+"\n")
Report.write(mfTime+"\n")

Report.write("User name = "+userName+"\n")
Report.write("MachineName = "+machineName+"\n")

if len(gcName) !=0:
	Report.write("[Graphic card: "+gcName)
if len(gcVersion) !=0:
	Report.write("[Graphic version: "+gcVersion)
if len(idoPath) !="":
	Report.write("Used Session file = "+idoPath+"\n")
if idoSize !=0:
	Report.write("  IdoSize = "+convertSize(idoSize)+"\n")
if fPath !="":
	Report.write("  FolderSize = "+convertSize(get_size(fPath))+"\n")


"""
Report.write(str(platform.system()))
Report.write(str(platform.processor()))
Report.write(str(platform.win32_ver(release='', version='', csd='', ptype='')))
"""
Report.write(logData)



Report.close()

"""close_written file"""




#!/usr/bin/python
"""
import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

"""
#message = """
#From: From Person <from@fromdomain.com>
#To: To Person <to@todomain.com>
#Subject: SMTP e-mail test

#This is a test e-mail message.



"""
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
"""

