import os
import shutil
import re


def get_file(filepath):
    """
    Reads a file and returns its text
    :param filepath: String
    :return: String
    """
    with open(filepath, 'r') as reader:
        return reader.read()


def get_phone_numbers(text):
    """
    Extracts phone numbers of varying formats from a text string.
    :param text: String
    :return: List
    """

    # Search text for phone numbers
    pattern_phone_num = r'(?:(?:\+)?\d{1,3}[\s-])?\(?:?\d{3}\)?[\s.-]\d{2,3}[\s.-]\d{4}(?:x\d+)?|(?:\d{10})'

    phone_numbers = re.findall(pattern_phone_num, text)

    formatted_phone_nums = []
    for num in phone_numbers:
        formatted_phone_nums.append(format_phone_num(num))

    return formatted_phone_nums


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

    with open(filename, 'w+') as f:
        f.write(content)

    shutil.move(filename, directory)


def format_main_num(num):
    """
    Parses and truncates a phone number. Returns last 10 digits separated by dashes.
    :param num: String
    :return: String
    """
    number = ''

    # Get digits only
    for i in range(len(num)):
        if num[i].isnumeric():
            number += num[i]

    # Remove excess front digits
    while len(number) > 10:
        number = number[1:]

    # Return formatted phone number
    return number[:3] + '-' + number[3:6] + '-' + number[6:]


def format_phone_num(num):
    """
    Formats a phone number, handles extensions.
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


if __name__ == "__main__":
    # Get phone numbers
    text_content = get_file('./assets/potential-contacts.txt')
    numbers = get_phone_numbers(text_content)
    write_list_to_file(numbers, 'phone_numbers.txt', 'assets')

