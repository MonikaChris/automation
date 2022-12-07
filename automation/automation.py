import os
import shutil
import re

# Get text
with open('./assets/potential-contacts.txt', 'r') as reader:
    text = reader.read()

# Search text for phone numbers
pattern_phone_num = r'(((\+)?\d{1,3}[\s-])?\(?\d{3}\)?[\s.-]\d{2,3}[\s.-]\d{4}(x\d+)?|(\d{10}))'
pattern_phone = r'(?:(?:\+)?\d{1,3}[\s-])?\(?:?\d{3}\)?[\s.-]\d{2,3}[\s.-]\d{4}(?:x\d+)?|(?:\d{10})'

phone_numbers = re.findall(pattern_phone, text)

if __name__ == "__main__":
    print(phone_numbers)

