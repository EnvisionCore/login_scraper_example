#Date Created: 04/12/15
#Usage: Used to scrape a website for links that end in .zip and list them
#Requirements: BeautifulSoup lib
#Notes:

import requests
from lxml import html

USERNAME = "<adam.conley>"
PASSWORD = "<AdaKun.Sione.C86>"

LOGIN_URL = "https://gplvault.com/my-account/"
URL = "https://gplvault.com/plugins/"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
   # result = session_requests.get(URL, headers = dict(referer = URL))
   # tree = html.fromstring(result.content)
   # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

   # print(bucket_names)

if __name__ == '__main__':
    mai#Author: Bellerophon_

    
    
#Date Created: 04/12/15
#Usage: Used to scrape a website for links that end in .zip and list them
#Requirements: BeautifulSoup lib
#Notes: 

import urllib2
from urllib2 import Request, urlopen, URLError
#import urllib
import os
from bs4 import BeautifulSoup

#Create a new directory to put the files into
#Get the current working directory and create a new directory in it named test
cwd = os.getcwd()
newdir = cwd +"\\test"
print "The current Working directory is " + cwd
os.mkdir( newdir, 0777);
print "Created new directory " + newdir
newfile = open('zipfiles.txt','w')
print newfile

print "Running script.. "
#Set variable for page to be open and url to be concatenated 
url = "https://gplvault.com"
page = urllib2.urlopen('https://gplvault.com/plugins/').read()

#File extension to be looked for. 
extension = ".zip"

#Use BeautifulSoup to clean up the page
soup = BeautifulSoup(page)
soup.prettify()

#Find all the links on the page that end in .zip
for anchor in soup.findAll('a', href=True):
    links = url + anchor['href']
    if links.endswith(extension):
        newfile.write(links + '\n')
newfile.close()

#Read what is saved in zipfiles.txt and output it to the user
#This is done to create presistent data 
newfile = open('zipfiles.txt', 'r')
for line in newfile:
    print line + '/n'
newfile.close()

#Read through the lines in the text file and download the zip files.
#Handle exceptions and print exceptions to the console
with open('zipfiles.txt', 'r') as url:
    for line in url:
        if line:
            try:
                ziplink = line
                #Removes the first 48 characters of the url to get the name of the file
                zipfile = line[48:]
                #Removes the last 4 characters to remove the .zip
                zipfile2 = zipfile[:3]
                print "Trying to reach " + ziplink
                response = urllib2.urlopen(ziplink)
            except URLError as e:
                if hasattr(e, 'reason'):
                    print 'We failed to reach a server.'
                    print 'Reason: ', e.reason
                    continue
                elif hasattr(e, 'code'):
                    print 'The server couldn\'t fulfill the request.'
                    print 'Error code: ', e.code
                    continue
            else:
                zipcontent = response.read()
                completeName = os.path.join(newdir, zipfile2+ ".zip")
                with open (completeName, 'w') as f:
                    print "downloading.. " + zipfile
                    f.write(zipcontent)
                    f.close()
print "Script completed"n()
