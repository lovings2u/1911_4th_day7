from django.shortcuts import render

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
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id = 'ZkmcJL1WAP4spgU6Pv4x'
    client_secret = 'MD72fRu0Pe'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = json.dumps(query)

    response = requests.post(url, headers=headers, data=params)

    result = response.text

    context = {
        'result': result
    }

    return render(request, 'result.html', context)