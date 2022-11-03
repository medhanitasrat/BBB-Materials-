# BBB URL Testing Environment

This tool deliverable consists of the implementation of an experiment and test environment that accesses client data and tests and records findings.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.


[csv](https://pypi.org/project/python-csv/) - to read the .csv files  

[re](https://pypi.org/project/re2/) – regular expressions to check if a URL matches a pattern

[urlparse](https://pypi.org/project/urlparse4/) from [urllib.parse](https://pypi.org/project/pycopy-urllib.parse/) – to process URLs, and to convert between URLs and platform-specific filenames

[request](https://pypi.org/project/requests/) - to send HTTP requests using a Python code to get the status code of the URLs

[ThreadPoolExecutorPlus](https://pypi.org/project/ThreadPoolExecutorPlus/) - to send a thread of HTTP requests

[repeat](https://pypi.org/project/repeat/) from [intertools](https://docs.python.org/3/library/itertools.html) - repeat the elements of the URLs in the list and the header to perform threading


## Usage

Install the above packages to run the program.

On **URLVerification.py** add the base directory and file name on lines 7 and 16 respectively
```bash
 7  base_dir = 'Enter the base directory here(where the file you want to read is located/where you want to write the new file)'
.
.
.
.
.
16  file_name = 'Enter the file name if the file you want to read here'
```



## Collaborators
Wengel Tsegaselassie - Team Lead



Wen Sun - Testing Lead



Mohammed Ahnaf Khalil - Documentation Lead



Medhanit Asrat Bekele - Lead Analyst
