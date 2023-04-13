#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim
"""
from sys import stdin

logs = stdin
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
total_file_size = 0


def validate_line(line):
    """
    Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum
    """
    elements = line.split()
    statuses = [200, 301, 400, 401, 403, 404, 405, 500]
    status = int(elements[-2])
    method = elements[4]
    number = 9
    size = int(elements[-1])
    url = '/projects/260'
    http = 'HTTP/1.1"'

    if status not in statuses:
        return False
    elif (len(elements) != number):
        return False
    elif (method != '"GET'):
        return False
    elif (size < 1):
        return False
    elif (url != elements[5]):
        return False
    elif (http != elements[6]):
        return False
    else:
        return True


def print_logs():
    """
    Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum
    """
    print("File size: {}".format(total_file_size))
    for key, value in status_codes.items():
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    try:
        for line in logs:
            tokens = line.split()
            if validate_line(line):
                line_count += 1
                status_codes[int(tokens[-2])] += 1
                total_file_size += int(tokens[-1])
                if line_count % 10 == 0:
                    print_logs()
    except KeyboardInterrupt:
        print("File size: {}".format(total_file_size))
        for key, value in status_codes.items():
            if value != 0:
                print("{}: {}".format(key, value))
