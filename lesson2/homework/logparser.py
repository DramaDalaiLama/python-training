import collections
import sys
import getopt

filepath = sys.argv[1]

with open (filepath[0], "r") as myfile:
    data=myfile.readlines()

def make_address_list(data):
    result = []
    for line in data:
        addr = line.split(' ')[0]
        result.append(addr)
    return result

#print make_address_list(data)
counter = collections.Counter(make_address_list(data))
print counter.most_common(10)
