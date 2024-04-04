from django.shortcuts import render

# Create your views here.

# def show_seoyoung(request) :
#     # return render(request, 'ugeoji/seoyoung.html')
#     # context = group_context['members'][0]
#     context = list(filter(lambda member : '이서영' in member['name'], group_context['members']))[0]
#     return render(request, 'ugeoji/member.html', context=context)
#
# def show_haewon(request) :
#     # return render(request, 'ugeoji/haewon.html')
#     # context = group_context['members'][1]
#     context = list(filter(lambda member: '이해원' in member['name'], group_context['members']))[1]
#     return render(request, 'ugeoji/member.html', context=context)
#
# def show_seohyeon(request) :
#     # return render(request, 'ugeoji/seohyeon.html')
#     # context = group_context['members'][2]
#     context = list(filter(lambda member: '조서현' in member['name'], group_context['members']))[2]
#     return render(request, 'ugeoji/member.html', context=context)

def show_멤버(request, 멤버):
    context = list(filter(lambda member: 멤버 in member['name'], group_context['members']))[0]
    return render(request, 'ugeoji/멤버.html', context=context)

group_context = {
    'members' : [

        {
            'group_name' : '우거지',
            'name' : '이서영',
            'nick_name' : '이서영(정치인)',
            # 'img_src' : 'https://gdimg.gmarket.co.kr/1655620556/still/400?ver=1593073519'
            'img_src' : 'ugeoji/images/이서영.jpg'
        },

        {
            'group_name': '우거지',
            'name': '이해원',
            'nick_name': '이해원(이순재)',
            # 'img_src': 'data:image/jpeg;base64,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'
            'img_src' : 'ugeoji/images/이해원.jpg'
        },

        {
            'group_name': '우거지',
            'name': '조서현',
            'nick_name': '조서현(봉태규)',
            # 'img_src': 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202103/19/e57754ef-779b-4217-9e82-f3d63b96f93a.jpg'
            'img_src' : 'ugeoji/images/조서현.jpg'
        }

    ]
}