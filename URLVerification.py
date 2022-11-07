import SyntaxChecker
import StatusCodeChecker
import csv

def main():

    base_dir = 'Enter the base directory here(where the file you want to read is located/where you want to write the new file)'
    b_id_list = []
    url_id_list = []
    url_list = []
    status_check = []
    uid = []
    bad_syntax = [["bid", "url_id", "url"]]
    new_file = [["bid", "url_id", "url", "status_code"]]

    file_name = "Enter the file name of the file you want to read"
    opener(base_dir, file_name, b_id_list, url_id_list, url_list)
    # loop through list of url for analysis
    for i in range(len(url_list)):
        is_valid, url = SyntaxChecker.verify(url_list[i])
        if is_valid:
            status_check.append(url)
            uid.append(i)
        else:
            bad = [b_id_list[i], url_id_list[i], url]
            bad_syntax.append(bad)
            write(base_dir, "bad syntax.csv", bad_syntax)

    status_list = StatusCodeChecker.get_statuscode(status_check)

    for i in range(len(uid)):
        new_f = [b_id_list[uid[i]], url_id_list[uid[i]], status_check[i], status_list[i]]
        new_file.append(new_f)
        write(base_dir, "Analyzed Url.csv", new_file)


def opener(base_dir, file_name, b_id_list, url_id_list, url_list):
    """
    Opens a csv file that contains all the a list of the URLs of the businesses
    :param base_dir: the base directory
    :param file_name: the file name of the csv file
    :param b_id_list: the list of business id in the csv file
    :param url_id_list: the list of URL id in the csv file
    :param url_list: the list of urls in the csv file
    """
    with open(base_dir + file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            b_id_list.append(row[1])
            url_id_list.append(row[2])
            url_list.append(row[3])


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


if __name__ == "__main__":
    main()

