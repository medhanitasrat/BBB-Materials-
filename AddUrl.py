import pandas as pd

from generate_url import company_URL


def reads(base_dir, fileName):
    """
    Reads company information form csv and writes a new file with a potential url included

    :param base_dir: the base directory
    :param fileName: the file name
    """
    df = pd.read_csv(base_dir + fileName, low_memory=False)
    urllst = []

    for i in range(len(df)):

        cURL = company_URL(df.iloc[i][1:].values)
        urllst.append(cURL)
    df['Website'] = urllst
    print(df)
    df.to_csv(base_dir + "newfile.csv")


def main():
    base_dir = 'C:/Users/Wenge/Desktop/BBB/'
    reads(base_dir, 'broken_Links.csv')
    reads(base_dir, 'noUrl.csv')


if __name__ == "__main__":
    main()
