
# download the file
local_filename = os.path.join(r"\pa2", filename)
lf = open(local_filename, "wb")
ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
lf.close()