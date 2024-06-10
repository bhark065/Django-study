from django.shortcuts import render

# Create your views here.
def show_chart(reqeust):
    with open('data/data.json', 'r', encoding='utf-8') as file:
        import json
        json_data = json.load(file)
    # data.json : name, price, ctgColor별로 데이터 분리하기
    name = [item['name'] for item in json_data]
    price = [item['price'] for item in json_data]
    ctgColor = [item['ctgColor'] for item in json_data]
    context = {
        # 'json_data': json_data, # 전체 데이터 불러오기
        'name': name,
        'price': price,
        'ctgColor': ctgColor
    }
    return render(reqeust, 'chart_test/chart_view.html', context=context)
