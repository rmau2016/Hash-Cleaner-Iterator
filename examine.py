import re
import os
import io
from io import StringIO

r_file = io.open('textfile.txt', mode = 'r', buffering=-1, encoding=None, errors=None, closefd=True)
w_file = io.open('md5.txt', 'w')
m_1=[]
for line in r_file:

	match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
	shortword = re.compile(r'\W*\b\w{1,31}\b')
	w_file.writelines(str(shortword.sub("",line)).rstrip()+str(match)+"\n")
		

