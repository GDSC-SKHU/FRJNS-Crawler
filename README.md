# FRJNS Crawler

유튜브 API를 이용해 '뉴진스 세로 직캠'에 관련한 영상들을 크롤링 해줍니다.

[FRJNS API 서버](https://github.com/GDSC-SKHU/FRJNS-Backend)를 위해 만든 크롤러 입니다.

## How To Use

.env 파일을 생성하여 아래와 같은 템플릿을 지키며 작성합니다.

```
YOUTUBE_API_KEY={발급 받은 YOUTUBE API 전용 키}
RDS_URL={DB url}
RDS_DATABASE_NAME={DB 스키마 이름}
RDS_PASSWORD={DB 비밀번호}
RDS_USERNAME={DB 유저이름}
```

* Unix 계열 기준

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
python3 api.py
```