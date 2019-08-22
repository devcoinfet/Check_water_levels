import sys
import requests
import os
from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import requests
import types
import itertools
from lxml.html import fromstring

#https://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python
#https://stackoverflow.com/questions/2632520/what-is-the-fastest-way-to-send-100-000-http-requests-in-python




check_urls = ['.git/HEAD','robots.txt','console','manager','login','backoffice','support']

answers = []


target_list = []


def detect_shit(ourl):
    try:
       r = requests.get(ourl, allow_redirects=False, timeout=3)
       print(r.status_code,ourl)
       if "200" in str(r.status_code):
           if r.content:
              tree = fromstring(r.content)
              page_title = tree.findtext('.//title')
              print(r.status_code,ourl,page_title) 
              local_copy = {'Url':ourl,"valid hit":"True",'Content':r.text,'Status':r.status_code}
              answers.append(local_copy)
              return local_copy


       if "301"  in str(r.status_code):
          if r.content:
              answers.append(local_copy)
              local_copy = {'Url':ourl,"valid hit":"True",'Content':r.text,'Status':r.status_code}
              answers.append(local_copy)
              return local_copy


       if "302"  in str(r.status_code):
          if r.content:
              local_copy = {'Url':ourl,"valid hit":"True",'Content':r.text,'Status':r.status_code}
              answers.append(local_copy)
              return local_copy

       if "401"  in str(r.status_code):
          if r.content:
              local_copy = {'Url':ourl,"valid hit":"True",'Content':r.text,'Status':r.status_code}
              answers.append(local_copy)
              return local_copy

       if "403"  in str(r.status_code):
          if r.content:
              local_copy = {'Url':ourl,"valid hit":"True",'Content':r.text,'Status':r.status_code}
              answers.append(local_copy)
              return local_copy
    except:
        pass
 

      


def main():
    with open(sys.argv[1]) as temp_file:
       lines = [line.rstrip('\n') for line in temp_file]

    urls_list = []
    length = len(lines) -1
    print(length)
    for item in lines:
        for paths in check_urls:
            try:
               new_url = str(item.strip()) +  str(paths)
               print(new_url)
               urls_list.append(new_url)
            except:
               pass
      
    
    try:
        for urls in urls_list:
          try:
             thread = Thread(target=detect_shit, args=(urls,))
             thread.start()
             Result = thread.join()
             if Result:
                print(Result)
            
          except:
              pass
            
    except:
      pass
    

    if answers:
       print(answers)

main()
