from pypresence import Presence
from config import TOKEN
import re
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
            # Remove anything before and including "|"
            title = re.sub(r".*\|", "", title).strip()

            # Remove file extensions
            title = re.sub(r"\.[a-zA-Z0-9]+$", "", title)  

            # Replace dots and underscores with spaces
            title = re.sub(r"[._]+", " ", title)

            # Capitalize words properly while preserving SxxExx format
            words = title.split()
            for i, word in enumerate(words):
                if re.match(r"^s\d{2}e\d{2}$", word, re.IGNORECASE):  # Keep SxxEyy format
                    words[i] = word.upper()
                else:
                    words[i] = word.capitalize()
            
            sanitized_title = " ".join(words)

            try:
                self.rpc.update(
                    details=f"{sanitized_title}",
                    large_image="vlc_for_ios_icon",
                    large_text=f"Watching: {sanitized_title}",
                )
                print(f"Updated Discord status: Watching {sanitized_title}")
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
