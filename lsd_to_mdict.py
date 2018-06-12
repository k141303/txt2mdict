# -*- coding: utf-8 -*-
"""
lsdをMDict形式に変換します。
"""

from writemdict import MDictWriter, encrypt_key
import sys

args = sys.argv

d = {}

with open(args[1], encoding="shift-jis") as f:
    line = f.readline()

    while line:
        words = line.split('\t')
        d[words[0]] = words[2]+','+words[3]
        line = f.readline()

with open("lsd.mdx", "wb") as outfile:
    writer = MDictWriter(d,
                         "lsd",
                         "\"UTF-8\" encoding.",
                         encoding="utf-8")
    writer.write(outfile)
