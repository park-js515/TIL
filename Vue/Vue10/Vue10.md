# Vue 10일차

### DRF Auth System  

### Authentication & Authorization  

> Authentication - 인증, 입증  

자신이라고 주장하는 사용자가 누구인지 확인하는 행위  

모든 보안 프로세스의 첫 번째 단계(가장 기본 요소)   

즉, 내가 누구인지를 확인하는 과정  

401 Unauthorized  
- 비록 HTTP 표준에서는 "미승인(unauthorized)"을 명확히하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미  

<hr>  

> Authorization - 권한 부여, 허가  

사용자에게 특정 리소스 또는 기능에 대한 액세스 권한을 부여하는 과정(절차)  

보안 환경에서 권한 부여는 항상 인증이 먼저 필요함  
- 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함  

서류의 등급, 웹 페이지에서 글을 조회 & 삭제 & 수정 할 수 있는 방법, 제한 구역  
- 인증 되었어도 모든 권한을 부여받는 것은 아님  

403 Forbidden  
- 401과 다른 점은 서버는 클라이언트가 누구인지 알 수 있음  

<hr>  

> Authentication and authorization work together  

회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성  
- 인증 이후에 권한이 따라오는 경우가 많음  

단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님  
- Django에서 로그인을 했더라도 다른 사람의 글까지 수정/삭제가 가능하지 않음  

세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식이 존재  

<hr>  

### authentication determind  

> 인증 여부를 확인하는 방법  

DRF 공식문서에서 제안하는 인증 절차 방법  

<a href="https://www.django-rest-framework.org/api-guide/authentication/">https://www.django-rest-framework.org/api-guide/authentication/</a>

![](2023-05-15-10-19-50.png)  

BasicAuthentication, SessionAuthentication은 뭘까?  

<br>  

settings.py에 작성하여야할 설정  
- "기본적인 인증 절차를 어떠한 방식으로 둘 것이냐"를 설정하는 것  
- 예시의 2가지 방법 외에도 각 framework마다 다양한 인증 방식이 있음  

우리가 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 `TokenAuthentication`  

모든 상황에 대한 인증 방식을 정의하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요  

<br>  

view 함수마다 (각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용  

![](2023-05-15-10-22-30.png) 

[참고] permisson_classes  
- 권한 관련 설정  
- 권한 역시 특정 view 함수마다 다른 접근 권한을 요구할 수 있음  

<hr>  

> 다양한 인증 방식  

[참고] - 왜 필요할까?  
- 인터넷은 비연결성을 가진다.(상태를 저장X: HTML을 1번 다운로드하면 연결을 끊는다.)
- 요청을 보낼 때마다 인증하는 것은 비효율적이므로 이를 세션(출입 명부: 서버), 토큰(통행증: 클라이언트), 쿠키 등을 이용해서 처리한다.

[참고] - 세션 방식
- 문제점: 사용자가 너무 많으면? => 서버에 부하가 크다.

[참고] - 토큰 방식  
- 토큰에는 정보가 담겨 있음
    - 내가 누구인지
    - 암호화
- 문제점: 클라이언트 토큰 탈취(해킹), 무거움

<hr>

BasicAuthencation(쿠키)  
- 가장 기본적인 수준의 인증 방식  
- 테스트에 적합  

SessionAuthentication(session)  
- Django에서 사용하였던 session 기반의 인증 시스템  
- DRF와 Django의 session 인증 방식은 보안적인 측면을 구성하는 방법에 차이가 있음  

RemoteUserAuthentication  
- Django의 Remote user 방식을 사용할 때 활용하는 인증 방식  

<br>
TokenAuthentication  
- 매우 간단하게 구현할 수 있음  
- 기본적인 보안 기능 제공  
- 다양한 외부 패키지가 있음  

(중요) settings.py에서 <mark>DEFAULT_AUTHENTICATION_CLASS</mark>를 정의  
- TokenAuthentication 인증 방식을 사용할 것임을 명시  

<hr>  

> TokenAuthentication 사용 방법  

INSTALLED_APPS에 `rest_framework.authtoken` 등록  

```py
# settings.py

INSTALLED_APPS = [
    ...,
    "rest_framework.authtoken"
]
```

각 User마다 고유 Token 생성  

```py
from rest_framework.authtoken.models import Token  

token = Token.objects.create(user=...)
print(token.key)
```

<br>  

생성한 Token을 각 User에게 발급  
- User는 발급 받은 Token을 요청과 함께 전송  
- Token을 통해 User 인증 및 권한 확인  

Token 발급 방법
```py
def some_view_func(request):
    token = Token.objects.create(user=...)
    return Response({ 'token': token.key })
```

<br>  

User는 발급 받은 Token을 headers에 담아 요청과 함께 전송  
- 단 반드시 `Token` 문자열과 함께 삽입  
    - 삽입해야할 문자열은 각 인증 방식마다 다름 (ex. Beared, Auth, JWT 등) 
    - <font color="red">주의)</font> Token 문자열과 발급받은 실제 token 사이를 <mark>' '(공백)</mark>으로 구분  


Authorization HTTP Headers 작성 방법

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

<hr>  

> 토큰 생성 및 관리 문제점  

기본 제공 방식에서 고려하여야 할 사항들  

1. Token 생성 시점  
2. 생성한 Token 관리 방법  
3. User와 관련된 각종 기능 관리 방법  
회원가입  
로그인  
회원 정보 수정  
비밀번호 변경 등...

<hr>  

### dj-rest-auth  

> Dj-Rest-Auth   

회원가입, 인증(소셜미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공  

<font color="red">주의)</font> django-rest-auth는 더 이상 업데이트를 지원하지 않음. 

![](2023-05-15-10-46-31.png)

dj-rest-auth 사용

<a href="https://github.com/iMerica/dj-rest-auth">https://github.com/iMerica/dj-rest-auth</a>

<hr>  

> dj-rest-auth 사용 방법  

1. 패키지 설치  
```bash
$ pip install dj-rest-auth
```

2. App 등록  
```py
# settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
]

```

3. url 등록

```py

urlpatterns = [
    ...,
    path('accounts/', include('dj_rest_auth.urls')),
]
```

<hr>  

> 시작하기 전에  

시작하기 전에, auth.User를 `accounts.User`로 변경 필요  

auth.User로 설정된 DB 제거  

`my_api/settings.py` 주석 해제 

```py
# my_api/settings.py

INSTALLED_APPS = [
    # Django Apps
    'accounts',
    'articles',
    ...
    ]

AUTH_USER_MODEL = 'accounts.User'
```

db.sqlite3 삭제  

migrations의 000N.~~.py 삭제  

<hr>  

> dj-rest-auth 사용하기  

`dj-rest-auth` 설치  

```bash
$ pip install dj-rest-auth
```

`my_api/settings.py` 주석해제  

```py
# my_api/settings/py

INSTALLED_APPS = [
    ...

    # Auth
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```

<br>  

`makemigrations & migrate`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

`my_api/urls.py` 주석 해제  

```py
# my_api/urls.py

urlpatterns = [
    ...,
    path('accounts/', include('dj_rest_auth.urls')),
]
```

<br>  

결과 확인  
- `/accounts/`로 이동  
- 회원 가입 기능이 없음  

![](2023-05-15-11-40-09.png)  

<br>  

Github 재확인  

상세 옵션은 공식 문서를 참고하도록 안내  

<a href="https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional">https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional</a>  


<hr>  

> Registration  

Registration 기능을 사용하기 위해 추가 기능 등록 및 설치 필요  
- dj-rest-auth는 소셜 회원가입을 지원한다.  
- dj-rest-auth의 회원강비 기능을 사용하기 위해서는 `django-allauth` 필요  

django-allauth 설치  

```bash
# 반드시 ''도 함께 입력  
$ pip install 'dj-rest-auth[with_social]'
```

<br>  

`my _api/settings.py` 주석 해제  
- App 등록 및 SITE_ID 설정  

```py
# my_api/settings.py

INSTALLED_APPS = [
    ...
    # registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

# 회원가입 시 토큰 발급
REST_AUTH = {
    'SESSION_LOGIN': False,
}

SITE_ID = 1
```

[참고] SITE_ID는 무엇인가요?  
- Django는 하나의 컨텐츠를 기반으로 여러 도메인에 컨테츠를 게시 가능하도록 설계됨  
- 다수의 도메인이 하나의 데이터베스에 등록  
- 현재 프로젝트가 첫 번째 사이트임을 나타냄  

<br>  

`my_api/urls.py` 주석 해제  

```py
# my_api/urls.py

urlpatterns = [
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```

migrate  

```bash
# allauth 추가에 대한 migrate
$ python manage.py migrate
```

<br>  

`/accounts/signup/` 페이지 확인  

GET method는 접근 불가  

회원가입 POST 요청 양식 제공  
- email은 생략 가능  

![](2023-05-15-11-47-00.png)  

<hr>  

> Sign up & Login 

회원 가입 요청 후 결과 확인  
- 요청에 대한 응답으로 Token 발급  

![](2023-05-15-11-49-53.png)  

로그인 시에도 동일한 토큰 발급  
- 정상적인 로그인 가능  

![](2023-05-15-11-50-22.png)  

발급 받은 토큰은 테스트를 위해 기록  

<hr>  

> Password change  

`/accounts/password/change/` 기능 확인  
- 로그인되어 있거나, 인증이 필요함  
- DRF 자체 제공 HTML form에서는 토큰을 입력할 수 있는 공간이 없음  
- Postman에서 진행  

[참고] Raw data에서 직접 headers 추가  

```
{
  "headers" : {"Authorization": "Token token"},
  "new_password1": "new_password",
  "new_password2": "new_password"
}
```

<br>  

Postman 양식에 맞춰 POST 요청  

body/form-data에 값 입력  

![](2023-05-15-11-53-09.png)

<br>  

headers에 Token 입력  

`Authorization: Token { your token }` 형식에 맞춰 입력  

![](2023-05-15-12-04-56.png)  

<br>  

실패 이유는?  
- 인증 방법이 입증되지 않음  

`my_api/settings.py` 주석 해제  

```py
# my_api/settings.py

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

<br>  

최종 결과 확인  
- 정상적으로 비밀번호 변경 완료  

![](2023-05-15-12-09-14.png)  

<hr>  

### Permission setting  

> Permission setting  

권한 설정 방법 확인  
- DRF 공식 문서 > API Guide > Permissions 확인  

<a href="https://www.django-rest-framework.org/api-guide/permissions/">https://www.django-rest-framework.org/api-guide/permissions/</a>  

<br> 

권한 세부 설정  
1. 모든 요청에 대해 인증을 요구하는 설정  
2. 모든 요청에 대해 인증이 없어도 허용하는 설정  

설정 위치 == 인증 방법을 설정한 곳과 동일  
- 우선 모든 요청에 대해 허용 설정  

<br>  

`my_api/settings.py` 주석 해제  
- 모두 허용만 주석 해제

```py
REST_FRAMEWORK = {
    ...,
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
}
```

<hr>  

> Article Read  

`articles/views.py` 주석 해제  

게시글 조회 및 생성 요청 시 인증된 경우만 허용하도록 권한 부여  
- decorator를 활용  

```py
# aritcles/view.py

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) # 게시글 조회, 생성은 권한이 필요하게 만듦
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

<br>  

`/articles/` 조회 요청 확인  

게시글 조회 시 로그인 필요  

![](2023-05-15-12-15-33.png)  

<hr>  

> Article Create  

`/articles/` 생성 요청으로 확인  
- Postman으로 진행  

![](2023-05-15-12-16-13.png)  

<br> 

결과 확인  
- 게시글 생성 성공  

![](2023-05-15-12-16-41.png)  

<hr>  

> Article Detail Read  

`/article/1/` 상세 조회 요청 확인  
- headers에 token을 담지 않아도 조회 가능  
- 인증 필요 권한 설정을 따로 하지 않았기 때문  

<hr>  

> 정리  

1. 인증 방법 설정  
- DEFAULT_ATHENTICATION_CLASSES  

2. 권한 설정하기  
- DEFAULT_PERMISSION_CLASSES

3. 인증 방법, 권한 세부 설정도 가능  
- @authentication_classes
- @permission_classes

4. 인증 방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택  

<hr>  

### DRF Auth with Vue  

> Vue Server 요청 정상 작동 여부 확인  

정상  작동하던 게시글 전체 조회 요청이 작동하지 않음  
- 401 status code 확인  
- 인증되지 않은 사용자이므로 조회 요청이 불가능해진 것  

![](2023-05-15-13-25-19.png)  

<hr>  

### signUp Request  

`views/SignUpView.vue` 코드 확인  
- Server에서 정의한 field명 확인  
    1. username
    2. password1
    3. password2

```vue
// views/SignUpview.vue

<template>
  <div>
    <h1>Sign Up Page</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>
```

<br>  

router/index.js 주석 해제  

```js
// router/index.js
...
import SignUpView from '@/views/SignUpView'
...

Vue.use(VueRouter)

const routes = [
  ...,
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
]
```

<br>  

`src/App.vue` 주석 해제  
- 파이프 라인 등을 활용하여 링크간 공간 확보  

```vue
// src/App.vue  

<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      <!-- <router-link :to="{ name: 'LogInView' }">LogInPage</router-link> -->
    </nav>
    <router-view/>
  </div>
</template>
```

`views/SignUpView.vue` 결과 확인  

![](2023-05-15-13-45-08.png)  

<hr>  

> SignUp Request  

회원가입을 응답 받을 정보 Token을 store에서 관리할 수 있도록 action를 활용하여 요청 후, state에 저장할 로직 작성  
- 회원가입이나 로그인 후 얻을 수 있는 Token은 server를 구성 방식에 따라 매 요청마다 요구할 수 있으므로, 다양한 컴포넌트에서 쉽게 접근할 수 있도록 중앙 상태 저장소인 vuex에서 관리  

<br>  

`views/SignUpView.vue` 코드 확인  
- 사용자 입력 값을 하나의 객체 payload에 담아 전달  

```vue
// views/SignUpView.vue

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: "",
      password1: "",
      password2: ""
    }    
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch("signUp", payload)
    }
  }
}
</script>
```

이후에 계속해서