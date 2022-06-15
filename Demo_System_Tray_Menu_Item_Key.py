import PySimpleGUI as sg

from psgtray import SystemTray


def main():
    layout = [
        [
            sg.Multiline(
                size=(None, 20),
                k='-OUTPUT-LOG-',
                write_only=True,
                auto_refresh=True,
                reroute_cprint=True,
            )
        ],
        [sg.Button('Clear'), sg.Push(), sg.Quit()],
    ]
    window = sg.Window(
        'System Tray With Custom Menu Item Key',
        layout=layout,
        enable_close_attempted_event=True,
    )

    tray_menu = ['', ['Show Window', 'Hello::-HELLO-', '!Logs', '---', 'Quit']]
    tray = SystemTray(
        menu=tray_menu,
        tooltip='System Tray With Custom Menu Item Key',
        single_click_events=True,
        window=window,
    )

    while True:
        event, values = window.read()

        if event == tray.key:
            event = values[event]

        if event in (sg.WIN_CLOSED, 'Quit'):
            break

        sg.cprint(f'event: {event}, values: {values}', colors='green on black')

        if event == sg.WIN_CLOSE_ATTEMPTED_EVENT:
            window.hide()
        elif event in (sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED, '-SHOW-'):
            window.un_hide()
        elif event == 'Clear':
            window['-OUTPUT-LOG-'].update('')
        elif event == '-HELLO-':
            sg.popup('Hello, Toy!', title='HELO')

    tray.close()
    window.close()


if __name__ == '__main__':
    main()
