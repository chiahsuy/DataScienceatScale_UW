import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 
    
    def finddim(self,record, dim):
    		mat=record[0]
    		if mat=='a':
    				k=record[1]
    		else:
    				k=record[2]
    		if mat not in dim:
    				dim[mat]=k
    		else:
    				dim[mat]=max(k,dim[mat])

    def execute(self, data, mapper, reducer):
    		dim={}
    		for line in data:
    				record=json.loads(line)
    				self.finddim(record,dim)
    		
    		data.seek(0)		
    		for line in data:
    				record = json.loads(line)
    				mapper(record,dim)
    		
    		for key in self.intermediate:
    				reducer(key, self.intermediate[key])
    				
    		#jenc = json.JSONEncoder(encoding='latin-1')
    		jenc = json.JSONEncoder()
    		#print len(self.result)
    		for item in self.result:
    				print jenc.encode(item)
