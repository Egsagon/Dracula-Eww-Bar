# ======================================= #
# Script that parses the output of i3-msg #
# into readable jsons for the EWW BAR.    #
# ======================================= #

import os, json

wks = json.loads(os.popen('i3-msg -t get_workspaces').read())
outputs = list({wk['output'] for wk in wks})
tree = []

outputs.sort(key = lambda out: int(out[3:]), reverse = 1)

for out in outputs:
   cur = [{'name': wk['name'],
           'visible': wk['visible'],
           'focused': wk['focused'],
           'urgent': wk['urgent']}
        for wk in wks if wk['output'] == out]
   
   tree.append({'name': out, 'wks': cur})

print(json.dumps(tree))