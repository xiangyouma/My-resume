#!/usr/bin/env python3
import base64
import sys

# 讀取圖片檔案並轉換為 Base64
try:
    with open('d:/My-resume/images/profile.jpg', 'rb') as img_file:
        base64_str = base64.b64encode(img_file.read()).decode('utf-8')
        print(base64_str)
except FileNotFoundError:
    print("Error: Image file not found", file=sys.stderr)
    sys.exit(1)
