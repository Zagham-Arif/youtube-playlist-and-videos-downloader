# YouTube Downloader

A flexible Python script to download videos from YouTube - supports both playlists and individual videos.

## Features

✨ **Two Download Modes:**
- **Playlist Mode**: Download specific ranges from YouTube playlists
- **Individual Videos Mode**: Download multiple single videos at once

🎯 **Key Features:**
- Interactive command-line interface
- Resume interrupted downloads
- Automatic retries on failed downloads
- Custom output folder selection
- Progress tracking with live updates
- MP4 format output (compatible with most devices)
- Error handling with informative messages

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this repository**

2. **Set up the virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install:
   ```bash
   pip install yt-dlp
   ```

## Usage

### Quick Start

1. Activate the virtual environment (if you created one):
   ```bash
   source venv/bin/activate  # On Linux/Mac
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

3. Follow the interactive prompts!

### Mode 1: Playlist Download

Perfect for downloading lecture series, course playlists, or any YouTube playlist.

**Example:**
```
Select download mode:
  1. Download from playlist
  2. Download individual video(s)

Enter choice (1 or 2): 1

Enter YouTube playlist URL: https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID
Enter start index (default: 1): 1
Enter end index (default: 100): 52
Enter output folder (default: downloaded_videos): my_lectures

Start download? (y/n): y
```

**Features:**
- Download specific ranges (e.g., videos 1-52)
- Files are numbered with playlist index
- Perfect for organized series

### Mode 2: Individual Videos

Great for downloading specific videos that aren't in a playlist.

**Example:**
```
Select download mode:
  1. Download from playlist
  2. Download individual video(s)

Enter choice (1 or 2): 2

Enter video URLs (one per line).
When done, enter a blank line or type 'done':
  Video 1: https://www.youtube.com/watch?v=abc123
  Video 2: https://www.youtube.com/watch?v=xyz789
  Video 3: [Press Enter or type 'done']

Enter output folder (default: downloaded_videos): single_videos

Start download? (y/n): y
```

**Features:**
- Add as many video URLs as you want
- All downloaded to the same folder
- Files use video titles as filenames

## Configuration

The script uses these default settings:
- **Start Index**: 1
- **End Index**: 100
- **Output Folder**: `downloaded_videos`
- **Video Format**: Best quality MP4
- **Retries**: 10 attempts for failed downloads
- **Resume**: Automatically resumes interrupted downloads

You can change these defaults during runtime through the interactive prompts.

## Output File Naming

- **Playlist Mode**: `01 - Video Title.mp4`, `02 - Video Title.mp4`, etc.
- **Individual Videos Mode**: `Video Title.mp4`

## Troubleshooting

### Common Issues

**1. "ERROR: Space not allowed in string format specifier"**
- This has been fixed in the latest version
- Make sure you're using the updated `main.py`

**2. Download fails with HTTP 403 or similar errors**
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Check your internet connection
- Verify the URL is correct and the video is publicly accessible

**3. "ModuleNotFoundError: No module named 'yt_dlp'"**
- Install dependencies: `pip install -r requirements.txt`
- Or: `pip install yt-dlp`

**4. Slow download speeds**
- This depends on your internet connection
- YouTube may throttle download speeds
- Try downloading during off-peak hours

**5. Partial downloads (.part files)**
- The script automatically resumes these on the next run
- Delete .part files only if you want to restart a download

### Getting Help

If you encounter issues:
1. Make sure yt-dlp is up to date: `pip install --upgrade yt-dlp`
2. Check that the video/playlist is publicly accessible
3. Verify your Python version: `python3 --version` (should be 3.6+)
4. Check your internet connection

## Advanced Usage

### Running Without Confirmation

If you want to skip the confirmation step, you can modify the script or pipe 'y' to it:
```bash
echo "y" | python3 main.py
```

### Updating yt-dlp

YouTube frequently changes its API. Keep yt-dlp updated:
```bash
pip install --upgrade yt-dlp
```

## Project Structure

```
youtube-downloader/
├── main.py                 # Main script
├── requirements.txt        # Python dependencies
├── setup.sh               # Setup script (if available)
├── README.md              # This file
└── downloaded_videos/     # Default output folder
```

## Dependencies

- **yt-dlp**: Modern YouTube downloader (fork of youtube-dl with active development)

## Legal Notice

⚠️ **Important**: This tool is for personal use only. 

- Respect copyright laws and YouTube's Terms of Service
- Only download videos you have permission to download
- Do not distribute copyrighted content
- Some content may be protected by copyright

## License

This project is provided as-is for educational and personal use.

## Contributing

Feel free to fork, modify, and improve this script for your personal use!

---

**Happy Downloading! 🎥**
