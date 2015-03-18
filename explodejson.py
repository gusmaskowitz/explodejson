import json
import sys
import os.path
import os

# Take a filename as input. Assuming the filename ends with .json so cutting it
base = os.path.basename(sys.argv[1])[0:-5]
os.mkdir(base)
discovery = json.load(open(sys.argv[1]))
for key in discovery:
    path = os.path.join(base, key) + '.json'
    fp = open(path, 'w')
    value = discovery[key]
    json.dump(value, fp, sort_keys=True, indent=2)
    fp.close()
    
