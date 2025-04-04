# send_data.py
import requests
import random
import time

while True:
    data = {
        'a': random.randint(1, 100),
        'b': random.randint(101, 200),
        'c': random.randint(201, 300)
    }
    try:
        res = requests.post('https://flask-web-lh04.onrender.com/update', json=data)
        print('已上传数据:', data, '状态:', res.status_code)
    except Exception as e:
        print('上传失败:', e)
    
    time.sleep(1)  # 每秒上传一次
