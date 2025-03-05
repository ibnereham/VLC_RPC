# VLC Discord Rich Presence

A simple Rich Presence integration for VLC Media Player that updates your Discord status with the currently playing media.

## Features
- Displays the currently playing media title in your Discord status.
- Automatically updates when the media changes.
- Stops displaying when VLC is closed.

## Installation

### Option 1: Running the Python Script

1. **Download the repository:**
   - Go to the [GitHub Repository](https://github.com/ibnereham/VLC_RPC).
   - Click the **"Code"** button and select **"Download ZIP"** to download the repository.
   
2. **Extract the repository:**
   - Extract the contents of the ZIP file to a location of your choice, for example `C:\VLC-RPC`.

3. **Set up the Python script:**
   - Inside the extracted folder, find the `main.py` script.
   - Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org).
   - Open Command Prompt and run the following command to install dependencies:
     ```
     pip install -r C:\VLC-RPC\requirements.txt
     ```

4. **Set up the environment file:**
   - Open the `config.py` file in the same directory as `main.py`.
   
   - Replace `your_client_id_here` with the actual Client ID from Discord.

5. **Create a shortcut for startup (Python Script):**
   - Press `Win + R`, type `shell:startup`, and hit `Enter`.
   - Create a shortcut for the `VLC_RPC.py` script in the `Startup` folder:
     - Right-click inside the `Startup` folder, select **New** → **Shortcut**.
     - For the location, enter:
       ```
       python C:\VLC-RPC\main.py
       ```
     - Click **Next**, name the shortcut, and click **Finish**.

### **Option 2: Running the Executable (.exe) File (Manually Compiled)**  
1. **Set up the environment file:**
   - Open the `config.py` file in the same directory as `main.py`.
   
   - Replace `your_client_id_here` with the actual Client ID from Discord.

2. **Manually Compile the Executable:**  
   - Open Command Prompt and navigate to your script directory:  
     ```sh
     cd C:\VLC-RPC
     ```
   - Run the following command to compile the script:  
     ```sh
     pyinstaller --onefile --noconsole --name=VLC_RPC main.py
     ```
   - After compilation, the executable will be in the `dist` folder:  
     ```
     C:\VLC-RPC\dist\VLC_RPC.exe
     ```
   - Move `VLC_RPC.exe` to a location like `C:\VLC-RPC`.



3. **Create a Shortcut for Startup (Executable):**  
   - Press `Win + R`, type `shell:startup`, and hit `Enter`.  
   - Create a shortcut for `VLC_RPC.exe` in the `Startup` folder:  
     - Right-click inside the `Startup` folder, select **New** → **Shortcut**.  
     - For the location, enter:  
       ```
       C:\VLC-RPC\VLC_RPC.exe
       ```
     - Click **Next**, name the shortcut, and click **Finish**.  

---

Now, every time you start Windows, the manually compiled `VLC_RPC.exe` will run automatically.


## How to Run

1. **Create a Discord Application:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and give it a name ("VLC MEDIA PLAYER" is a good choice).
   - Navigate to "Rich Presence" and set up the necessary assets (like icons).
   - Copy the "Client ID" from the application page.
   - Goto the "config.py" and replace the "here" in `TOKEN="here"` to the Client ID you have copied from the application page.

2. **Run the application:**
   - If using the script, run `VLC_RPC.py`.
   - If using the executable, run `VLC_RPC.exe`.
   - Start VLC Media Player and play a video.
   - Check your Discord status for the media information.

## Notes
- Make sure Discord is running before launching the RPC.
- If the status does not update, restart both VLC and Discord.

## License
This project is open-source under the MIT License.

