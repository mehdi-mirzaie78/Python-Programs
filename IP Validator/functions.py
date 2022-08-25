import re
from pythonping import ping


def validate_ip(filename: str, result: str = 'validated ips.txt') -> list:
    """
    validate_ip: it gets a text file with some IPs inside and, it gives
    back IPs which are valid.
    -------------------------------------------------------------------
    :param: filename: Name of the file which contains IPs.
    :param: result: Name of the file that results will store into.
    :return: None
    """
    with open(filename) as file:
        ip_list = file.read()

    # repetitive_pattern which includes numbers from 0 to 255
    rp = r"([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    pattern = re.compile(r'\b' + rp + r'\.' + rp + r'\.' + rp + r'\.' + rp + r'\b')

    # Finding all matches inside the given text file
    valid_ips = pattern.findall(ip_list)
    valid_ips_store = list(map(lambda x: '.'.join(x) + '\n', valid_ips))

    # Storing the results into a text file
    with open(result, 'w') as f:
        f.writelines(valid_ips_store)
        print('Valid IPs has been stored successfully')

    return valid_ips


def optimal_ping_ip(ips: list, optimal_ping: float, file: str = 'optimal ips.txt') -> None:
    optimal_ips = [ip for ip in ips if ping(ip).rtt_max_ms <= optimal_ping]
    print(optimal_ips)
    optimal_ips = [ip + '\n' for ip in optimal_ips]
    with open(file, 'w') as f:
        f.writelines(optimal_ips)
