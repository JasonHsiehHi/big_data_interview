interview for Big Data Co.,Ltd. 3/18

# API基本說明
請先進行管理員認證來取得JWT令牌資料(rest_framework_simplejwt)

curl -X POST \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "big_data"}' \
http://127.0.0.1:8000/api/token-auth/

return：
{
  "access":<your_access_token>,
  "refresh":<your_refresh_token>
}



管理員帳號： \
username:admin \
password:big_data

文章article的json格式範例： \
文章分為每日排名調查(type:Daily)與網路人氣話題(type:Popular)兩種
兩種類別的差別只在內容格式(content)

網路人氣話題文章:\
可依序自由插入小標題, 圖片, 文字內容, 提示字段...等 

故資料型態採用list: [\<sub_title>, \<content1>, \<content2>, \<img_src>,... ]

網路人氣話題(Popular): \
{
    "type": "Popular",  \
    "content": [
        "文／翁筠茜",
        "網紅夫妻Yun（周筠）與Dzingai（金該）...",
        "https://dvblobcdnjp.azureedge.net//Content/ueditor/net/upload1/2022-03/422fe628-3ab7-4d46-9bc2-7f51dd562b53.png",
        "Rice & Shine為何惹議？"
    ],\
    "headline": "60萬網紅夫妻怒槓網友！嗆「不想看就不要看」　網爆發退追潮 | 網路人氣話題", \
    "datePublished": "2022-03-01T16:00:00Z", \
    "dateModified": "2022-03-18T10:11:05.919916Z", \
    "description": "在Instagram上有超過60萬名粉絲的網紅夫妻「Rice &amp; Shine」近日爆發爭議。", \
    "url": "https://dailyview.tw/popular/detail/13784", \
    "thumbnailUrl": "https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2022-03/a50af24f-bf97-49e6-9bf4-b84cd3f4354a_m.jpg", \
    "dateCreated": "2022-03-18T10:11:05.919961Z",
    "articleSection": "娛樂", \
    "creator": "網路溫度計", \
    "keywords": [
        "Rice&Shine",
        "周筠",
        "金該",
        "公審",
        "爭議",
        "懶人包"
    ], \
    "image": <imageObject_id>,  \
    "author": <author_id>,  \
    "publisher": <publisher_id>  \
}

每日排名調查文章:\
則將不同排名的文字內容分成不同的區塊(text_box)，而每個區塊由標題(topic_title), 內容(content), 圖片(image)依序組成

故資料型態採用dict： {"top":[\<topic_title>,\<content>,\<image>], "rank10":[\<topic_title>,\<content>,\<image>], "rank9":...}

每日排名調查(Daily): \
{
    "type": "Daily",  \
    "content": {
        "top": [
            "自在遊走濕冷天氣",
            "天氣冷颼颼，又下雨真心超不想出門！...",
            "https://rab.equipment/uk/women-s-ladakh-gtx-jacket"
        ],
        "rank10": [
            "No.10Rab",
            "英國登山用品與服裝公司Rab...",
            "https://dvblobcdnjp.azureedge.net//Content/Upload/ThemeImages/2022-02/08b4e647-f002-407d-90ca-a7629c695ebc.png"
        ]
    },\
    "headline": "天雨冷吱吱都不怕！十大防風防水外套品牌伴你一路衝鋒 | 每日排名調查 | 第1頁 | DailyView 網路溫度計", \
    "datePublished": "2022-02-21T16:00:00Z", \
    "dateModified": "2022-03-18T10:38:35.256037Z", \
    "description": "力抗冷氣團！登山、戶外活動、雨天通勤都好用的十大防水防風外套品牌", \
    "url": "https://dailyview.tw/Daily/2022/02/22", \
    "thumbnailUrl": "https://dvblobcdnjp.azureedge.net//Content/Upload/DailyArticle/Images/2022-02/ae4d613f-7881-447e-b079-3aa0bae8cb5f_m.jpg", \
    "dateCreated": "2022-03-18T10:38:35.256085Z", \
    "articleSection": "旅遊", \
    "creator": "網路溫度計", \
    "keywords": [
        "GORETEX",
        "北臉",
        "防水外套",
        "防風外套",
        "始祖鳥",
        "歐都納",
        "機能外套"
    ], \
    "image": <imageObject_id>,  \
    "author": <author_id>,  \
    "publisher": <publisher_id>  \
}

所有API皆需要在header加上access_token:("Authorization: Bearer <your_access_token>")
1. 新增文章API (POST)
curl -X POST \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d <your_article_json_data>\
http://127.0.0.1:8000/api/article/


2. 刪除文章API (DELETE)
curl -X DELETE \
-H "Authorization: Bearer <your_access_token>" \
http://127.0.0.1:8000/api/article/<article_id>/


3. 修改文章API (PATCH)
curl -X PATCH \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d <article_json_data_for_update>\
http://127.0.0.1:8000/api/article/<article_id>/


4. 取得文章API (GET)
curl \
-H "Authorization: Bearer <your_access_token>" \
http://127.0.0.1:8000/api/article/<article_id>/

