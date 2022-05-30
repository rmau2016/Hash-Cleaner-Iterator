import re
import os
import io
from io import StringIO


m_1 = []
answer = input("<0> for md5 and email" + "\n" +
 "<1> for Sha1 (or with salt) and email" + "\n" + "<2> for SHA-1 Only (Or with Salt)" + "\n"  "<3> for MD5 Only" + "\n" + "<4> to coloniate sha1 and salt after extraction" + "\n" + ">>>>")
r_file = input("What file do you want to read?(Without .txt)")
r_file +=".txt"
w_file = input("What file do you want to write?(Without .txt)")
w_file += ".txt"

r_file2 = io.open(r_file, mode='r', buffering=-1,
                  encoding=None, errors=None, closefd=True)
w_file2 = io.open(w_file, 'w')

if answer == '0':
    for line in r_file2:

        match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
        shortword = re.compile(r'\W*\b\w{1,31}\b')
        w_file2.writelines(
            str(shortword.sub("", line)).strip()+str(match)+"\n")

if answer == '1':
    for line in r_file2:
        match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
        shortword = re.compile(r'\W*\b\w{1,39}\b')
        w_file2.writelines(str(shortword.sub("", line)).strip() + str(match) + "\n")

if answer == '2':
    for line in r_file2:

        shortword = re.compile(r'\W*\b\w{1,39}\b')
        w_file2.writelines(str(shortword.sub("", line)).strip()+"\n")

if answer == '3':
    for line in r_file2:

        shortword = re.compile(r'\W*\b\w{1,31}\b')
        w_file2.writelines(str(shortword.sub("", line)).strip()+"\n")

if answer == '4':
    for line in r_file2:

        w_file2.writelines(':'.join(line[i:i+41] for i in range(0, len(line), 40)))



r_file2.close()
w_file2.close()
