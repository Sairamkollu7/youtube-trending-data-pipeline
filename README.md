

# YouTube Trending Data Pipeline 📈

## Project Overview
This project extracts trending video data from the YouTube Data API, processes and cleans the data, stores it in AWS S3, and visualizes key insights using Power BI. It demonstrates a complete real-world Data Engineering ETL pipeline.

---

## Technologies Used
- **Python** (`requests`, `pandas`, `boto3`)
- **AWS S3** (Cloud Storage)
- **Apache Airflow** (Orchestration - optional later)
- **Power BI** (Dashboard Visualization)
- **YouTube Data API v3**

---

##  Project Architecture

```
[YouTube API] 
   ⬇️
[Raw Data Storage] (AWS S3 - raw folder)
   ⬇️
[ETL Scripts] (Python: extract.py, transform.py)
   ⬇️
[Processed Data Storage] (AWS S3 - processed folder)
   ⬇️
[Power BI Dashboard] (Visualization)
```

---
##  Project Flow

1. **Extraction**
   - Fetch trending video metadata from YouTube API.
   - Save raw JSON locally.
   - Upload raw JSON to AWS S3 (`raw/` folder).

2. **Transformation**
   - Clean and process the JSON data.
   - Extract key fields like `title`, `viewCount`, `categoryId`.
   - Handle missing data and create calculated fields.
   - Save cleaned data as CSV.
   - Upload processed CSV to AWS S3 (`processed/` folder).

3. **Visualization**
   - Build Power BI Dashboard:
     - Bar Chart: Top 10 videos by views
     - Pie Chart: Video distribution by category
     - Line Chart: View trends over publish dates

---

##  Dashboard Screenshots

| Top 10 Trending Videos | ![Top 10 Bar Chart](C:\Users\pandu\OneDrive\Desktop\youtube-trending-data-pipeline\Screenshots) |
| Distribution by Category | ![Pie Chart](C:\Users\pandu\OneDrive\Desktop\youtube-trending-data-pipeline\Screenshots) |
| Views Trend Over Time | ![Line Chart](C:\Users\pandu\OneDrive\Desktop\youtube-trending-data-pipeline\Screenshots) |



