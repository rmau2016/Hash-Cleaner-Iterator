import re
import os
import io
from io import StringIO

r_file = io.open('file.txt', mode = 'r', buffering=-1, encoding=None, errors=None, closefd=True)
w_file = io.open('md5.txt', 'a')
m_1=[]
for line in r_file:
	string = r_file.readline()
	file_like_io = StringIO(string)

	for line in file_like_io:
		m_1.append(line)
		shortword = re.compile(r'\W*\b\w{1,31}\b')
		print(shortword.sub('', line))
		w_file.writelines(shortword.sub('',line))
		

