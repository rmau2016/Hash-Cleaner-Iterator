# Hash Cleaner and Iterator
This Python Script has three modes...


## Cleaner Mode: 
For r_file put in the database file location, for w_file put the directory and file you want to write, this will extract the hash byitself, or also with email with corresponding hash in database file.[SUPPORTS MD5 ANND SHA1 FOR NOW]
(Will update for other hashes choices and salts.)
## Iterator mode: 
will cross reference two files... one with [HASH:EMAIL] and the other would be [HASH:PASSWORD] to result [EMAIL:PASSWORD] 
## Wordlist mode:
the final mode will take the [Email:Pass] file and separate it into two files of your choice.

## TIPS:
FIRST: Use "paste" command to combine files Horizontally if you have to, use "Emeditor" too to clean the files, for instance the [HASH:EMAIL] option in the cleaner will output HASH['EMAIL'], just replace [' with : and '] with nothing in an text editor.
SECOND: Delete all remaining spaces... using cat file.txt | tr -d "[:blank:]"
THIRD: Now you will have two files, one is the hashcat potfile [HASH:PASS], the other is [HASH:EMAIL]
FOURTH: Use an iteration python script to check the hashes against both files to combine email with password.

IT GENERALLY LOOKS LIKE THIS IN ITERATION MODE:

```First File: [HASH:EMAIL]
Second File: [HASH:PASS]
We want [EMAIL:PASS]! So we write to a third file...```
