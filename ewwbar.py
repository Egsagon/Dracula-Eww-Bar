import os, json

# Set workspace gaps
cur = [wk for wk in json.loads(os.popen('i3-msg -t get_workspaces').read()) if wk['focused'] == True][0]
os.popen(f"i3-msg \"gaps left current set {[0, 85][cur['output'] == 'DP-7']}\"")

# Show resize mod
os.popen(f"eww {('open', 'close')[json.loads(os.popen('i3-msg -t get_binding_state').read())['name'] == 'default']} resizer")

# Show caps lock
os.popen(f"eww {('close', 'open')[int(os.popen('xset q | grep LED').read().rstrip()[-1])]} capser")
