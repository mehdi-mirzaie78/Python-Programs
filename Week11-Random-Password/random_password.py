import random
from time import time
import argparse

parser = argparse.ArgumentParser(description='This is a script for generating password', epilog='Created By Mehdi')

parser.add_argument('-w', nargs='+', required=True, help='Charters that you want to create a password with')
parser.add_argument('-o', action='store', help='Name of the file that you want to store it')
parser.add_argument('-l', nargs='+', type=int, help='Range of length of the passwords')

args = parser.parse_args()


def process_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time() - t1
        print(f'finished time: {t2:.4f} sec')
        return res

    return wrapper


def states(n: int, digits: int) -> int:
    if n < digits:
        raise ValueError
    s = 1
    for i in range(digits):
        s *= n
        n -= 1
    return s


@process_timer
def generate_pass(number: int, repos: list) -> list:
    password_list = []
    while len(password_list) != states(len(repos), number):
        password = random.sample(repos, k=number)
        password = ''.join(password)
        if password not in password_list:
            password_list.append(password)
    else:
        print(f'Number of passwords: {len(password_list)}')
        return sorted(password_list)


@process_timer
def generate_all_pass(number: int, repos: list) -> list:
    password_list = []
    while len(password_list) != number ** number:
        password = random.choices(repos, k=number)
        password = ''.join(password)
        if password not in password_list:
            password_list.append(password)
    else:
        print(f'Number of passwords: {len(password_list)}')
        return sorted(password_list)


def final(start: int, end: int, rep: list, file: str) -> None:
    result = {}
    for i in range(start, end + 1):
        result[i] = generate_pass(i, rep)
    else:
        with open(file, 'a') as f:
            for j in result:
                temp = '\n'.join(result[j])
                f.write(f'Number of passwords: {len(result[j])}\n')
                f.write(f'length: {j} characters \n')
                f.write('----------------------------\n')
                f.write(temp + '\n----------------------------\n')


repo = args.w
filename = args.o
length = args.l

final(length[0], length[1], repo, filename)
