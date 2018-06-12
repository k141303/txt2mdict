# -*- coding: utf-8 -*-
"""
ejdicをMDict形式に変換します。
"""

from writemdict import MDictWriter, encrypt_key
import sys

args = sys.argv

d = {}

with open(args[1]) as f:
    line = f.readline()

    while line:
        word,meaning = line.split('\t',1)
        meaning = meaning.replace('/','\n').replace('・',',')
        line = f.readline()
        d[word] = meaning

with open("ejdic.mdx", "wb") as outfile:
    writer = MDictWriter(d,
                         "EJDIC",
                         "\"UTF-8\" encoding.",
                         encoding="utf-8")
    writer.write(outfile)
