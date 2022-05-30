import re
import os
import io
from io import StringIO


m_1 = []
mode = input("DO YOU WANT CLEANING MODE(1) OR ITERATOR MODE?(2) OR [EMAIL:PASS] WORDLIST MODE(3)?\n")
answer = '6'

if mode == '1':
    answer = input("<0> for md5 and email" + "\n" +
                   "<1> for Sha1 (or with salt) and email" + "\n" + "<2> for SHA-1 Only (Or with Salt)" + "\n"  "<3> for MD5 Only" + "\n" + "<4> to coloniate sha1 and salt after extraction" +"\n" ">>>>")
    r_file = input("What file do you want to read?(Without .txt)")
    r_file += ".txt"
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
        w_file2.writelines(
            str(shortword.sub("", line)).strip() + str(match) + "\n")

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

        w_file2.writelines(':'.join(line[i:i+41]
                           for i in range(0, len(line), 40)))


if mode == '2':
    hashcat = input(
        "What's the hash file or the pot file? [HASH:PASSWORD]?(Without .txt)\n")
    email = input("What's the email file? [HASH:EMAIL]?(Without .txt)\n")
    file_out = input(
        "What's the Output File?[EMAIL:PASSWORD]?(Without .txt)\n")
    hashcat += ".txt"
    email += ".txt"
    file_out += ".txt"
    m = []
    z = []
    file_out = open(file_out, 'w+')
    file_in = open(email, 'r')
    for line in file_in:
    	m = file_in.readline()
    	m = m.split(":")
    	file_in2 = open(hashcat, 'r')
    	for line2 in file_in2:
        	z = file_in2.readline()
        	z = z.split(":")
        	if m[0].lower().strip() == z[0].lower().strip():
            		file_out.write(m[1] + ":" + z[1])
if mode == '3':
	r_file2=input("What is the Email:Pass File?(Without .txt)")
	r_file2 += ".txt"
	r_file2 = open(r_file2, 'r')
	w_file2 = input("What File do you want to save emails?(Without .txt)")
	w_file2 += ".txt"
	w_file3 = input("What File do you want to save passwords?(Without .txt)")
	w_file3 += ".txt"
	w_file2 = open(w_file2, 'w')
	w_file3 = open(w_file3, 'w')
	for line in r_file2:
    		newest = line.split(":")
    		User = line.split(":")[0]
    		Password = line.split(":")[1]
    		w_file2.write(User + "\n")
    		w_file3.write(Password + "\n")

r_file2.close()
w_file2.close()
