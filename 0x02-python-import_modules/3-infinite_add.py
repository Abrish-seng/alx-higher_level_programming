#!/usr/bin/python3
import sys
sum = 0
for i in range(len(sys.argv) - 1):
    sum = sum + int(sys.argv[i + 1])
print(sum)
