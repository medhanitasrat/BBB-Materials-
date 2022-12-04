# BBB Core algorithm

This tool deliverable consists of core algorithm that solves specific data quality issues.
The core algorithm contains three python scripts (AddUrl.py, badUrls.py, generate_url.py). More details are available on a sphinx documentation. 

## Accessing Sphinx Documentation

1) Go to the html folder (You might need to download the folder on your device before opening it)
2) Click on index.html
     * All the information about each function and module is available on this page.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.

For example to install pandas type in the folllowing command:

```bash
pip install pandas
```

[csv](https://pypi.org/project/python-csv/) - to read the .csv files  

[pandas](https://pypi.org/project/pandas/) - to load csv files into a data frame  

[urllib](https://pypi.org/project/urllib3/) - to scrap website

[from googlesearch import search](https://pypi.org/project/google-search/) - to search the web for potential urls

[request](https://pypi.org/project/requests/) - to send HTTP requests using a Python code to get the status code of the URLs

[tldextract](https://pypi.org/project/tldextract/)- to extract subdomain from URL

[ssl](https://pypi.org/project/ssl/)- this module provides access to Transport Layer Security

_For further description on those packages, click on the package name._ 


## Usage

Install the above packages to run the program.

First run the badUrls.py to extract companies with broken URLs and companies that don't have URLs in the data base and writes them into a new csv file. 

Once you have the csv file containing broken URLs and no URLs, run AddUrl.py, which will utilize generate_url.py to get the potential company URL and appends it into a new csv file.
_Make sure to replace all file directories and file names to your convenience_ 


## Collaborators
Wengel Tsegaselassie - Team Lead



Wen Sun - Testing Lead



Mohammed Ahnaf Khalil - Documentation Lead



Medhanit Asrat Bekele - Lead Analyst
