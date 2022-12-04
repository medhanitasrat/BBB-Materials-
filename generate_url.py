import urllib
from urllib.request import urlopen
from googlesearch import search
import requests
from tldextract import tldextract
import ssl


def appends(company_name, tld, url=[]):
    '''
    A funtion that appends company name to a general URL format

    :param company_name: The name of the company
    :param tld: top level domains
    :param url: the list to store urls
    :return: appended Urls
    '''
    url = []
    company_name = clean_data(company_name)
    for i in tld:
        urls = "https://www." + company_name + i
        if validURl(urls):
            url.append(urls)
    return url


def clean_data(companyName):
    '''
    A function that cleans companyName(changes to lowercase, and all remove all white spaces as well as remove any legal
    designation eg: ',LLC'

    :param companyName: The name of the company
    :return: The name of the company after being cleaned
    '''
    companyName = companyName.split(',')[0]
    companyName = companyName.lower()
    companyName = companyName.replace(" ", "")
    return companyName


def validURl(url):
    '''
    A function that checks if found url is valid

    :param url: The url
    :return: True if the url is valid, false otherwise
    '''
    s = status_code(url)
    if s != 404 and s != -1:
        return True
    else:
        return False


def getURL(company_name, Url, rating_sites):
    """
    Return company's URL given company name

    :param companyName: the name of the company
    :param Url: a list where URL is stored

    :return: company's URL if found, else return ''
    """
    try:

        term = ' '.join([company_name])
        for j in search(term, num=10, stop=10, pause=2):
            if filter(j, rating_sites):
                Url.append(j)
        return Url
    except:
        return ''


def filter(url, rating_sites):
    """
    A function that checks if found url are rating sites

    :param url: the url
    :param rating_sites: list of any known rating sites
    :return: True if url is a not a rating site, false otherwise
    """
    sub = tldextract.extract(url)
    # print("Subdomain ", sub.domain)
    for i in rating_sites:
        if sub.domain.lower() == i:
            return False
    return True


def status_code(url):
    """
    Gets a single url and returns the status code

    :param url: a single url
    :return: status code of the url if it receives a response within the given time, if not returns -1
    """

    try:
        r = requests.get(url, verify=True, timeout=5)
        return r.status_code
    except:
        return -1


def scrap(url, companyName, words):
    """
    Scrapes website and checks if any of the company information exists within the website
    Adds one to count whenever an information is found within a website except if that information is company name,
    if that's the case then adds 3 to count

    :param url: The url
    :param companyName: The company name
    :param words: list of company information ( company name, email, phone number, state, city, address)
    :return: the amount of how many contents in the database were found in the site
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    count = 0
    try:
        site = urllib.request.urlopen(url).read().decode("utf-8")


    except:
        return 3
    else:
        for word in words:
            word = str(word)
            if word in site:
                if word == companyName:
                    count += 3
                else:
                    count += 1
            else:
                count = count
        return count


def correctUrl(url, company_name, info):
    """
    A function that picks the url with the most count out of the list of potential urls passed

    :param url: the list of potential urls
    :param company_name: the name of the company
    :param info: company information
    :return: the correct url or empty space of url not found
    """
    maxnum = -1
    curl = ""
    for i in url:
        n = scrap(i, company_name, info)
        if n > maxnum:
            maxnum = n
            curl = i

    if maxnum >= 3:
        return curl
    else:
        return ""


def company_URL(information):
    """
    A function that gets the correct url utilizing all the functions above

    :param information: company information
    :return: the correct url
    """
    tld = ['.com', '.org', '.net', '.int', '.edu', '.gov', '.mil']
    rating_sites = ['mapquest', 'yelp', 'bbb', 'podium', 'porch', 'chamberofcommerce', 'angi']
    companyName = information[0]
    potentialUrl = appends(companyName, tld)
    if potentialUrl:
        return str(potentialUrl[0])
    else:
        potentialUrl = getURL(companyName, potentialUrl, rating_sites)
        url = correctUrl(potentialUrl, companyName, information)

        return url

