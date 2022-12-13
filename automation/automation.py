import os
import shutil
import re


def get_file(filepath):
    """
    Reads a file and returns its text as a String.
    :param filepath: String
    :return: String
    """
    with open(filepath, 'r') as reader:
        return reader.read()


def get_email_addresses(text):
    """
    Extracts email addresses of varying formats from a text string, removes duplicates, returns a sorted list.
    :param text: String
    :return: List
    """
    pattern_email = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

    emails = re.findall(pattern_email, text)

    # Remove duplicates
    emails = set(emails)
    sorted_emails = sort_emails(list(emails))
    return sorted_emails


def sort_emails(lst):
    """
    Sorts list of email addresses.
    :param lst: List
    :return: List
    """
    lst.sort(key=lambda x: x.split('@')[0])
    return lst


def get_phone_numbers(text):
    """
    Extracts phone numbers of varying formats from a text string, removes duplicates, returns list.
    :param text: String
    :return: List
    """

    # Search text for phone numbers
    pattern_phone_num = r'(?:(?:\+)?\d{1,3}[\s-])?\(?:?\d{3}\)?[\s.-]\d{2,3}[\s.-]\d{4}(?:x\d+)?|(?:\d{10})'

    numbers = re.findall(pattern_phone_num, text)

    # Remove duplicates
    numbers = set(numbers)
    return list(numbers)


def format_phone_numbers(phone_numbers):
    """
    Formats phone numbers in a list
    :param phone_numbers: List
    :return: List
    """
    formatted_phone_nums = []
    for num in phone_numbers:
        form_num = format_phone_number(num)
        if form_num:
            formatted_phone_nums.append(form_num)

    return sort_phone_numbers(formatted_phone_nums)


def format_phone_number(num):
    """
    Formats a single phone number, handles extensions.
    :param num: String
    :return: String
    """
    # Check for extension
    if 'x' in num:
        number, extension = num.split('x')
        number = format_main_num(number)
        return number + 'x' + extension

    else:
        return format_main_num(num)


def sort_phone_numbers(lst):
    """
    Sort list of phone numbers.
    :param lst: List
    :return: List
    """
    lst.sort(key=lambda x: int(''.join(x[:12].split('-'))))
    return lst


def format_main_num(num):
    """
    Parses and truncates a phone number that has no extension. Returns last 10 digits separated by dashes.
    :param num: String
    :return: String
    """
    number = ''

    # Get digits only
    for i in range(len(num)):
        if num[i].isnumeric():
            number += num[i]

    # Delete 8 and 9-digit numbers
    if len(number) == 8 or len(number) == 9:
        return

    # Remove excess front digits
    while len(number) > 10:
        number = number[1:]

    # Return formatted phone number - if missing area code, insert area code 206
    if len(number) == 7:
        return '206-' + number[:3] + '-' + number[3:]
    else:
        return number[:3] + '-' + number[3:6] + '-' + number[6:]


def get_new_phone_numbers(new_file, old_file):
    """
    Extracts and formats phone numbers from a text file, but excludes phone numbers present in a second text file.
    :param new_file: String
    :param old_file: String
    :return: List
    """
    # Read old data
    with open(old_file, 'r') as reader:
        old_lst = reader.read().splitlines()

    # Read new data, extract phone numbers
    new_data = get_file(new_file)
    new_lst = get_phone_numbers(new_data)

    # Remove old numbers from list of new numbers
    for num in old_lst:
        if num in new_lst:
            new_lst.remove(num)

    # Return formatted numbers
    return format_phone_numbers(new_lst)


def write_list_to_file(lst, filename, directory):
    """
    Writes contents of a list to a specified file in a specified directory. Both the file and directory are created
    if they don't exist.
    :param lst: List
    :param filename: String
    :param directory: String
    :return: None
    """
    content = ''
    for elem in lst:
        content += elem + '\n'

    if not os.path.isdir(directory):
        os.mkdir(directory)

    with open(filename, 'w') as f:
        f.write(content)

    shutil.move(filename, directory)


if __name__ == "__main__":
    # Extract all phone numbers, format numbers, write them to a text file
    text_content = get_file('./assets/potential-contacts.txt')
    num_lst = get_phone_numbers(text_content)
    form_num_lst = format_phone_numbers(num_lst)
    write_list_to_file(form_num_lst, 'phone_numbers.txt', 'assets')

    # Omit duplicate phone numbers - extract all phone numbers, return formatted phone numbers minus those already
    # appearing in the existing-contacts file
    num_lst_short = get_new_phone_numbers('./assets/potential-contacts.txt', './assets/existing-contacts.txt')
    write_list_to_file(num_lst_short, 'phone_numbers_no_dupes.txt', 'assets')

    # Extract all email addresses, sort, write them to a text file
    text_content = get_file('./assets/potential-contacts.txt')
    email_addresses = get_email_addresses(text_content)
    write_list_to_file(email_addresses, 'emails.txt', 'assets')
