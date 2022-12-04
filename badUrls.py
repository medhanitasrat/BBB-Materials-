import csv
import pandas as pd

base_dir = "C:/Users/Wenge/Desktop/BBB/"


def http_error(base_dir, fileName, bad_bid=[]):
    """
    A function that extracts businesses with http error

    :param base_dir: the base directory where csv is stored
    :param fileName: the name of the file we want to read
    :param bad_bid: list of business id of urls with http errors
    :return: list of business id of urls with http errors
    """
    analyzed_csv = pd.read_csv(base_dir + fileName)
    for i in range(len(analyzed_csv)):
        if analyzed_csv["status_code"][i] == 404 or analyzed_csv["status_code"][i] == -1:
            bad_bid.append(analyzed_csv["bid"][i])
    return bad_bid


def syntax_error(base_dir, fileName, bad_bid):
    """
    A function that extracts businesses with syntax error

    :param base_dir: the base directory where csv is stored
    :param fileName: the name of the file we want to read
    :param bad_bid: list of business id of urls with syntax errors
    :return: list of business id of urls with syntax errors
    """
    badsyntax = pd.read_csv(base_dir + fileName)
    for i in range(len(badsyntax)):
        bad_bid.append(badsyntax['bid'][i])
    return bad_bid


def no_Url(base_dir, fileName):
    """
    A function that extracts businesses with no urls and writes them into new csv

    :param base_dir: the base directory where csv is stored
    :param fileName: the name of the file we want to read
    """

    nourl = pd.read_csv(base_dir + fileName,
                        usecols=['BusinessID', 'BusinessName', 'StreetAddress', 'City', 'StateProvince', 'Phone',
                                 'Email', 'Website'], low_memory=False)

    binfo = ['BusinessID', 'BusinessName', 'StreetAddress', 'City', 'StateProvince', 'Phone',
             'Email']
    info = [binfo]

    for i in range(len(nourl)):
        if pd.isnull(nourl["Website"][i]):
            info.append(nourl.loc[i, nourl.columns != 'Website'])


    write(base_dir, "noUrl.csv", info)


def indentify_business(base_dir, fileName, bad_bid):
    """
    A function that identifies businesses with bad syntax or http error give their business id a writes them into a file

    :param base_dir: the base directory
    :param fileName: the file name
    :param bad_bid: list of business id of urls with http errors and syntax error
    """
    info = []
    business = pd.read_csv(base_dir + fileName, low_memory=False,
                           usecols=['BusinessID', 'BusinessName', 'StreetAddress', 'City', 'StateProvince', 'Phone',
                                    'Email'])
    info.append(business.columns.values)
    for i in range(len(business)):
        if business["BusinessID"][i] in bad_bid:
            info.append(business.iloc[i])

    write(base_dir, "broken_Links.csv", info)


def write(base_dir, file_name, lst):
    """
    Writes analyzed url into new file

    :param base_dir: the base directory
    :param file_name: the file name of the csv file
    :param lst: the content being writen into file
    """
    with open(base_dir + file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)

def main():
    bad = http_error(base_dir, "Analyzed Url.csv")
    bad = syntax_error(base_dir, "bad syntax.csv", bad)
    indentify_business(base_dir, "mn_bbb_businesses.csv", bad)
    no_Url(base_dir, "mn_bbb_businesses.csv")


if __name__ == "__main__":
    main()





