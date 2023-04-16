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
    statuses = ['200', '301', '400', '401', '403', '404', '405', '500']

    if (len(elements) < 7):
        return False
    elif elements[-2] not in statuses:
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
    """
    Lorem ipsum dolor sit amet, qui minim labore adipisicing
    """
    try:
        for line in logs:
            line_count += 1
            tokens = line.split()
            if len(tokens) > 6:
                total_file_size += int(tokens[-1])
            if validate_line(line):
                status_codes[int(tokens[-2])] += 1
                if (line_count % 10) == 0:
                    print_logs()
    except KeyboardInterrupt:
        print_logs()
        raise
    finally:
        print_logs()
