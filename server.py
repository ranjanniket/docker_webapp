#!/usr/bin/python3
import cgi
import subprocess

print("content-type:text/html")
print()

#x = "niket"

mydata = cgi.FieldStorage()
op = mydata.getvalue("x")

output = subprocess.getoutput("sudo " + op)

print(output)

#sub = subprocess.getoutput("cal")

#print(sub)

