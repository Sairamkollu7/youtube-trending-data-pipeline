import requests # type: ignore
import json
import datetime

# =========================
# Configuration Section
# =========================
API_KEY = 'AIzaSyA7GAFfsxWpsVZTsbGKyCY-_jwiXfG8si4'  # 🔥 <-- REPLACE this with your actual YouTube API Key
REGION_CODE = 'US'  # Change this to your target region (example: 'IN' for India)

# YouTube API Endpoint
YOUTUBE_TRENDING_URL = (
    f"https://www.googleapis.com/youtube/v3/videos"
    f"?part=snippet,statistics"
    f"&chart=mostPopular"
    f"&regionCode={REGION_CODE}"
    f"&maxResults=50"
    f"&key={API_KEY}"
)

# Output filenames
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"trending_raw_{timestamp}.json"


# =========================
# Function to Fetch Data
# =========================
def fetch_trending_videos():
    response = requests.get(YOUTUBE_TRENDING_URL)

    if response.status_code == 200:
        data = response.json()
        print(f"[INFO] Successfully fetched {len(data['items'])} videos.")
        
        # Save to local JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"[INFO] Raw trending data saved to {output_file}")
    
    else:
        print(f"[ERROR] Failed to fetch trending videos. Status Code: {response.status_code}")
        print(f"Reason: {response.text}")


# =========================
# Main Execution
# =========================
if __name__ == "__main__":
    fetch_trending_videos()
