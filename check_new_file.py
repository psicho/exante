import requests
from lxml import html
from ftplib import FTP
import ftputil
import time, datetime
from datetime import date
import json


link = 'ftp://ftp.cmegroup.com/pub/span/data/cme/'


today = date.today()

# mounths = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}



def check():
    new_cme = []
    cme_data = {}
    pa2_files = []

    with open('cme_data.json', "r") as cme_data:
        try:
            cme_data = json.load(cme_data)
        except json.decoder.JSONDecodeError:
            cme_data = {}
            # print('Ошибка открытия файла')


        # newses = newses[::-1]
    # print('cme_data >>> ', cme_data)
    pa2_files = []
    with FTP("ftp.cmegroup.com") as ftp:
        ftp.login()
        ftp.cwd('/pub/span/data/cme/')
        # names = ftp.dir()

        listing = []
        ftp.retrlines("LIST", listing.append)

        for i in range(len(listing)):
            words = listing[i].split(None, 8)
            # print('words', words)

            filename = words[-1].lstrip()
            # print(filename)
            if '.pa2.zip' in filename:
                # print(filename)
                pa2_files.append(filename)

                # print(datetime.date(year='', month=words[-4], day=words[-3]))
                # print('words', words)
                # t4 = datetime(year=today.year, month=mounths[words[-4]], day=words[-3], hour=words[-2].split(':')[0], minute=words[-2].split(':')[1], second=0)

                # print(words, filename)
    for file in pa2_files:
        file_add = file.split('.')
        # print(file_add[2])

        if len(file_add) == 5 and file_add[2] in cme_data:
            if file_add[1] not in cme_data[file_add[2]]:
                cme_data[file_add[2]].append(file_add[1])
                new_cme.append(file)
        elif len(file_add) == 5:
            # print(file_add[2])
            # cme_data[file_add[2]] = []
            cme_data[file_add[2]] = [file_add[1]]
            new_cme.append(file)

    json.dump(cme_data, open("cme_data.json", "w"))

    return new_cme


pa2_files = check()
print(len(pa2_files))
# print(pa2_files)
