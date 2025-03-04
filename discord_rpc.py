from pypresence import Presence
from config import TOKEN
class DiscordRPC:
    def __init__(self):
        self.client_id = TOKEN  # Replace with your Discord client ID
        self.rpc = Presence(self.client_id)
        self.connected = False

    def connect(self):
        """Connect to Discord RPC."""
        try:
            self.rpc.connect()
            self.connected = True
            print("Connected to Discord RPC.")
        except Exception as e:
            print(f"Failed to connect to Discord: {e}")
            self.connected = False

    def update_status(self, title):
        """Update Discord status with VLC title."""
        if self.connected and title:
            try:
                self.rpc.update(
                    details=f"Watching: {title}",
                    large_image="vlc_for_ios_icon",
                    large_text="VLC Media Player",
                )
                print(f"Updated Discord status: Watching {title}")
            except Exception as e:
                print(f"Error updating Discord status: {e}")
                self.connected = False
                self.rpc.close()

    def clear_status(self):
        """Clear Discord Rich Presence."""
        if self.connected:
            try:
                self.rpc.clear()
                print("Cleared Discord status.")
            except Exception as e:
                print(f"Error clearing status: {e}")
                self.connected = False
                self.rpc.close()
