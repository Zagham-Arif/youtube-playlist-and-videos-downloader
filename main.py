"""
YouTube Playlist Video Downloader
Downloads videos from a YouTube playlist with specified index range.  
"""

import yt_dlp
import os


def download_single_videos(video_urls, output_path='downloads'):
    """
    Download individual YouTube videos (not playlists).
    
    Args:
        video_urls: List of video URLs to download
        output_path: Directory to save downloaded videos (default: 'downloads')
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Configure yt-dlp options
    ydl_opts = {
        # Format selection - use a more compatible format
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Output template (no playlist_index for single videos)
        'outtmpl':  os.path.join(output_path, '%(title)s.%(ext)s'),
        
        # Error handling
        'ignoreerrors': True,  # Continue on download errors
        'no_warnings':  False,
        
        # No playlist mode - only download the single video
        'noplaylist': True,
        
        # Download options
        'continuedl': True,  # Resume downloads
        'retries': 10,  # Retry failed downloads
        'fragment_retries': 10,  # Retry failed fragments
        
        # Post-processing
        'merge_output_format': 'mp4',  # Merge to mp4 if needed
        
        # Workaround for YouTube issues
        'extractor_args': {
            'youtube':  {
                'player_client': ['android', 'web'],
                'player_skip':  ['webpage', 'configs'],
            }
        },
        
        # Additional options
        'writethumbnail': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        
        # Verbose output
        'verbose': False,
        'quiet': False,
        'no_color': False,
        
        # Progress hooks
        'progress_hooks': [download_progress_hook],
    }
    
    print(f"Starting download of {len(video_urls)} video(s)...")
    print(f"Output directory: {os.path.abspath(output_path)}")
    print("-" * 60)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download videos
            error_code = ydl.download(video_urls)
            
        print("-" * 60)
        if error_code == 0:
            print("✓ Download completed successfully!")
        else:
            print("⚠ Download completed with some errors.  Check the output above.")
        
    except Exception as e:
        print(f"✗ An error occurred: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Make sure yt-dlp is updated:  pip install --upgrade yt-dlp")
        print("2. Check your internet connection")
        print("3. Verify the video URLs are correct")


def download_youtube_playlist(playlist_url, start_index=1, end_index=52, output_path='downloads'):
    """
    Download videos from a YouTube playlist. 
    
    Args:
        playlist_url:  Base URL of the playlist
        start_index: Starting video index (default: 1)
        end_index: Ending video index (default: 52)
        output_path: Directory to save downloaded videos (default: 'downloads')
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Configure yt-dlp options
    ydl_opts = {
        # Format selection - use a more compatible format
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Output template
        'outtmpl':  os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        
        # Error handling
        'ignoreerrors': True,  # Continue on download errors
        'no_warnings':  False,
        
        # Playlist options
        'playlist_items': f'{start_index}-{end_index}',
        'noplaylist': False,
        
        # Download options
        'continuedl': True,  # Resume downloads
        'retries': 10,  # Retry failed downloads
        'fragment_retries': 10,  # Retry failed fragments
        
        # Post-processing
        'merge_output_format': 'mp4',  # Merge to mp4 if needed
        
        # Workaround for YouTube issues
        'extractor_args': {
            'youtube':  {
                'player_client': ['android', 'web'],
                'player_skip':  ['webpage', 'configs'],
            }
        },
        
        # Additional options
        'writethumbnail': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        
        # Verbose output
        'verbose': False,
        'quiet': False,
        'no_color': False,
        
        # Progress hooks
        'progress_hooks': [download_progress_hook],
    }
    
    print(f"Starting download of videos {start_index} to {end_index}...")
    print(f"Output directory: {os.path.abspath(output_path)}")
    print("-" * 60)
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download videos directly
            error_code = ydl.download([playlist_url])
            
        print("-" * 60)
        if error_code == 0:
            print("✓ Download completed successfully!")
        else:
            print("⚠ Download completed with some errors.  Check the output above.")
        
    except Exception as e:
        print(f"✗ An error occurred: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Make sure yt-dlp is updated:  pip install --upgrade yt-dlp")
        print("2. Check your internet connection")
        print("3. Verify the playlist URL is correct")


def download_progress_hook(d):
    """Hook to show download progress"""
    if d['status'] == 'downloading': 
        filename = os.path.basename(d['filename'])
        # Truncate long filenames
        if len(filename) > 45:
            filename = filename[:42] + '...'
        
        percent = d. get('_percent_str', 'N/A').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        
        # Clear line and print progress
        print(f"\r{' ' * 100}", end='')  # Clear previous line
        print(f"\r  └─ {percent} of {filename} | {speed} | ETA: {eta}", end='', flush=True)
        
    elif d['status'] == 'finished':
        filename = os.path.basename(d['filename'])
        if len(filename) > 45:
            filename = filename[:42] + '...'
        print(f"\r{' ' * 100}", end='')  # Clear progress line
        print(f"✓ Downloaded: {filename}")
        
    elif d['status'] == 'error':
        print(f"\n✗ Error downloading file")


def main():
    print("=" * 60)
    print("   YouTube Playlist Downloader")
    print("=" * 60)
    
    # Ask mode: playlist or individual videos
    print("\nSelect download mode:")
    print("  1. Download from playlist")
    print("  2. Download individual video(s)")
    
    while True:
        mode = input("\nEnter choice (1 or 2): ").strip()
        if mode in ['1', '2']:
            break
        print("✗ Invalid choice. Please enter 1 or 2.")
    
    if mode == '1':
        # Playlist mode
        playlist_url = input("\nEnter YouTube playlist URL: ").strip()
        
        if not playlist_url:
            print("✗ Error: Playlist URL cannot be empty!")
            return
        
        # Get start index
        while True:
            start_input = input("Enter start index (default: 1): ").strip()
            if not start_input:
                START_INDEX = 1
                break
            try:
                START_INDEX = int(start_input)
                if START_INDEX < 1:
                    print("✗ Start index must be at least 1. Try again.")
                    continue
                break
            except ValueError:
                print("✗ Invalid number. Try again.")
        
        # Get end index
        while True:
            end_input = input("Enter end index (default: 100): ").strip()
            if not end_input:
                END_INDEX = 100
                break
            try:
                END_INDEX = int(end_input)
                if END_INDEX < START_INDEX:
                    print(f"✗ End index must be at least {START_INDEX}. Try again.")
                    continue
                break
            except ValueError:
                print("✗ Invalid number. Try again.")
        
        # Get output folder
        folder_input = input("Enter output folder (default: downloaded_videos): ").strip()
        OUTPUT_FOLDER = folder_input if folder_input else "downloaded_videos"
        
        print("\n" + "=" * 60)
        print("Download Configuration:")
        print(f"  Mode: Playlist")
        print(f"  Playlist URL: {playlist_url}")
        print(f"  Videos to download: {START_INDEX}-{END_INDEX}")
        print(f"  Output folder: {OUTPUT_FOLDER}")
        print("=" * 60)
        
        # Confirm before starting
        confirm = input("\nStart download? (y/n): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("Download cancelled.")
            return
        
        print()
        
        # Start download
        download_youtube_playlist(
            playlist_url=playlist_url,
            start_index=START_INDEX,
            end_index=END_INDEX,
            output_path=OUTPUT_FOLDER
        )
        
    else:
        # Individual videos mode
        print("\nEnter video URLs (one per line).")
        print("When done, enter a blank line or type 'done':")
        
        video_urls = []
        while True:
            url = input(f"  Video {len(video_urls) + 1}: ").strip()
            if not url or url.lower() == 'done':
                break
            video_urls.append(url)
        
        if not video_urls:
            print("✗ Error: No video URLs provided!")
            return
        
        # Get output folder
        folder_input = input("\nEnter output folder (default: downloaded_videos): ").strip()
        OUTPUT_FOLDER = folder_input if folder_input else "downloaded_videos"
        
        print("\n" + "=" * 60)
        print("Download Configuration:")
        print(f"  Mode: Individual Videos")
        print(f"  Number of videos: {len(video_urls)}")
        print(f"  Output folder: {OUTPUT_FOLDER}")
        print("  URLs:")
        for i, url in enumerate(video_urls, 1):
            print(f"    {i}. {url}")
        print("=" * 60)
        
        # Confirm before starting
        confirm = input("\nStart download? (y/n): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("Download cancelled.")
            return
        
        print()
        
        # Start download
        download_single_videos(
            video_urls=video_urls,
            output_path=OUTPUT_FOLDER
        )
    
    print("\n" + "=" * 60)
    print(f"All files saved to: {os.path.abspath(OUTPUT_FOLDER)}")
    print("=" * 60)


if __name__ == "__main__": 
    main()