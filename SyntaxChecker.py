import re
from urllib.parse import urlparse


def check_syntax(url):
    """
    A function that checks if the url matches the general syntax of URL.
    It includes two possible regular expressions, one for URLs that start with http/https and one for URLs that don't.
    :param url: The URL bring checked
    :return: returns true if the passed url matches the both of the expected pattern and false otherwise
    """

    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern1 = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    if re.match(url_pattern, url) is None and re.match(url_pattern1, url) is None:
        return False
    else:
        return True


def fix(url):
    """
    This function tries to correct the syntax of a URL.
    It utilizes re to fix some errors that are detected within the URL.
    :param url: url to be fixed
    :return: The new url with the correct syntax
    """
    if re.match('[-a-zA-Z0-9]$', url[-1]) is None:  # get rid of special characters at the end of URLs
        url = url[:-1]

    url = re.sub('[;,]|(:(?!//))', '.', url)  # change any [;:,] to '.' in URL

    domain = urlparse(url).netloc  # extracts the domain for fixing errors in the domain

    domain = re.sub('(?<!\.)((?=com$)|(?=net$)|(?=org$)|(?=edu$)|(?=gov$))', '.',
                    domain)  # add '.' before top level domains if there aren't any

    if urlparse(url).scheme:
        url = urlparse(url).scheme + "://" + domain + urlparse(url).path + urlparse(url).params + urlparse(
            url).query + urlparse(url).fragment
    else:
        url = domain + urlparse(url).path + urlparse(url).params + urlparse(url).query + urlparse(url).fragment

    return url


def verify(url):
    """
    This method checks if the URLs that have gone through the fixing process have actually been fixed.
    It first checks if the URL is valid, if not it tries to fix it and checks if it actually has been fixed
    :param url: the URL being verified
    :return: returns true and the url if the URL is valid in the first place, returns true and the fixed url if the url
             has been fixed and is now valid, and returns false and the url if the fixing process didn't work and the
             url is invalid.
    """
    if check_syntax(url):
        return True, url
    else:
        fixed_url = fix(url)
        if check_syntax(fixed_url):
            return True, fixed_url
        else:
            return False, url
