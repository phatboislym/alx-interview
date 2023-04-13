from collections import defaultdict
import sys
import re

total_size = 0
status_code_counts = defaultdict(int)
line_count = 0
logs = sys.stdin

try:
    for line in logs:
        try:
            match = re.match(
                r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+|-)$', line)
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4)) if match.group(4) != '-' else 0
                total_size += file_size
                status_code_counts[status_code] += 1
        except:
            pass

        line_count += 1
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for status_code in sorted(status_code_counts.keys()):
                print(f'{status_code}: {status_code_counts[status_code]}')
            print()

except KeyboardInterrupt:
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_code_counts.keys()):
        print(f'{status_code}: {status_code_counts[status_code]}')
