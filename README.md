## Lab 19: Automation
Monika Davies

### About

This project implements the following functions that extract phone numbers and email addresses in varying formats 
from text data.

get_file() - reads a text file and returns contents as a string\
get_phone_numbers() - takes a string of text and returns a list of all phone numbers (original format preserved)\
format_phone_numers() - takes a list of phone numbers stored as strings and returns a formatted list in sorted order. 
The format provided is ###-###-####x### where the digits following x represent an extension number when available.\
get_new_phone_numbers() - takes two filenames, extracts the phone numbers from the first text file, compares this list 
with 
phone numbers listed in the second file and removes them from the list to prevent duplicates. Returns the shortened 
list of 
phone numbers.
get_email_addresses() - takes a string of text and returns a list of all email addresses in sorted order\
write_list_to_file() - takes a list (of phone numbers or email addresses), a filename string, and a directory name 
string. Writes the list contents to a text 
file with the given filename in the given directory. If the file and/or directory do not exist, they are created.

## How to Run
Run script: python3 automation/automation.py

Running this script calls the above methods in order to extract phone numbers and email addresses from the included 
text file potential-contacts.txt. It then writes the phone numbers to a phone_numbers.txt file, and the email 
addresses to an emails.txt file, both located in the assets folder.

A second phone numbers file (phone_numbers_no_dupes.txt) is also created which omits phone numbers already present 
in the existing-contacts.txt file.

## Acknowledgements

The regex expression used to collect phone numbers was based on the one found here, and modified for the purposes of 
this project:\
https://www.abstractapi.com/guides/phone-number-python-regex

The regex expression used to collect email addresses was found here:\
http://emailregex.com/




