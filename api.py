import os, urllib.parse, requests, pymysql

from dotenv import load_dotenv

load_dotenv()

con = pymysql.connect(host=os.getenv("RDS_URL"), port=3306, user=os.getenv("RDS_USERNAME"), password=os.getenv('RDS_PASSWORD'),
                       db=os.getenv("RDS_DATABASE_NAME"), charset="utf8", use_unicode=True, autocommit=True)

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search?"
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
params = {"key": YOUTUBE_API_KEY, "part": "snippet", "maxResults": 50, "q": "뉴진스 세로 직캠", "type": "video"}

responses = requests.get(YOUTUBE_API_URL + urllib.parse.urlencode(params))

# print(responses.json())
values = []

for item in responses.json()["items"]:
    values.append(f"('{item['id']['videoId']}', '{item['snippet']['title']}')")

cur = con.cursor()

sql = "insert into video(channel_id, title) VALUES " + ", ".join(values) + ";"

cur.execute(sql)
rows = cur.fetchall()

con.close()

print(rows)