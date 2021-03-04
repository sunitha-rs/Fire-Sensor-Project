import json
import requests
headers = {"Authorization": "Bearer ya29.A0AfH6SMDT0kPA5GxBnhMII2HkNv1q8OKgX2IPLhb2txdGeAccleVSbPvYwaYBI6Y8AOIvOuvxPVDlCf-Pu48rR5cCoUq0U3Qyff8QtIuH1McxTJObl6JUGrzX_fN70LT6ruBwE2ZCOolPN6kbkUaIsNRozI9A"}
para = {
    "name": "Samplefile.png",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./saved_img.jpg", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
