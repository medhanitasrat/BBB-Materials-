# BBB URL Testing Environment

This tool deliverable consists of the implementation of an experiment and test environment that accesses client data and tests and records findings.
The testing environment contains three python scripts (StatusCodeChecker.py, SyntaxChecker.py, URLVerification.py). More details are available on a sphinx documentation. 

## Accessing Sphinx Documentaion

1) Go to the html folder (You might need to download the folder on your device before opening it)
2) Click on index.html
     * All the information about each function and module is available on this page.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.

For example to install requests type in the folllowing command:

```bash
pip install requests
```

[csv](https://pypi.org/project/python-csv/) - to read the .csv files  

[re](https://pypi.org/project/re2/) – regular expressions to check if a URL matches a pattern

[urlparse](https://pypi.org/project/urlparse4/) from [urllib.parse](https://pypi.org/project/pycopy-urllib.parse/) – to process URLs, and to convert between URLs and platform-specific filenames

[request](https://pypi.org/project/requests/) - to send HTTP requests using a Python code to get the status code of the URLs

[ThreadPoolExecutorPlus](https://pypi.org/project/ThreadPoolExecutorPlus/) - to send a thread of HTTP requests

[repeat](https://pypi.org/project/repeat/) from [intertools](https://docs.python.org/3/library/itertools.html) - repeat the elements of the URLs in the list and the header to perform threading

_For further description on those packages, click on the package name._ 


## Usage

Install the above packages to run the program.
Main method is present in **URLVerification.py**, which uses funtions from **SyntaxChecker.py** and **StatusCodeChecker.py**. It reads the csv file that contains just the URLs of buisnesses and analyzes the syntax and http error of each URL and records them.

On **URLVerification.py** add the base directory and file name on lines 7 and 16 respectively
```bash
7  base_dir = 'Enter the base directory here(where the file you want to read is located/where you want to write the new file)'
.
.
.
.
.
16  file_name = 'Enter the file name of the file you want to read here'
```



## Collaborators
Wengel Tsegaselassie - Team Lead



Wen Sun - Testing Lead



Mohammed Ahnaf Khalil - Documentation Lead



Medhanit Asrat Bekele - Lead Analyst
