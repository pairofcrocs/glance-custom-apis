# Glance Custom API's

This is a collection of some of the APIs that I've built for the amazing [Glace dashboard](https://github.com/glanceapp/glance)

---

# Plex Stream Status Display

A web-based display for showing the status of active Plex streams, including user details, stream progress, and thumbnails. All via the Tautulli API

![image](https://github.com/user-attachments/assets/bfa668e8-10bc-4e9c-8511-87c1a04ea794)


## Features
- Displays active Plex streams with user information and playback details.
- Progress bar indicating the current playback position.
- Thumbnails from the Plex server with support for parent-level images.
- Conditional styling and hover tooltips for enhanced information display.
- Handles cases when no streams are active.

## Usage
1. Copy the content from "PlexStreams.yml" into your Glance.yml
2. Change the URL and API key of your Tautulli setup
3. Enjoy!

## Code Overview
### Key Functionalities
- **Active Streams:** Displays user name, device info, and playback progress.
- **Progress Bar:** Visual representation of playback percentage.
- **Thumbnails:** Uses `grandparent_thumb` if available, otherwise falls back to `thumb`.
- **Hover Tooltips:** Shows the episode name when hovering over the stream title.
- **No Active Streams:** Shows a default icon with specific classes when no streams are found.
  
## Troubleshooting
- Ensure network access to your Plex server.
- Verify API endpoint permissions.
- Double-check thumbnail paths for accuracy.

