# helloidol

---

1. startproject helloidol
    1. python -m pip install django~=4.2
    2. django-admin startproject _helloidol_ .
    3. [python manage.py migrate]
    4. python manage,py runserver
2. startapp _playeground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. hellidol/settings.py
      1. 'playground',in INSTALLED_APPS
3. playground/
   - 정보 전달 : urls -> views -> (models ->)templates
   - 코드 작성 : (models -> )views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp 우거지
   1. Terminal
      1. python manage.py startapp 우거지
   2. helloidol/settings.py
      1. '우거지', in INSTALLED_APPS
6. 우거지/
   1. views
      1. show_서영()
      2. show_해원()
      3. show_서현()
      4. -> templates에 context 전달
   2. templates/우거지/
      1. ~~서영.html~~
         1. title : 우거지 - 서영
         2. h1 : 우거지
         3. h2 : 서영
         4. img : 서영 프로필 사진
            1. border-radius : 50%;
      2. ~~해원.html~~
         1. title : 우거지 - 해원
         2. h1 : 우거지
         3. h2 : 해원
         4. img : 해원 프로필 사진
            1. border-radius : 50%;
      3. ~~서현.html~~
         1. title : 우거지 - 서현
         2. h1 : 우거지
         3. h2 : 서현
         4. img : 서현 프로필 사진
            1. border-radius : 50%;
      4. 멤버.html
         1. group_name, name, img_src
   3. urls
      1. 우거지/ -> 서영 / -> show_서영()
      2. 우거지/ -> 해원 / -> show_해원()
      3. 우거지/ -> 서현 / -> show_서현()