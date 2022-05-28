import re

m = []
z = []
index = 1
file_out = open('scraped.txt', 'w')
file_in = open('Finale2.txt', 'r')
for line in file_in:
    m = file_in.readline()
    m = m.split(":")
    file_in2 = open('hashcat.txt', 'r')
    for line in file_in2:
         z = file_in2.readline()
         z = z.split(":")
         if z[0].upper() == m[0].upper():
             file_out.write(str(m[1]) + ":" + str(z[1]))
file_out.close()
file_in.close()
file_in2.close()
