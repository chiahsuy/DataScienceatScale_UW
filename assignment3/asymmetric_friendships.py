import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: people pair
    # value: 
    person = record[0].encode('utf-8')
    friend = record[1].encode('utf-8')
    mr.emit_intermediate(person, (friend, +1))
    mr.emit_intermediate(friend, (person, -1))

def reducer(key, list_of_values):
    # key: person
    # value: frieind points: +1 friend, -1 not friend
    #print key
    #print list_of_values
    fd={}
    for v in list_of_values:
    	if v[0] in fd:
    		fd[v[0]]+=int(v[1])
    	else:
    		fd[v[0]]=int(v[1])
    for asyf in fd.keys():
    	if fd[asyf]==-1:
    		mr.emit((key,asyf))
    		mr.emit((asyf,key))
 	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
