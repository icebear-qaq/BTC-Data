# BTC_USDT 5-Minute Kline Data Downloader

This script downloads the BTC_USDT 5-minute kline data for the last 18 months from a specified URL and saves it to a local directory. It skips downloading files that already exist in the target directory.

## Features
- Downloads BTC_USDT 5-minute kline data for the last 18 months.
- Skips files that have already been downloaded.
- Creates a directory to store downloaded files if it doesn't exist.

## Requirements
- Python 3.x
- `requests` library

To install the required library, run:
```bash
pip install requests