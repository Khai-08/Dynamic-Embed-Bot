# Dynamic Embed Bot

A **Discord bot** that dynamically updates embeds with the **dominant color** of a **Roblox game icon**. The bot fetches the latest game thumbnail, extracts the dominant color, and updates the embed in real time.

## Features
✅ Responds when **mentioned**, showing the extracted embed color for debugging.  
✅ Sends periodic updates in a specific **Discord channel**.  
✅ Extracts **dominant color** and applies it to the embed.  
✅ Fetches **latest game icon** from Roblox.  

## Setup & Installation

### 1. Clone the Repository

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Create a `.env` File
Inside the project directory, create a file named `.env` and add the following:  


### 4. Run the Bot
python main.py

## How It Works
- The bot **periodically fetches** the latest game thumbnail.  
- It extracts the **dominant color** using `ColorThief` library.  
- The embed updates dynamically and gets posted in the **specified channel**.  
- If you mention the bot, it sends a **debug embed** showing the extracted color.

## Troubleshooting
🛠 If the bot doesn't start:  
- **Check your `.env` file** for missing variables.  
- **Ensure the bot has permission** to send messages in the channel.  
- **Verify your Python version** (recommended: Python 3.10+).  

## Contributing
Pull requests are welcome! Feel free to suggest improvements or report bugs.

## License
📜 MIT License.
