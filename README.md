# Dracula-Eww-Bar
Vertical eww bar dracula-themed.

## Description

Includes:
- Clock with hour and minutes
- I3 gaps informations compatible with X monitors (i think)
- Monitoring bars for the CPU, RAM, and GPU (config specific tho)
- Tray with settings, shutdown, restart and lock buttons

## Files

`eww.yuck`    - Main eww file with the bar
`popups.yuck` - Popups for the shutdown, restart menu, and informations like i3 resize mode
`eww.scss`    - Main eww style sheet
`src/*.png`   - Icons for the buttons on the bar tray
`parser.py`   - Must be in the eww config directory. Will parse the output of i3-msg for the bar
`ewwbar.py`   - Has to be run every X seconds by the i3 config. Will change the gaps for the main
                monitor in order for the bar to be visible, and decide wheter to show the resize
                and cap lock informations.
## TODO

- The settings popup
- Remove the last at the end of the i3 workspace list
- Make it less ugly
