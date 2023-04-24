# JavaSript 4일차

### Event

> 개요  

<mark>Event</mark>란 HTML 요소에서 발생하는 모든 상황을 의미
- 예를 들어 사용자가 웹 페이지 버튼을 클릭한다면 클릭에 대해 이벤트가 발생하고 우리는 


```html
<!-- 01_pg14_button.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  <script>
  // 초기값
    let countNumber = 0
  // ID가 btn인 요소를 선택
    const btn = document.querySelector('#btn')

  // btn이 클릭 되었을 때마다 함수가 실행됨
    btn.addEventListener("click", function(event) {
      console.log("버튼을 클릭했어요!")
      countNumber += 1

      const counter = document.querySelector('#counter')
      counter.innerText = countNumber
    })
  </script>
</body>

</html>
```

```html
<!-- 02_pg16_input.html -->

```
