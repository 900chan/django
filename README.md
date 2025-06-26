# Django (25.06.16 ~ 07.04)

---
Django 과목을 수강하면서 일차별 배운 내용을 추가하는 README 연습입니다.

--- 
## _Day 1_ : Django 프로젝트 세팅

- - -

1. python 설치 & 프로젝트 세팅  ([Download Python | Python.org](https://www.python.org/downloads/))

````
mkdir django # 프로젝트 파일 생성
cd django # 프로젝트 파일로 이동
````

2. Poetry(가상환경) 설치

##### 가상환경의 필요성 : 각각의 프로젝트별로 버전 관리가 가능하기 떄문
    

````
# 1) brew 설치
# brew 공식 사이트: https://brew.sh/index_ko
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## (2) poetry 설치
> brew install poetry
> poetry --version

### (3) poetry 설치 확인
> poetry --version
````

3. Poetry 세팅

(1) poetry를 사용하여 가상환경 설정
```
## 폴더 생성
> mkdir django

## 폴더 이동
> cd django

## poetry 초기화
> poetry init

## vsc 열기
> code .
```
(2) 가상환경에 Django 설치
```
# django 설치
> poetry add django

--> 실행 후 .venv 폴더와 poetry.lock 파일이 생성됌.

# pip install selenium
# -> poetry add selenium
```
(3) 가상환경에서 Django 실행

```
1) 현재 폴더에서 프로젝트 생성
> django-admin startproject config .
```

4. Django 서버 실행

```
> python manage.py runserver
```






--- 

# Day 2 : Django Model (URL & VIEW, MODEL)

---

1. URL Dispatcher (urls.py)
- 웹 요청을 처리하고 해당 요청에 맞는 View 함수로 라우팅하는 역할

2. URL & VIEW 설정


(1) config/urls.py 
```
from django.contrib import admin
from django.urls import path, include
from feeds import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("feeds/", include("feeds.urls")),
]
```
(2) feeds/urls.py (파일 생성 필요)
```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_feed)
    path("<int:feed_id>/<str:feed_content>", views.all_feed,
]
```

3. Rendering (View)
* feeds -> templates 폴더 생성
* html 파일 생성
    
--> 데이터 전달 (dict{"key":"value"} 형태로 전달 가능)

(1) feeds/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed

def show_feed(request):
    return HttpResponse("show feed")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"feed id: {feed_id}, {feed_content}")

def all_feed(request):
    feeds = Feed.objects.all()
    return render(request, "feeds.html", {"feeds":feeds, "content":"내용"})
```

(2) feeds/templates/feeds.html
```
<!-- <h1>Show All Feed</h1> -->

<h1>{{content}}</h1>

<ul>
    {% for feed in feeds %} 
        <li>{{ feed.content }}</li> 
    {% endfor %} 
</ul>
```
- - -

1. Model이란?
- 웹 애플리케이션의 데이터 구조를 정의하고 데이터베이스와의 상호작용을 관리

2. Model의 기본 개념 

    (1) 클래스 : **`django.db.models.Model`** 클래스를 상속받아 정의
   
    (2) 필드 정의 : 모델 안에 다양한 필드 타입(CharField, IntegerField 등)을 정의하여 데이터베이스 테이블의 구조 결정

    (3) 데이터베이스 테이블과의 매핑 : 모델 클래스를 기반으로 데이터베이스 테이블 생성. __클래스 이름이 테이블 이름으로 사용__

    (4) ORM 기능 : 모델을 통해 CRUD(Create, Read, Update, Delete) 작업을 SQL 쿼리를 작성하지 않고도 수행 가능

3. Model 고급 기능

* 관계 필드 : ForeignKey, ManyToManyField, OneToOneField 등을 사용하여 모델 간의 관계를 정의
* 메타 클래스 : **`class Meta`** 내부에서 모델의 데이터베이스 테이블 이름, 정렬방식, 인덱싱 등의 추가적인 옵션 정의
* 모델 메소드 : 모델 인스턴스의 행동을 정의하는 메소드 추가
* 매니저 : 모델의 데이터베이스 쿼리 작업을 관리하는 객체, 기본적으로 모든 Django 모델에 objects라는 매니저 자동 추가

4. Model 사용

* Migration : 모델을 정의하거나 변경한 후에 명령어 사용하여 데이터베이스 스키마 생성 또는 업데이트 진행
```
> python manage.py makemigrations # 모델 변경 사항 발생시 변경 사항을 바탕으로 마이그레이션 파일 생성
> python manage.py migrate # 만들어진 마이그레이션 파일을 실제 데이터베이스에 적용
```

5. Model Field

| **필드 타입** | **설명** | **추가 파라미터** |
| --- | --- | --- |
| CharField | 짧은 문자열 저장 | **`max_length=100`** |
| TextField | 긴 문자열 저장 | - |
| IntegerField | 정수 저장 | - |
| BigIntegerField | 매우 큰 정수 저장 | - |
| FloatField | 부동 소수점 숫자 저장 | - |
| DecimalField | 고정 소수점 숫자 저장 | **`max_digits=5, decimal_places=2`** |
| BooleanField | 불리언 값 (**`True`**/**`False`**) 저장 | - |
| NullBooleanField | 불리언 값이나 **`Null`** 저장 | - |
| DateField | 날짜 저장 | **`auto_now=True`**, **`auto_now_add=True`** |
| DateTimeField | 날짜와 시간 저장 | **`auto_now=True`**, **`auto_now_add=True`** |
| TimeField | 시간 저장 | - |
| DurationField | 시간 간격 저장 | - |
| ForeignKey | 다른 모델에 대한 일대다 관계 | **`on_delete=models.CASCADE`** |
| OneToOneField | 다른 모델에 대한 일대일 관계 | **`on_delete=models.CASCADE`** |
| ManyToManyField | 다른 모델에 대한 다대다 관계 | - |
| FileField | 파일 업로드 | **`upload_to='path/'`** |
| ImageField | 이미지 파일 업로드 | **`upload_to='path/'`** |
| SlugField | URL에 사용하기 좋은 짧은 레이블 | - |
| URLField | URL 저장 | - |
| UUIDField | UUID 저장 | - |
| JSONField | JSON 형식 데이터 저장 | - |
| EmailField | 이메일 주소 저장 | - |

- 숫자
    - IntegerField
    - PositiveIntegerField
- 문자
    - CharField
    - TextField
    - URLField
    - EmailField
- 날짜
    - DateField
    - DateTimeField
- 기타
    - ImageField
    - JSONField
- - -
## 실습하기

#### Board Model 생성
1. boards app 생성
```
> python manage.py startapp boards
# boards라는 모델 생성, 모델은 1개지만 모델의 갯수 자체는 늘어나기에 복수 형태로 생성 
```

2. `boards/models.py`에서 모델 정의
```
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
```

3. `config/settings.py`
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "boards.apps.BoardsConfig" # 추가
]
```

4. `boards/admin.py`
```
from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
```

5. makemigrations & migrate
```
> python manage.py makemigrations # 0001_initial.py 파일 생성
> python manage.py migrate
```

6. boards model 테스트

```
> python manage.py shell

from boards.models import Board

# 새로운 Board 객체 생성 및 저장
board = Board(title="테스트 제목", content="테스트 내용")
board.save()

# 저장된 Board 객체 조회
all_boards = Board.objects.all()
print(all_boards)
```
---
#### User Model 생성

1. startapp 명령어 실행
```
> poetry shell # 가상환경 접속
> python manage.py startapp users # users라는 모델 생성
```

2. models.py, admin.py 파일 확인


3. users/model.py
```
from django.db import models

class User(models.Model): # Model을 상속받는다
    name = models.CharField(max_length=20) # 짧은 문장
    description = models.TextField() # 긴 텍스트 문장
    age = models.PositiveIntegerField(null=True) # 양의 정수형 숫자 
    gender = models.CharField(max_length=10)
```

4. config/settings.py에 users app 기입
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig" # startapp할 때 생성 -> users/app.py 체크
]
```

5. users/admin.py

```
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    pass
```

6. makemigrations & migrate
```
> python manage.py makemigrations
> python manage.py migrate
```
---
# Day 3 : Django Admin (Admin 패널 관리, Custom Admin 실습)

---

__Admin Pannel__

1. Admin Pannel 활성화
* `myproject/urls.py`파일에서 `django.contrib.admin`이 포함되어 있는지 확인

```
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

2. Admin Page에 Model 등록

```
# myapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

# myapp/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

3. Admin 계정 생성 
```
> python manage.py createsuperuser 
# -> 실행 후 사용자 이름, 이메일, 비밀번호 입력
```

4. Admin Page 접속 및 사용

```
> python manage.py runserver
```

5. Custom Admin Page
```
# myapp/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # 목록에 표시할 필드
    search_fields = ['title', 'author']  # 검색 필드

admin.site.register(Book, BookAdmin)
```
- - - 
__User Admin Pannel__

1. 패널에 표시될 이름 관리

```
# users/models.py

def __str__(self):
    return self.name

def __str__(self):
    return f"{self.name} / ({self.age}살)" # f-string 도 가능
```
2. 필터, 검색 기능 추가

```
list_filter= ["age", "gender"]
search_fields = ["name"]
```

3. 최종 코드
```
# users/admin.py
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User) # UsersAdmin에 등록할 Model 지정 (Decorator)
class UsersAdmin(admin.ModelAdmin): # ModelAdmin을 상속
    # pass
    list_display = ["name", "description", "age", "gender"]
    list_filter= ["age", "gender"]
    search_fields = ["name"]
```

---
__Board Admin Panel 관리__

1. board model 정의

```
# models.py
from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
```

2. admin.py 최종 코드

```
# admin.py
from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'date', 'likes', 'content') # 관리자 페이지의 목록에 표시할 필드 지정
    list_filter = ('date', 'writer') # 목록 페이지에서 필터 옵션으로 사용될 필드 지정
    search_fields = ('title', 'content') # 검색 기능에서 사용할 필드 지정
        ordering = ('-date',) # 목록 페이지의 기본 정렬 순서 지정
        readonly_fields = ('writer',) # 읽기 전용 필드 지정
        fieldsets = (
            (None, {'fields': ('title', 'content')}),
            ('추가 옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
            ) # 상세 페이지에서 필드 그룹 지정
	    list_per_page = 1 # 목록 페이지에 표시할 항목의 수 지정

	    actions = ('increment_likes',) # 사용자 정의 대량 작업 추가

        def increment_likes(self, request, queryset):
            for board in queryset:
                board.likes += 1
                board.save()

        increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"
```

#### Custom_admin
* Django에서 제공하는 기능을 활용해 진행

0. users app 생성
```
> python manage.py startapp users
```

1. users/models.py 수정
```
from django.contrib.auth.models import AbstactUser

class User(AbstractUser):
    pass
```

2. users/admin.py
```
from django.contrib.auth,admin import UserAdmin

@admin.register(User)
class CustiomUserAdmin(UserAdmin):
    pass
```

3. config/settings.py
```
AUTH_USER_MODEL = "users.User"
```

4. users/migrations 폴더에 0001,0002로 시작하는 파일, db.sqlite3 삭제

5. makemigrations & migrate

```
> python manage.py makemigrations
> python manage.py migrate
```

6. user create
```
> python manage.py createsuperuser
```

#### Custom User - 지정 데이터로 수정

1. users/models.py 업데이트
```
class User(AbstractUser):
    is_business = model.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')
```
2. columns값들이 변경되어 Makemigrations & migrate 

#### Common Model 설정

1. common app 생성
```
> python manage.py startapp common
```

2. common/models.py 수정
```
from django.db import models

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 해당 object 생성 시간 기준
    updated_at = models.DateTimeField(auto_now=True) # 해당 object 업데이트된 시간 기준
    
    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서지정 등과 같은 모델에 대한 다양한 사항을 정의하는데 사용
    class Meta:
        abstract = True # DB 테이블에 추가 X
```

3. users를 제외한 각 모델들의 상속 클래스 변경
```
# boards/models.py

from django.db import models
from common.models import CommonModel


class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
		writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
```

4. Makemigrations & Migrate
```
> python manage.py makemigrations
> python manage.py migrate
```
---

# Day 4 : ORM (Object-Realtional Mapping)

---



















