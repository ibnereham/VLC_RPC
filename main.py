import time
import threading
import requests
from discord_rpc import DiscordRPC
from vlc_checker import is_vlc_window_open, get_vlc_window_title
from pystray import Icon, MenuItem, Menu
from PIL import Image
from io import BytesIO


def fetch_vlc_icon():
    """Fetch the VLC logo from the internet."""
    url = "https://cdn1.iconfinder.com/data/icons/metro-ui-dock-icon-set--icons-by-dakirby/512/VLC_Media_Player.png"
    
    # Fetch the PNG file from the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Convert the PNG to an image object
        png_image = Image.open(BytesIO(response.content))
        
        # Flip the image upside down using the rotate method from PIL.Image
        flipped_image = png_image.rotate(180)
        return flipped_image
    else:
        raise Exception("Failed to fetch the VLC icon from the URL")


def update_tray_icon(icon, title):
    """Update tray icon text or tooltip."""
    icon.title = f"VLC - {title}"


def on_quit(icon, item):
    """Quit the application."""
    icon.stop()


def main_loop(rpc, icon):
    """Main loop to check VLC status and update Discord Rich Presence."""
    while True:
        if not rpc.connected:
            rpc.connect()

        if is_vlc_window_open():
            title = get_vlc_window_title()
            rpc.update_status(title)
            update_tray_icon(icon, title)  # Update tray icon with the VLC title
        else:
            rpc.clear_status()
            update_tray_icon(icon, "VLC not running")  # Update tray icon with status

        time.sleep(15)


def start_tray():
    """Start the system tray."""
    icon_image = fetch_vlc_icon()  # Get flipped VLC icon
    icon = Icon("VLC Rich Presence", icon_image, menu=Menu(MenuItem("Quit", on_quit)))
    thread = threading.Thread(target=main_loop, args=(rpc, icon))
    thread.daemon = True
    thread.start()
    icon.run()


if __name__ == "__main__":
    rpc = DiscordRPC()
    start_tray()
