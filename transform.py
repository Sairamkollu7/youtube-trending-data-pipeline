import pandas as pd
import json
import os
import boto3
import datetime

# =========================
# Configuration Section
# =========================
BUCKET_NAME = 'youtube-trending-pipeline-bucket'  # 🔥 Replace with your real bucket name
RAW_FOLDER = 'raw/'
PROCESSED_FOLDER = 'processed/'

# Detect the latest raw file
files = [f for f in os.listdir('.') if f.startswith('trending_raw_') and f.endswith('.json')]
latest_raw_file = max(files, key=os.path.getctime)

# Generate name for processed CSV
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
processed_file_name = f"trending_processed_{timestamp}.csv"

# =========================
# Data Cleaning Function
# =========================
def clean_trending_data(raw_file, processed_file):
    with open(raw_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    videos = []
    for item in data.get('items', []):
        snippet = item.get('snippet', {})
        stats = item.get('statistics', {})
        
        video = {
            'title': snippet.get('title'),
            'publishedAt': snippet.get('publishedAt'),
            'categoryId': snippet.get('categoryId'),
            'viewCount': stats.get('viewCount'),
            'likeCount': stats.get('likeCount')
        }
        
        videos.append(video)
    
    df = pd.DataFrame(videos)
    
    # Data cleaning
    df.dropna(inplace=True)
    df['viewCount'] = df['viewCount'].astype(int)
    df['likeCount'] = df['likeCount'].astype(int)
    df['views_in_million'] = df['viewCount'] / 1_000_000
    
    df.to_csv(processed_file, index=False)
    print(f"[INFO] Processed file created: {processed_file}")

# =========================
# Upload Function
# =========================
def upload_to_s3(file_name, bucket, s3_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, s3_key)
        print(f"[INFO] Successfully uploaded {file_name} to S3 as {s3_key}")
    except Exception as e:
        print(f"[ERROR] Upload failed: {e}")

# =========================
# Main Execution
# =========================
if __name__ == "__main__":
    print(f"[DEBUG] Cleaning file: {latest_raw_file}")
    clean_trending_data(latest_raw_file, processed_file_name)
    
    print(f"[DEBUG] Uploading cleaned file to S3...")
    s3_key = PROCESSED_FOLDER + processed_file_name
    upload_to_s3(processed_file_name, BUCKET_NAME, s3_key)
