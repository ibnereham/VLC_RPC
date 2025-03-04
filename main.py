import time
from discord_rpc import DiscordRPC
from vlc_checker import is_vlc_window_open, get_vlc_window_title

def main():
    """Main loop to check VLC status and update Discord Rich Presence."""
    rpc = DiscordRPC()
    
    while True:
        if not rpc.connected:
            rpc.connect()

        if is_vlc_window_open():
            title = get_vlc_window_title()
            rpc.update_status(title)
        else:
            rpc.clear_status()

        time.sleep(15)

if __name__ == "__main__":
    main()
