<p align="center">
  <p align="center"><img width="238" height="135" src="https://pysimplegui.net/images/logos/psglogofull.svg"><p>

  <h2 align="center">psgtray</h2>
  <h2 align="center">A PySimpleGUI Application</h2>
</p>

Adds ability to run your program in the System Tray using PySimpleGUI tkinter port













## Features

* Adds System Tray Icon
* Adds ability to show messages in system tray
* Show and get menu items from system tray icon
* Provides capability normally only available in the Qt and Wx ports of PySimpleGUI
* Integrates with the pystray python package



## Installation

### Using PIP with PyPI

The latest official release of PySimpleGUI products can be found on PyPI.  To pip install the demo applications from PyPI, use this command

#### If you use the command `python` on your computer to invoke Python (Windows):

`python -m pip install --upgrade psgtray`

#### If you use the command `python3` on your computer to invoke Python (Linux, Mac):

`python3 -m pip install --upgrade psgtray`

### Using PIP with GitHub

You can also pip install the PySimpleGUI Applications that are in the PySimpleGUI GitHub account.  The GitHub versions have bug fixes and new programs/features that have not yet been released to PyPI. To directly pip install from that repo:

#### If you use the command `python` on your computer to invoke Python (Windows):

```bash
python -m pip install --upgrade https://github.com/PySimpleGUI/psgtray/zipball/main
```

#### If you use the command `python3` on your computer to invoke Python (Linux, Mac):

```bash
python3 -m pip install --upgrade https://github.com/PySimpleGUI/psgtray/zipball/main
```

## Adding To Your PySimpleGUI Program

This is a copy of the demo program that can be found in the PySimpleGUI Project's Demo Program folder.

```python
import PySimpleGUI as sg
from psgtray import SystemTray

"""
    A System Tray Icon courtesy of pystray and your friends at PySimpleGUI
    
    Import the SystemTray object with this line of code:
    from psgtray import SystemTray

    Key for the system tray icon is: 
        tray = SystemTray()
        tray.key
        
    values[key] contains the menu item chosen.
    
    One trick employed here is to change the window's event to be the event from the System Tray.
    
    
    Copyright PySimpleGUI 2021
"""

def main():

    menu = ['', ['Show Window', 'Hide Window', '---', '!Disabled Item', 'Change Icon', ['Happy', 'Sad', 'Plain'], 'Exit']]
    tooltip = 'Tooltip'

    layout = [[sg.Text('My PySimpleGUI Celebration Window - X will minimize to tray')],
              [sg.T('Double clip icon to restore or right click and choose Show Window')],
              [sg.T('Icon Tooltip:'), sg.Input(tooltip, key='-IN-', s=(20,1)), sg.B('Change Tooltip')],
              [sg.Multiline(size=(60,10), reroute_stdout=False, reroute_cprint=True, write_only=True, key='-OUT-')],
              [sg.Button('Go'), sg.B('Hide Icon'), sg.B('Show Icon'), sg.B('Hide Window'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True)


    tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON)
    tray.show_message('System Tray', 'System Tray Icon Started!')
    sg.cprint(sg.get_versions())
    while True:
        event, values = window.read()

        # IMPORTANT step. It's not required, but convenient. Set event to value from tray
        # if it's a tray event, change the event variable to be whatever the tray sent
        if event == tray.key:
            sg.cprint(f'System Tray Event = ', values[event], c='white on red')
            event = values[event]       # use the System Tray's event as if was from the window

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.cprint(event, values)
        tray.show_message(title=event, message=values)

        if event in ('Show Window', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            window.un_hide()
            window.bring_to_front()
        elif event in ('Hide Window', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            window.hide()
            tray.show_icon()        # if hiding window, better make sure the icon is visible
            # tray.notify('System Tray Item Chosen', f'You chose {event}')
        elif event == 'Happy':
            tray.change_icon(sg.EMOJI_BASE64_HAPPY_JOY)
        elif event == 'Sad':
            tray.change_icon(sg.EMOJI_BASE64_FRUSTRATED)
        elif event == 'Plain':
            tray.change_icon(sg.DEFAULT_BASE64_ICON)
        elif event == 'Hide Icon':
            tray.hide_icon()
        elif event == 'Show Icon':
            tray.show_icon()
        elif event == 'Change Tooltip':
            tray.set_tooltip(values['-IN-'])

    tray.close()            # optional but without a close, the icon may "linger" until moused over
    window.close()

if __name__ == '__main__':
    main()
```

# Limitations

The Windows implementation is working well.  The Linux GTK version, not as well.

Updating the Menu after initial creation is not yet supported.

# Requirements

In order to use this pacakge you'll also need these packages:

* PySimpleGUI
* pystray (licensed under LGPL3)

Currently only versions <= 0.18.0 of pystray are supported

## License & Copyright

Copyright 2023-2024 PySimpleSoft, Inc. and/or its licensors.

This is a free-to-use "Utility" and is licensed under the
PySimpleGUI License Agreement, a copy of which is included in the
license.txt file and also available at https://pysimplegui.com/eula.

Please see Section 1.2 of the license regarding the use of this Utility,
and see https://pysimplegui.com/faq for any questions.


## Contributing

We are happy to receive issues describing bug reports and feature
requests! If your bug report relates to a security vulnerability,
please do not file a public issue, and please instead reach out to us
at issues@PySimpleGUI.com.

We do not accept (and do not wish to receive) contributions of
user-created or third-party code, including patches, pull requests, or
code snippets incorporated into submitted issues. Please do not send
us any such code! Bug reports and feature requests should not include
any source code.

If you nonetheless submit any user-created or third-party code to us,
(1) you assign to us all rights and title in or relating to the code;
and (2) to the extent any such assignment is not fully effective, you
hereby grant to us a royalty-free, perpetual, irrevocable, worldwide,
unlimited, sublicensable, transferrable license under all intellectual
property rights embodied therein or relating thereto, to exploit the
code in any manner we choose, including to incorporate the code into
PySimpleGUI and to redistribute it under any terms at our discretion.
