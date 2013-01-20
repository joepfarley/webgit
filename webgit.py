#!/usr/bin/env python
#  webgit.py
#  A simple CGI handler for working with git on the web. 
#  Currently it only supports auto commiting.   
#  Features included
#   *can request status
#   *can add customer commit message in address bar
#   *can view log
#
#
#
#
#  Note: Make sure to set this file as executable or your web
#        server will not run it! On *nix you could do this by
#        running: `chmod +x comment.py`

import math
import cgitb
import sys
import commands
import os

cgitb.enable()
print "Content-Type: text/html;charset=utf-8"
print 


print """<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
    h1 { color: #9999ff; background-color: #000000 fontsize:2em;}
    body { color: #ffffff; background-color: #000000; }
    a:link { color: #0000CC; }
    p, address {margin-left: 2em;}
    span {font-size: smaller;}
/*]]>*/--></style>"""
print "<head><title>Web Git Client</title></head>"

def startpage():
    print"""<pre>
    You haven't entered any arguments in the address bar. 
    Eventually this will be an actual disigned page with real content. 
    For now here's some instructions
    * after the address bar type a question mark (?) and then the word commit followed by a plus sign (+). 
    * Next write in the commit message. No special formatting required. 
    <pre>"""



def status():
    print "<h1>Status Page</h1><pre>"
    print "</br>"
    print commands.getoutput("git status")
    print "<h1>Diff</h1><xmp>"
    print commands.getoutput("git diff")
    print "</xmp></pre>"



def log():
    print "<h1>Log Page</h1><pre>"
    print "</br><xmp>"
    print commands.getoutput("git log")
    print "</xmp></pre>"



def commit(x="auto commit from web"):
    print 
    print "<head><title>Webgit.py</title><head><body>"
    print "<p>"
    print "<h1>Status</h1><pre>"
    print commands.getoutput("git status")
    print "</pre></br>"
    print "<h1>Diff</h1><pre><xmp>"
    print commands.getoutput("git diff")
    print "</xmp></pre></br>"
    print "<h1>Add</h1><pre>"
    print commands.getoutput("git add --all")
    print "</pre></br>"
    print "<h1>Commit</h1><pre>"
    try:
        commitMessageStr = str("git commit -m '%s'")%x
        print(commands.getoutput(commitMessageStr))
    except TypeError:
        print(commands.getoutput("git commit -m 'auto commit from web'"))
    print "</pre></p>"
    print "</body>"

def gitinit():
    if ".git" in os.listdir("."):
        print "<p>A git repository has already been created in this directory.<p>"
    else:
        print(commands.getoutput("git init"))

try:
    if sys.argv[1]=="commit":commit(sys.argv[-1])
    if sys.argv[1]=="init":
        print "<ul>"
        gitinit()
        print "</ul>"
    if sys.argv[1]=="status":status()
    if sys.argv[1]=="log":log()
except IndexError:
    startpage()

    
    
    
    
    