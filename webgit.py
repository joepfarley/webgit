#!/usr/bin/env python
#  webgit.py
#  A simple CGI handler for working with git on the web. 
#  Currently it only supports auto commiting.   
#  Features included
#   *can request status
#   *can add customer commit message in address bar
#   *can view log
#  
#   test etste
#  Note: Make sure to set this file as executable or your web
#        server will not run it! On *nix you could do this by
#        running: `chmod +x webgit.py`

import math
import cgitb
import sys
import commands
import os

cgitb.enable()

print "Content-Type: text/html;charset=utf-8"
print 

def css():
    print """<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
        h1 { color: #9999ff; background-color: #000000 fontsize:1em;}
        body { color: #ffffff; background-color: #000000; }
        span {font-size: smaller;}
        
    ul.topBar        		{
    	background: #9999ff;
    	padding:0 5px;
    	font-size:13px;
    	color:#000000;
    	overflow:hidden;
        position: relative;
    	background:#9999ff);
    }
    ul.topBar li	{
    	float:right;
    	padding:7px 8px;
        list-style-type: none;
    }
    ul.topBar li:hover	{
    	background:#e4ebf8;

    }
    /*]]>*/--></style>
    
    """
    
def headers():
    print"""
    <html>
    <head><title>Web Git Client</title></head>
    
    <script language="Javascript">
    //--></script>
    
    <body>
    <ul class="topBar">
        <li><a class="button" href='javascript:s = prompt("Enter a commit message",""); location = ("?commit+" + s);'>commit</a></li>
    	<li><a href='?status'>status</a></li>
    	<li><a href='?log'>log</a></li>
    </ul>
    """

def startpage():
    print"""
        <h1>WebGit</h1>
        <p1>This page is a tool that, when installed in an ownclowd directory with cgi enabled you may preform many functions using Git.
        Just click on the links in the upper right to preform an action. 
        If this tool doesn't work please ensure the following. </p>
        <ul>
            <li>CGI is enabled on this directory. Ask the admin if you don't manage the server, they may say no, because it is inherently insecure</li>
            <li>This file along with the .git directory are owned by the www user for the server</li>
            <li>This file is executable</li>
            <li>git is installed</li>
            <li>Python 2.7 is installed</li>
        </ul>
    """
    if ".git" not in os.listdir("."):
        print """<h1>No Git repository</H1>
        <p1>There is no Git repository in this directory.Click <a href=?init>here</a> if you'd like to add one.</p1>
        """



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
    

def gitinit():
    if ".git" in os.listdir("."):
        print "<p>A git repository has already been created in this directory.<p>"
    else:
        print(commands.getoutput("git init"))

def gitpush():
    print(commands.getoutput("git config --global http.sslVerify false"))
    print(commands.getoutput("git push -u origin master"))

css()
headers()
startpage()

try:
    if sys.argv[1]=="commit":
        commit(sys.argv[-1])
    if sys.argv[1]=="init":
        print "<ul>"
        gitinit()
        print "</ul>"
    if sys.argv[1]=="status":
        status()
    if sys.argv[1]=="log":
        log()
    if sys.argv[1]=="push":
        gitpush()
except IndexError:pass

print "</body></html>"
    
    
    
    