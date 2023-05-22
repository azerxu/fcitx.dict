#!/usr/bin/env python
# coding: utf-8

import os
import sys

# filter out of gbk word
GBK_UP = ord("\uFEFE")
GBK_UP = 50000


def load_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("..."):
                break

        for line in f:
            phrase, pinyin, weight = line.rstrip().split("\t")
            _pys = pinyin.split()
            if all(_py.isascii() for _py in _pys):
                yield "'".join(_pys), phrase, int(
                    weight) if weight.isdigit() else 1


def trans(filename, base=True, freq=0):
    cwd = os.path.dirname(__file__)
    outfile = os.path.join(cwd, "pybase.org") if base else os.path.join(
        cwd, "pyphrase.org")
    with open(outfile, mode="a", encoding="utf-8") as out:
        for pinyin, phrase, weight in load_file(filename):
            if base and ord(phrase) > GBK_UP:  # filter out of gbk characters
                continue
            if weight >= freq:
                print(pinyin, phrase, file=out)


def main():
    args = sys.argv[1:]
    freq = 1
    if args and args[0].startswith("-"):
        freq = int(args[0][1:])
        args = args[1:]

    for filename in args:
        base = "base" in filename
        trans(filename, base=base, freq=freq)


if __name__ == "__main__":
    main()
