# JavaSript 4일차

### Event

> 개요  

<mark>Event</mark>란 HTML 요소에서 발생하는 모든 상황을 의미
- 예를 들어 사용자가 웹 페이지 버튼을 클릭한다면 클릭에 대해 이벤트가 발생하고 우리는 이벤트를 통해 클릭이라는 사건에 대한 결과를 받거나, 조작을 할 수 있음  

클릭 말고도 웹에서는 각양각색의 Event가 존재  
- 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등  

<hr>  

### Event Intro

> Event object  

네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체  

이벤트가 발생했을 때 생성되는 객체  

Event 발생  
- 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고  
- 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음  

&nbsp;

DOM 요소는 Event를 받고 ("수신")

받은 Event를 "처리"할 수 있음  
- Event 처리는 주로 <code>addEventListener()</code> 메서드를 통해 Event 처리기(Event handler)를 다양한 html 요소에 "부착"해서 처리함  

<hr>  

> Event handler

특별한 함수가 아닌 일반적인 JavaScript Function을 정의하여 사용  

웹 페이지에서 발생하는 Event에 대해 반응하여 동작하는 함수를 지칭  

Event handler 함수는 이벤트가 발생했을 때 호출되며, Event 객체를 매개 변수로 전달 받음  

<hr>  

Event handler - <mark>addEventLister()</mark>

<h4>"<font color='red'>대상</font>에게 <font color='green'>특정 Event</font>가 발생히면, <font color="blue">할 일</font>을 등록하자"</h4>  

<h4><font color='red'>EventTarget</font>.addEventListener(<font color='green'>type</font>, <font color="blue">handler function</font>)</h4>  

&nbsp;

<code>EventTarget.addEventListener(type, handler function[, options])</code>  
- 지정한 Event가 대상에게 전달될 때마다 호출할 함수를 설정  
- Event를 지원하는 모든 객체(Element, Document, window 등)를 대상 (EventTarget)으로 지정  

&nbsp;

- type
    - 반응할 Event 유형을 나타내는 대소문자를 구분하는 문자열  
    - 대표 이벤트  
        - input, click, submit ...
        - 다양한 이벤트 확인(<a href="https://developer.mozilla.org/en-US/docs/Web/Events">https://developer.mozilla.org/en-US/docs/Web/Events</a>)

&nbsp;

- hander function  
    - 지정된 타입의 Event를 수신할 객체
    - JavaScript function(콜백 함수)여야 함  
    - 콜백 함수는 발생할 Event의 데이터를 가진 Event 객체를 유일한 매개변수로 받음  

<hr>

### Event 실습

> button 실습

버튼을 클릭하면 특정 변수 값으로 변경  

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
