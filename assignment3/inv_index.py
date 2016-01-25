import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def unique(list):
		output = []
		for item in list:
				if item not in output:
						output.append(item)
		return output


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    words = unique(words)
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total =[]
    for v in list_of_values:
      total.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
