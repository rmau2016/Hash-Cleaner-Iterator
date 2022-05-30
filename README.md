# Hash Cleaner and Iterator
This Python Script will extract all Md5 hashes or SHA1 hashes in a file of choice and the emails with the corresponding hash.

cleaner.py : Cleaner Mode: For r_file put in the database file location, for w_file put the directory and file you want to write.
Will update for other hashes choices and salts.
Iterator mode will cross reference two files... one with [HASH:EMAIL] and the other would be [HASH:PASSWORD] to result [EMAIL:PASSWORD] 
Wordlist mode, the final mode will take the [Email:Pass] file and separate it into two files of your choice.

TIPS-------
FIRST: Use "paste" command to combine files Horizontally
Second: Combine hash and email types because they are predictable to get (hash:email) using paste command.
THIRD: Delete all remaining spaces... using cat file.txt | tr -d "[:blank:]"
FOURTH: Now you will have two files, one is the hashcat potfile [HASH:PASS], the other is [HASH:EMAIL]
FIFTH: Use an iteration python script to check the hashes against both files to combine email with password.
---------
IT GENERALLY LOOKS LIKE THIS IN ITERATION MODE:

First File: [HASH:EMAIL]
Second File: [HASH:PASS]
We want [EMAIL:PASS]! So we write to a third file...
