from infi.systray import SysTrayIcon

def copypast(systray):
    import duck_windows

def on_quit_callback(systray):
    exit(-1)
def fake():
    return None

menu_options = (("CopyPast", None, copypast),('-----', None, fake),)
systray = SysTrayIcon("icon.ico", "Duck project", menu_options,on_quit=on_quit_callback)
systray.start()
