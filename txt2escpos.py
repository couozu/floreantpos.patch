#!/usr/bin/python -utt
# -*- coding: utf-8 -*-

import sys
#init printer
sys.stdout.write('\x1B\x40')
#set codepage 866
sys.stdout.write('\x1B\x74\x07')

for line in sys.stdin.readlines():
    sys.stdout.write(line.decode('utf8').encode(encoding='cp866', errors='ignore')[:44])

#feed and cut
sys.stdout.write('\n\n\n\n\n\n\n\n\x1d\x56\x00')
