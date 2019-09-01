import requests
from lxml import html
from ftplib import FTP
import ftputil
import time, datetime
from datetime import date


link = 'ftp://ftp.cmegroup.com/pub/span/data/cme/'


today = date.today()

# mounths = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
pa2_files = []


def ftp_lib():
    with FTP("ftp.cmegroup.com") as ftp:
        ftp.login()
        ftp.cwd('/pub/span/data/cme/')
        # names = ftp.dir()

        listing = []
        ftp.retrlines("LIST", listing.append)

        for i in range(len(listing)):
            words = listing[i].split(None, 8)
            filename = words[-1].lstrip()
            if '.pa2' in filename:
                pa2_files.append(filename)
                # print(datetime.date(year='', month=words[-4], day=words[-3]))
                # print('words', words)
                # t4 = datetime(year=today.year, month=mounths[words[-4]], day=words[-3], hour=words[-2].split(':')[0], minute=words[-2].split(':')[1], second=0)

                # print(words, filename)


ftp_lib()
print(len(pa2_files))
print(len(set(pa2_files)))
