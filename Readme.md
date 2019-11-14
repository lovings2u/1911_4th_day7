# Day7

- Naver Api 사용하기

  - 검색어 트랜드api 사용하기

  - [참조 문서]( https://developers.naver.com/products/datalab/ )

  - 해당 Api는 request를 보낼 때 POST 방식을 사용하고, 파라미터를 json형식으로 보낸다. 기존의 query  string으로 보내는 방법과 다르기 때문에 주의해서 사용해야 한다.

  - `django-admin startproject naverapi`

  - `cd naverapi`

  - `python manage.py search_trend`

  - ```python
    # settings.py
    INSTALLED_APPS = [
        'search_trend',
    	...
    ]
    ```

  - ```python
    # urls.py
    
    from search_trend import views as search_trend_view
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        # 검색어를 입력하는 곳
        path('search/', search_trend_view.search),
        # 검색어에 대한 트랜드 결과를 받는 곳
        path('search/result', search_trend_view.result)
    
    ]
    ```

  - ```python
    # search_trend.views.py
    
    import json
    import requests
    
    # Create your views here.
    def search(request):
        # 검색어를 입력하는 곳
        return render(request, 'search.html')
    
    def result(request):
        # 검색어에 대한 검색 트랜드를 받아보는 곳
        start_date = request.GET['search_start_date']
        end_date = request.GET['search_end_date']
        time_unit = request.GET['search_time_unit']
        group_name = request.GET['search_group_name']
        keywords = request.GET['search_keywords'].split(',')
        
        query = {
            "startDate": start_date,
            "endDate": end_date,
            "timeUnit": time_unit,
            "keywordGroups": [
                {
                    "groupName": group_name,
                    "keywords": keywords
                }
            ]
        }
        # json 형식으로 요청 파라미터를 보내기 위해 딕셔너리를 선언하여 Naver Api에서 정해준 형식으로 요청을 보낸다.
        url = 'https://openapi.naver.com/v1/datalab/search'
        client_id = 'Client-Id'
        client_secret = 'Secret-Key'
    
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret
        }
        # 딕셔너리 형식으로 만들어진 변수를 json으로 변환하기 위해 json.dumps를 사용한다.
        params = json.dumps(query)
    	# 요청 방식이 POST인 경우 params가 아닌 data로 매개변수를 보낸다.
        response = requests.post(url, headers=headers, data=params)
    
        result = response.text
    
        context = {
            'result': result
        }
    
        return render(request, 'result.html', context)
    ```

  - ```html
    <!-- search.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>
            검색어를 입력하세요.
        </h1>
        <form action="/search/result">
            <label>기간 시작날짜</label>
            <input type="date" name="search_start_date">
            <br/>
            <label>기간 종료날짜</label>
            <input type="date" name="search_end_date">
            <br/>
            <label>구간 단위</label>
            <select name="search_time_unit">
                <option value="date">일간</option>
                <option value="week">주간</option>
                <option value="month">월간</option>
            </select>
            <br/>
            <label>검색어 그룹명</label>
            <input type="text" name="search_group_name">
            <br/>
            <label>트랜드를 볼 검색어 목록(여러개의 검색어의 경우 ','로 구분한다)</label>
            <input type="text" name="search_keywords">
            <br/>
            <input type="submit" value="트랜드 보기">
        </form>
    </body>
    </html>
    ```

  - ORM

    - Object Relationship Mapping

    - DBMS를 활용하기 위해 사용하는 SQL을 python 문법으로 똑같게 사용할 수 있도록 하는 것.

    - [관련자료]( https://velog.io/@kyusung/aboutORM )

    - 먼저 마이그레션을 만들어 DB의 구조를 만들어 반영하고 마이그레이트로 실제 DB에 반영한다.

    - `python manage.py startapp boards`

    - ```python
      # boards/models.py
      from django.db import models
      
      # Create your models here.
      class Board(models.Model):
          title = models.CharField(max_length=30)
          contents = models.TextField()
          creator = models.CharField(max_length=10, null=True)
      
      ```

    - [필드 종류 관련]( https://docs.djangoproject.com/en/2.2/ref/models/fields/#integerfield )

    - `python manage.py makemigrations`

    - `python manage.py migrate`

    - ```python
      # python Shell
      > python manage.py shell
      > from boards.models import Board
      > b = Board() # 실제 DB에 반영되지 않고 객체를 만들어 조작
      > b.title = '오레오 맛있다.'
      > b.contents = '내일도 먹고싶다.'
      > b.save() # 실제 DB에 반영
      ```