# 2022-08-25 21:14:33.896342
# description: this is a python script to store valid IPs from a text file of IPs.
# Created By Mark --* (Mehdi Mirzaie)
# =================================================================================
import argparse
from functions import validate_ip, optimal_ping_ip

parser = argparse.ArgumentParser(description="IP Validator Scripts", epilog="Created By Mark --*")

parser.add_argument('-f', '--filename', required=True, help='Full Name of the text file with extension')
parser.add_argument('-dp', '--desired_ping', required=True, type=float, help='Desired ping in ms')
parser.add_argument('-v', '--validate', action='store_true', default=False, help='Validates IPs from given file')
parser.add_argument('-s', '--save', help='Use this flag to save your results in file', default='ips-optimal-pings.txt')

args = parser.parse_args()

if args.validate:
    ip_lst = validate_ip(args.filename)
else:
    with open(args.filename) as f:
        ip_lst = list(map(str.strip, f.readlines()))

optimal_ping_ip(ip_lst, args.desired_ping, args.save)
