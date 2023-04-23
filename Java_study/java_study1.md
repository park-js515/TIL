# Java1

### 형 변환(Type Casting)

변수의 타입을 다른 타입으로 변환하는 것  

primitive <-> primitive, reference <-> reference  
- boolean은 다른 기본 타입과 호환되지 않음  
- 기본 타입과 참조형의 형 변환을 위해서 Wrapper 클래스 사용  

```java
// ex
double d = 100.5;
int reuslt = (int) d;
```

```java
// 묵시적 형 변환(promotion)

byte b = 10;
int i = (int) b;
int i2 = b;
```

```java
// 명시적 형 변환  

int i = 300;
byte b = (byte) i;
```

