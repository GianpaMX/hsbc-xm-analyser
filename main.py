#!/usr/bin/python3.4

import sys

from analyser import Analyser
from configuration import Configuration

fileNames = []
output = sys.stdout
config = Configuration()

i = 1

while i < len(sys.argv):
    if sys.argv[i] == '-c' or '--config':
        config = config.readFrom(sys.argv[i + 1])
        i += 2
        continue

    if sys.argv[i] == '-o' or '--output':
        output = open(sys.argv[i + 1], 'w')
        i += 2
        continue

    if not sys.argv[i].startswith('-'):
        fileNames.append(sys.argv[i])

    i += 1

analyser = Analyser(config)

for fileName in fileNames:
    accountBalancePeriod = analyser.analyse(fileName)

result = analyser.getResult()

output.write(result)
