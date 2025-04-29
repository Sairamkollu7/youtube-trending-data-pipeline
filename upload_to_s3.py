import boto3
import os
import datetime

# =========================
# Configuration Section
# =========================
BUCKET_NAME = 'youtube-trending-pipeline-bucket'  # 🔥 Replace with your real bucket name
RAW_FOLDER = 'raw/'  # Upload under 'raw/' folder

# Get latest file dynamically
files = [f for f in os.listdir('.') if f.startswith('trending_raw_') and f.endswith('.json')]
latest_file = max(files, key=os.path.getctime)

# =========================
# Upload Function
# =========================
def upload_file_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"[INFO] Successfully uploaded {file_name} to S3 bucket {bucket} as {object_name}")
    except Exception as e:
        print(f"[ERROR] Could not upload file. Error: {e}")

# =========================
# Main Execution
# =========================
if __name__ == "__main__":

    print(f"[DEBUG] Latest file detected: {latest_file}")
    print(f"[DEBUG] Uploading to Bucket: {BUCKET_NAME}, Key: {RAW_FOLDER + latest_file}")
    
    s3_key = RAW_FOLDER + latest_file
    upload_file_to_s3(latest_file, BUCKET_NAME, s3_key)
