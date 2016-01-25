import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: seq_id
    # value: nucleotides 
    key = record[0]
    value = record[1]
    nucleo_st = value[:-10] 
    mr.emit_intermediate(nucleo_st, key)

def reducer(key, list_of_values):
    # key: trimmed nucleotide
    # value: list of seq_id
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
