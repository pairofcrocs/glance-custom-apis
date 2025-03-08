# Glance Custom API's

This is a collection of some of the APIs that I've built for the amazing [Glace dashboard](https://github.com/glanceapp/glance)

---

# Plex Stream Status Display

A web-based display for showing the status of active Plex streams, including user details, stream progress, and thumbnails. All via the Tautulli API

![image](https://github.com/user-attachments/assets/bfa668e8-10bc-4e9c-8511-87c1a04ea794)
![image](https://github.com/user-attachments/assets/7d4081db-7411-4646-adde-ecdb95054848)

## Features
- Displays active Plex streams with user information and playback details.
- Progress bar indicating the current playback position.
- Thumbnails from the Plex server with support for parent-level images.
- Conditional styling and hover tooltips for enhanced information display.
- Handles cases when no streams are active.

## Usage
1. Copy the content from [PlexStreams.yml](https://raw.githubusercontent.com/pairofcrocs/glance-custom-apis/refs/heads/main/PlexStreams.yml) into your glance.yml
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

---

# Plex Stream Status Display - Minimal
![image](https://github.com/user-attachments/assets/c560072f-2306-4c92-aaa8-890f236706ca)
![image](https://github.com/user-attachments/assets/7d4081db-7411-4646-adde-ecdb95054848)

It's the same basic concept as the over Custom API (for the minimalists)

Copy the contents of [PlexStreamsMinimal.yml](https://raw.githubusercontent.com/pairofcrocs/glance-custom-apis/refs/heads/main/PlexStreamsMinimal.yml) into you glance.yml, edit the URL and replace with your Tautulli API key.

---

# Glance Private Tracker Widget
Adds a widget to Glance that monitors your private tracker accounts using Glance's custom API.

![image](https://github.com/user-attachments/assets/55c592ea-a48a-46cf-adbe-90ed20dd72fc)

Included are:

[PrivateTracker.yml](https://raw.githubusercontent.com/pairofcrocs/glance-custom-apis/refs/heads/main/PrivateTracker/PrivateTracker.yml) – Front-end code to integrate the widget into your Glance setup.

[FlaskServer.py](https://raw.githubusercontent.com/pairofcrocs/glance-custom-apis/refs/heads/main/PrivateTracker/FlaskServer.py) – A simple server to handle requests from the scraper script.


You should be able to spin up the server, and send requests to it via a POST request:
```
{
    "red_ratio": ****,
    "red_class": ****,
    "red_messages": ****,
    "btn_lumens": ****,
    "btn_bp": ****,
    "btn_hnr": ****
    "btn_messages": ****,
    "ggn_ratio": ****,
    "ggn_gold": ****,
    "ggn_messages": ****,
    "ptp_bonus": ****,
    "ptp_message": ****,
    "ptp_ratio": ****
}
```
---
For now, this repository focuses on the front end. The backend is currently a rough but functional Python script—I plan to refine and optimize it before making it publicly shareable. :)

