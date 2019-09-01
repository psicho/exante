import os
from ftplib import FTP

# download the file
local_filename = os.path.join(r"\pa2", filename)
lf = open(local_filename, "wb")
FTP.retrbinary("RETR " + filename, lf.write, 8*1024)
lf.close()