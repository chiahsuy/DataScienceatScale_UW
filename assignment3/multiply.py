import MapReduce_mx
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce_mx.MapReduce()

# =============================
# Do not modify above this line

def mapper(record,dm):
    # mat: matrix identifier; i:row; j:col
    # value: item contents
    mat = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if mat=='a':
    	for k in range(0,dm['b']+1):
    		mr.emit_intermediate((i,k),(j,value))
    else:
    	for k in range(0,dm['a']+1):
    		mr.emit_intermediate((k,j), (i,value))

def reducer(key, list_of_values):
    # key: i,k
    # value: list of occurrence counts
    mul={}
    total=0
    for v in list_of_values:
    	if v[0] in mul:
    		total += mul[v[0]]*v[1]
    	else:
    		mul[v[0]]=v[1]
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
