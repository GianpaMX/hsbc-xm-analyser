#!/usr/bin/python3.4

import sys
import csv

from analyser import Analyser
from argumentsParser import parse
from configuration import Configuration

inputFilenames, output, config = parse(sys.argv, sys.stdout, Configuration())

analyser = Analyser(config)

for fileName in inputFilenames:
    accountBalancePeriod = analyser.analyse(fileName)

dictWriter = csv.DictWriter(output, analyser.fieldnames)
dictWriter.writeheader()

for row in analyser.result:
    dictWriter.writerow(row)
