# helloidol2
---
1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > Settings... > Language & Frameworks > Django > [v] Enable Django Support
   4. Run > Edit Configurations... > + > Django Server > Name : runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp 로보카폴리
   1. python manage.py startapp 로보카폴리
   2. '로보카폴리', in INSTALLED_APPS in settings.py
3. 로보카폴리/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
         2. `__str__()` : 객체를 출력할 때, 알맞은 string으로 출력하자.
         3. `get_absolute_url()` : 캐릭터 하나 데이터 가져오자.
      2. python manage.py makemigrations 로보카폴리
      3. python manage.py migrate 로보카폴리
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R: CharacterListView
      2. R: CharacterDetailView
      3. C: CharacterCreateView
      4. U: CharacterUpdateView
   4. templates/로보카폴리/
      1. character_list.html
      2. character_detail.html
      3. character_create.html
      4. character_update.html
   5. urls
      1. 로보카폴리:character_list
      2. 로보카폴리:character_detail
      3. 로보카폴리:character_create
      4. 로보카폴리:character_update
4. templates/
   1. base.html
      1. settings.py > TEMPLATES
         1. 'DIRS': [BASE_DIR / 'templates']