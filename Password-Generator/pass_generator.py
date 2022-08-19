from itertools import product, permutations
from string import ascii_letters as letters
from typing import Generator

###########################################

def generate_all_pass(repo: str|tuple|list, length: int) -> Generator:
    if len(repo) < length:
        raise ValueError("Length of repository must be more than length of generated password")
    result = product(repo, repeat=length)
    for password in result:
        yield ''.join(password)

###########################################

def generate_unique_pass(repo: str|tuple|list, length: int) -> Generator:
    if len(repo) < length:
        raise ValueError("Length of repository must be more than length of generated password")
    result = permutations(repo, r=length)
    for password in result:
        yield ''.join(password)


###########################################

def store_all_passes(repos, length, filename='all_pass_list.txt', mode='w'):
    with open(filename, mode=mode) as f:
        print(f'Generated passwords with {length} characters:\n\
----------------------------------------------------', file=f)
        c = 0
        for i in generate_all_pass(repos, length):
            c += 1
            print(f'<{i}>', end='\t', file=f)
        else:
            print(f'Number of generated passwords: {c}')
            f.write('\n-----------------------------------------------------------\n')
            print(f'Number of generated passwords: {c}', file=f)

###########################################

def store_unique_passes(repos, length, filename='unique_pass_list.txt', mode='w'):
    with open(filename, mode=mode) as f:
        print(f'Generated passwords with {length} characters:\n\
----------------------------------------------------', file=f)
        c = 0
        for i in generate_unique_pass(repos, length):
            c += 1
            print(f'<{i}>', end='\t', file=f)
        else:
            print(f'Number of generated passwords: {c}')
            f.write('\n-----------------------------------------------------------\n')
            print(f'Number of generated passwords: {c}', file=f)

###########################################
store_all_passes('1234567890', 6)
store_unique_passes('1234567890', 6)