import requests
url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=D162B6E0-77BB-4E1F-99A6-E3F44A0503BF'
try:
    response = requests.get(url)
    response.raise_for_status()
except Exception as e:
    print(e)
else:
    print(response.text)