import os
import requests
from datetime import datetime, timedelta

# 基础URL
base_url = "https://d2s4an60yebwep.cloudfront.net/SPOT2/kline/2fb942154ef44a4ab2ef98c8afb6a4a7/daily/Min5/"

# 文件保存目录
save_dir = "downloads"

# 创建保存目录
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 开始日期和结束日期
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# 遍历日期范围
current_date = start_date
while current_date <= end_date:
    # 生成文件名
    file_name = f"BTC_USDT-Min5-{current_date.strftime('%Y-%m-%d')}.csv"
    file_url = base_url + file_name

    # 下载文件
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(os.path.join(save_dir, file_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}")

    # 增加一天
    current_date += timedelta(days=1)

print("All files downloaded.")