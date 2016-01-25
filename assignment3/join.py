import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record[0]: table
    # record[1]: order_id
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of att
    tab_record=[]
    line_records=[]
    for v in list_of_values:
    	if(v[0]=='order'):
    		tab_record=v
    	else:
    		line_records.append(v)
    
    jrecords=[]		
    for jr in line_records:
    	jrecord=[]
    	for i in tab_record:
    		i=i.encode('utf-8')
    		jrecord.append(i) 
    	for j in jr:
    		j=j.encode('utf-8')
    		jrecord.append(j)
    	jrecords.append(jrecord)
    	mr.emit(jrecord)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
