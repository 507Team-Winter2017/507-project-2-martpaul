#proj2.py
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
def problem1():
    nyt_headlines = []

    nyt_url = 'http://www.nytimes.com'
    nyt_html = urlopen(nyt_url, context=ctx).read()

    nyt_soup = BeautifulSoup(nyt_html, 'html.parser')

    story_head = nyt_soup.find_all(class_ = "story-heading")

    for x in story_head:
        if x.a:
            nyt_headlines.append(((x.a.text).strip()))
        else:
            nyt_headlines.append(((x.contents[0]).strip()))

    nyt_headlines = nyt_headlines[:10]
    for x in nyt_headlines:
        print (x)

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
def problem2():
    md_headlines = []
    il = []

    md_url = "https://www.michigandaily.com/"
    md_html = urlopen(md_url, context = ctx).read()

    md_soup = BeautifulSoup(md_html, 'html.parser')

    item_list = md_soup.find_all(class_ = "item-list")

    for x in item_list:
        x = (x.get_text()).strip()
        il.append(x)

    most_read = il[-1:]
    for x in most_read:
        print (x)

#### Problem 3 ####
print('\n*********** PROBLEMbase 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
def problem3():

    alt_text = []
    alt_url = "http://newmantaylor.com/gallery.html"
    alt_html = urlopen(alt_url, context = ctx).read()
    alt_soup = BeautifulSoup(alt_html, 'html.parser')

    body = (alt_soup.body)

    alt_list = body.find_all("img")

    for x in alt_list:
        #print (x.attrs)
        if "alt" in x.attrs:
            at = x.attrs["alt"]
            alt_text.append(at)
        else:
            at = "No alternative text provided!!"
            alt_text.append(at)

    for x in alt_text:
        print (x)

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
def problem4():

    email_lst = []
    dir_pages = []
    num = 1;

    dir_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
    req = urllib.request.Request(dir_url, None, {'User-Agent': 'SI_CLASS'})
    dir_test = urllib.request.urlopen(req, context = ctx)
    #print (dir_test)

    last_url = ''
    dir_pages.append(dir_url)

    for i in range(5):
        req = urllib.request.Request(dir_url, None, {'User-Agent': 'SI_CLASS'})

        dir_html = urllib.request.urlopen(req, context = ctx)
        #dir_html = urlopen(dir_url, context = ctx).read()
        dir_soup = BeautifulSoup(dir_html, 'html.parser')
        #print (dir_soup)

        next_link = dir_soup.find_all("a", title = "Go to next page")
        print (next_link)
        for x in next_link:

            dir_url = "https://www.si.umich.edu" + x.attrs["href"]
            dir_pages.append(dir_url)
        #print (dir_url)
        last_link = dir_soup.find_all("a", title = "Go to previous page")

        for x in last_link:
            last_url = "https://www.si.umich.edu" + x.attrs["href"]
        #print (last_url)


    for i in dir_pages:
        print (i)
        i_req = urllib.request.Request(i, None, {'User-Agent': 'SI_CLASS'})
        i_html = urllib.request.urlopen(i_req, context = ctx)
        #i_html = urlopen(i, context = ctx).read()
        i_soup = BeautifulSoup(i_html, 'html.parser')

        a_tags = i_soup.find_all("a")

        for x in a_tags:
            if x.get_text() == "Contact Details":
                href =  x.attrs["href"]
                base_url = "https://www.si.umich.edu"
                contact_url = base_url + href

                contact_req = urllib.request.Request(contact_url, None, {'User-Agent': 'SI_CLASS'})
                contact_html = urllib.request.urlopen(contact_req, context = ctx)
                #contact_html = urlopen(contact_url, context = ctx).read()
                contact_soup = BeautifulSoup(contact_html, 'html.parser')

                email = contact_soup.find(string = re.compile("@umich.edu"))
                email = str(num) + " " + email

                email_lst.append(email)
                num += 1

    for x in email_lst:
        print (x)

problem1()
problem2()
problem3()
problem4()
