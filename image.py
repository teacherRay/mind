from PIL import Image
import requests
from io import BytesIO

url = "https://1.bp.blogspot.com/-7qwH7C-RiEY/XcZDrwodqtI/AAAAAAAAUog/VSMQsn7Em-4BGNt1hvNDxu5-xrxbNwc6wCLcBGAsYHQ/s420-p/B86831DB-5E4E-48B6-A0E7-F2021B1DAB30.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
print(img)
img.show()