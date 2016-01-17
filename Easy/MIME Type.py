import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed
ext_list = []
file_name_list = []
fname_list = []

for i in xrange(n):
    ext, mt = raw_input().split()

    file_name_list.append(mt)
    ext_list.append("." + ext.lower())

#print >> sys.stderr, ext_list
#print >> sys.stderr, file_name_list

for i in xrange(q):
    fname = raw_input().lower()  # One file name per line.
    fname = fname[fname.find("."):].replace("..", ".")
    
    #print fname
    #print ext_list.count(fname)

    if ext_list.count(fname) == 0:
        print "UNKNOWN"
    else:
        print file_name_list[ext_list.index(fname)]
