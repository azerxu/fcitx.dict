#!/usr/bin/env python
# coding: utf-8

import sys
import os

def load_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('...'):
                break

        for line in f:
            phrase, pinyin, weight = line.rstrip().split('\t')
            yield "'".join(pinyin.split()), phrase


def trans(filename, base=True):
    cwd = os.path.dirname(__file__)
    outfile = os.path.join(cwd, "pybase.org") if base else os.path.join(cwd, "pyphras.org")
    with open(outfile, mode='a', encoding='utf-8') as out:
        for pinyin, phrase in load_file(filename):
            print(pinyin, phrase, file=out)


def main():
    for filename in sys.argv[1:]:
        base = 'base' in filename
        trans(filename, base=base)


if __name__ == '__main__':
    main()
