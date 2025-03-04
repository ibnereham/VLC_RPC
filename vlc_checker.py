import psutil
import win32gui
import win32process

def get_vlc_pids():
    """Get all PIDs of running VLC processes."""
    return {proc.info['pid'] for proc in psutil.process_iter(['pid', 'name']) if proc.info['name'].lower() == 'vlc.exe'}

def get_vlc_window_titles():
    """Get titles of all VLC windows."""
    vlc_pids = get_vlc_pids()
    if not vlc_pids:
        return []
    
    vlc_windows = []
    def enum_windows_callback(hwnd, _):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid in vlc_pids:
            title = win32gui.GetWindowText(hwnd)
            if title:
                vlc_windows.append(title)
        return True

    win32gui.EnumWindows(enum_windows_callback, None)
    return vlc_windows

def is_vlc_window_open():
    """Check if VLC has any open windows."""
    return bool(get_vlc_window_titles())

def get_vlc_window_title():
    """Get the title of the first VLC window."""
    titles = get_vlc_window_titles()
    if titles:
        for title in titles:
            if "VLC media player" in title:
                return title.replace(" - VLC media player", "")
        return titles[0]
    return None
