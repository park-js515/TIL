# Vue 8일차

### Navigation Guard

> 네비게이션 가드  

Vue router를 통해 특정 URL에 접근할 때 따른 url로 redirect를 하거나 해당 url로 접근을 막는 방법  
EX) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함  

<a href="https://v3.router.vuejs.org/guide/advanced/navigation-guards.html">https://v3.router.vuejs.org/guide/advanced/navigation-guards.html</a>  

<hr>  

> 네비게이션 가드의 종류  

전역 가드  
- 애플리케이션 전역에서 동작  

라우드 가드  
- 특정 URL에서만 작동  

컴포넌트 가드  
- 라우터 컴포넌트 안에 정의  

<hr>  

### 전역 가드  

> Global Before Guard  

다른 url 주소로 이동할 때 항상 실행  

route/index.js에 `router.beforeEach()`를 사용하여 설정  

콜백 함수의 값으로 다음과 같이 3개의 인자를 받음  
- to: 이동할 url 정보가 담긴 Route 객체  
- from: 현재 url 정보가 담긴 Route 객체
- next: 지정한 url로 이동하기 위해 호출하는 함수  
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함  
    - 기본적으로 to에 해당하는 url로 이동  

<br>  

url이 변경되면 화면이 전환되기 전 `router.beforeEach()`가 호출됨  
- 화면이 전환되지 않고 대기 상태가 됨  

변경된 url로 라우팅하기 위해서는 `next()`를 호출해줘야 함  
- <mark>next()가 호출되기 전까지 화면이 전환되지 않음</mark>  

<hr>  

> Global Before Guard 실습  

```js
// router/index.js
router.beforeEach((to, from, next) => {
  // CODE HERE
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
})
```

'/home'으로 이동하더라도 라우팅이 되지 않고 아래와 같이 로그만 출력함  

`next`가 호출되지 않으면 화면이 전환되지 않음  

![](2023-05-10-09-18-03.png)

<br>  

`next()`가 호출되어야만 화면이 전환됨  

```js
// router/index.js
router.beforeEach((to, from, next) => {
  // CODE HERE
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
  next()
})
```

![](2023-05-10-09-22-50.png)

<br>  

About으로 이동해보기  
- to에는 이동할 url이 about에 대한 정보가, from에는 현재 url인 home에 대한 정보가 들어있음  

![](2023-05-10-09-27-56.png)  

<hr>  

> Login 여부에 따른 라우팅 처리  

Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가  

```vue
// views/LoginView.vue

<template>
  <div>
    <h1>this is login page</h1>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
}
</script>
```

```js
// router/index.js

import LoginView from '@/views/LoginView.vue'

const routes = [
  ...
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
]
```

<br>  

LoginView에 대한 라우터 링크 추가  

```vue
<template>
  <div id="app">
    <nav>
      ...
      <router-link :to="{ name: 'login'}">Login</router-link> |
    </nav>
    <router-view/>
  </div>
</template>
```

<br>  

HelloView에 로그인을 해야만 접근할 수 있도록 만들어보기  

로그인 여부에 대한 임시 변수 생성  

로그인이 필요한 페이지를 저장  
- 로그인이 필요한 페이지들의 이름(라우터에 등록한 name)을 작성  

앞으로 이동할 페이지(to)가 로그인 필요한 사이트인지 확인  

```js
// router/index.js  
// 약간 재귀적으로 작동하는 것으로 생각하면 된다.

router.beforeEach((to, from, next) => {
  // 로그인 여부  
  const isLoggedIn = true // 로그인 됨

  // 로그인이 필요한 페이지 지정  
  const authPages = ['hello']
  
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)
})
```

<br>  

isAuthRequired 값에 따라 로그인이 필요한 페이지이고 로그인이 되어있지 않으면  
- login 페이지로 이동  

그렇지 않으면  
- 기존 루트로 이동  

next() 인자가 없을 경우 to로 이동  

```js
// router/index.js
// 약간 재귀적으로 작동하는 것으로 생각하면 된다.
router.beforeEach((to, from, next) => {
  ...
  if (isAuthRequired && !isLoggedIn) {
    console.log('Login으로 이동')
    next({ name: 'login' })
  } 
  else {
    console.log('to로 이동!')
    next()
  }
})
```

<font color="red">next()가 한번만 호출되도록 유의</font>  

<br>  

isLoggedIn이 true인 경우 (로그인 상태에서 로그인 필요한 페이지로 접속)  
- <mark>/hello/harry</mark>에 해당하는 컴포넌트가 정상적으로 렌더링  

![](2023-05-10-09-49-45.png)  

<br>  

isLoggedIn이 false인 경우 (비로그인 상태에서 로그인 필요한 페이지로 접속)  
- <mark>/hello/harry</mark>을 렌더링하지 않고 Login 페이지로 이동됨  

![](2023-05-10-09-51-26.png)

<br>  

Home => Login으로 이동했는데 console창에 log가 2개가 찍힌 이유  
- 첫 번째 출력은 /hello/harry 로 접속 시도 후 (전역 가드에 막힘)  
    - 전역 가드에서 /login으로 이동 요청할 때 출력  
- 두 번째 출력은 /login으로 이동 요청할 때 출력

<br>  

`/hello/:userName` 페이지를 제외하고는 전역 가드에서 기존 주소로 이동하기 때문에 정상적으로 작동  

로그인 필요한 페이지에 추가하면 비로그인 시 해당 페이지에 접근 불가  

```js
// router/index.js

router.beforeEach((to, from, next) => {
  ...
// 로그인이 필요한 페이지 지정  
  const authPages = ['hello', 'about', 'home']
  
// 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    console.log('Login으로 이동')
    next({ name: 'login' })
  } 
  else {
    console.log('to로 이동!')
    next()
  }
})
```

<br>  

만약 view들이 여러 개라면 모두 추가해주어야 할까?  
- 반대로 Login하지 않아도 되는 페이지들을 모아 둘수도 있음  

```js
// router/index.js
router.beforeEach((to, from, next) => {
  ...
  // 로그인을 하지 않아도 되는 페이지 지정  
  const allAuthPages = ['login']  

  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = !allAuthPages.includes(to.name)
  
  if (isAuthRequired && !isLoggedIn) {
    console.log('Login으로 이동')
    next({ name: 'login' })
  } 
  else {
    console.log('to로 이동!')
    next()
  }
})
```

<hr>  

### 라우터 가드  

> 라우터 가드  

전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용  

`beforeEnter()`  
- route에 진입했을 때 실행됨  
- 라우터에 등록한 위치에 추가  
- 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고, 다른 경로에서 탐색할 때만 실행됨  
- 콜백 함수는 to, from, next를 인자로 받음  

<hr>  

> Login 여부에 따른 라우팅 처리  

"이미 로그인 되어있는 경우 HomeView로 이동하기"  

라우터 가드 실습을 위해 전역 실습코드는 주석처리  

<br>  

로그인 여부에 대한 임시 변수 생성  

로그인 되어있는 경우  
- home으로 이동  

로그인 되어있지 않은 경우  
- login으로 이동  

```js
// router/index.js  

const isLoggedIn = true  

const routes = [
  ...
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 함')
        next({ name: 'home' })
      }
      else {
        console.log('로그인 필요함')
        next({ name: 'login' }) // 로그인이 안되어 있다면 로그인 페이지로 이동
      }
    }
  },
]
```

<br>  

`isLoggedIn = true`인 경우 (로그인 상태인 경우)  
- `/login`으로 접속을 시도하면 Home으로 이동

![](2023-05-10-10-10-44.png)

Login을 제외한 다른 페이지로 이동하면 라우터 가드를 따로 설정해주지 않았기 때문에 라우터 가드가 동작하지 않음  

이런식을 특정 라우트만 따로 가드를 하고 싶은 경우에는 라우터 가드를 사용  

`isLoggedIn = false`로 변경하면 Login 페이지로 정상 이동 가능  

<hr>  

### 컴포넌트 가드  

> 컴포넌트 가드  

특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용  

`BeforeRouteUpdate()`  
- 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행  

<hr>  

> Params 변화 감지  

about에서 jun에게 인사하는 페이지로 이동  

![](2023-05-10-10-54-43.png)  

<br>  

navbar에 있는 Hello를 눌러 woong?(harry)에게 인사하는 페이지로 이동  
- URL은 변하지만 페이지는 변화하지 않음  

![](2023-05-10-10-57-30.png)  

<br>  

변화하지 않는 이유  
- 컴포넌트가 재사용되었기 때문  
- 기존 컴포넌트를 지우고 새로 만든느 것보다 효율적  
    - 단, lifecycle hook이 호출되지 않았음  
    - 따라서 $route.params에 있는 데이터를 새로 가져오지 않음  

<br>  

`beforeRouteUpdate()`를 사용하여 처리  
- userName을 이동할 params에 있는 userName으로 재할당  

```vue
// views/HelloView.vue

<script>
export default {
    name: 'HelloView',
    data() {
        return {
            userName: this.$route.params.userName
        }
    },
    // CODE HERE
    beforeRouteUpdate(to, from, next) {
        this.userName = to.params.userName
        next()
    }
}
</script>
```

<hr>  

### 404 Not Found  

> 404 Not Found  

사용자가 요청한 리소스가 존재하지 않을 때 응답  

```vue
// views/NotFound404.vue  

<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
  name: 'NotFound404'
}
</script>
```

```js
// routers/index.js

import NotFound404 from '@/views/NotFound404.vue'

const routes = [
  ...
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
]
```

<br>  

<a href="https://localhost:8080/404">https://localhost:8080/404</a> 확인

이렇게 직접 요청하는 방식이 아닌, 요청한 리소스가 존재하지 않을 때 404로 이동하도록 하려면 어떻게 해야 할까?  

![](2023-05-10-11-12-00.png)  

<hr>  

> 요청한 리소스가 존재하지 않는 경우  

모든 경로에 대해서 404 page로 redirect 시키기  
- 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redircet 됨  

"이 때, routes에 최하단부에 작성해야 함"  

```js
// router/index.js  
const routes = [
  ...,
  {
    path: '*', // aesterisk, 순서대로 내려가면서 찾기에 마지막에 나두는 것이 바람직하다.
    redirect: '/404',
  }
]
```

<hr>  

> 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우  

예시) Django에게 `artcies/1/`로 요청을 보냈지만, 1번 게시글이 삭제된 상태  
- 이 때 `path: '*'`를 만나 404 page로 렌더링 되는 것이 아니라 기존에 명시한 `articles/:id/`에 대한 components가 렌더링 됨  

하지만 데이터가 존재하지 않기 때문에 정상적으로 렌더링이 되지 않음  

해결책  
- 데이터가 없을 명시  
- 404 page로 이동해야 함  

<br>  

Dog API 문서(<a href="https://dog.ceo/dog-api/">https://dog.ceo/dog-api/</a>)를 참고하여 동적 인자로 강아지 품종을 전달해 품종에 대한  
랜덤 이미지를 출력하는 페이지를 만들어 보기  

<br>  

1. Axios 설치  
2. DogView 컴포넌트 작성  
3. routes에 등록
`'*'`보다 상단에 등록  

```bash
$ npm i axios
```

```vue
// views/DogView/vue

<template>
  <div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
}
</script>
```

```js
// router/index.js

import DogView from '@/views/DogView.vue'

const routes = [
  ...
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView  
  },
  {
    path: '*', // aesterisk, 순서대로 내려가면서 찾기에 마지막에 나두는 것이 바람직하다.
    redirect: '/404',
  }
]
```

<br>  

Dog api 문서를 참고하여 axios 로직을 작성  

```vue
// views/DogView.vue

<template>
  <div>
    <img :src="imgSrc" v-if='imgSrc' alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        methods: 'GET',
        url: dogImageSearchURL
      })
      .then((response) => {
        // console.log(response)
        const imgSrc = response.data.message

        this.imgSrc = imgSrc
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    this.getDogImage()
  }

}
</script>
```

<br>  

`/dog/hound`에 접속하면 hound 품종에 대한 랜덤 사진이 출력  

axios 요청이 오는 중 동작하고 있음을 표현하기 위한 로딩 메시지 정의

```vue
// views/DogView.vue

<template>
  <div>
    <p v-if='!imgSrc'>{{ message }}</p>
    <img :src="imgSrc" v-if='imgSrc' alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중 ... ..."
    }
  },
  ...
}
</script>
```

<br>  

axios 요청이 실패할 경우 자료가 없음을 표현하기  

```vue
<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중 ... ..."
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        methods: 'GET',
        url: dogImageSearchURL
      })
      .then((response) => {
        // console.log(response)
        const imgSrc = response.data.message

        this.imgSrc = imgSrc
      })
      .catch((error) => {
        console.log(error)
        this.message = `${this.$route.params.breed}는 없는 품종입니다.`
        this.$router.push({ name: 'NotFound404' })

      })
    }
  },
  created() {
    this.getDogImage()
  }

}
</script>

```

<br>

이전처럼 메시지를 바꿀수도 있지만 axios 요청이 실패했을 경우 404 페이지로 이동시킬 수도 있음  

```vue
<template>
  <div>
    <p v-if='!imgSrc'>{{ message }}</p>
    <img :src="imgSrc" v-if='imgSrc' alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중 ... ..."
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        methods: 'GET',
        url: dogImageSearchURL
      })
      .then((response) => {
        // console.log(response)
        const imgSrc = response.data.message

        this.imgSrc = imgSrc
      })
      .catch((error) => {
        console.log(error)
        // this.message = `${this.$route.params.breed}는 없는 품종입니다.`
        this.$router.push({ name: 'NotFound404' }) // 이 부분!
      })
    }
  },
  created() {
    this.getDogImage()
  }

}
</script>
```