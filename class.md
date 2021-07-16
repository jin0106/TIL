#### 1. 인스턴스 변수의 접근 제한 기능	

```python
class Person:
  self.__name = name
```

- `__` 프라이빗 필드 생성
- getter/setter 메서드의 제공 여부에 대한 고민 필요

> getter :  멤버를 읽어오는 메서드
>
> setter : 멤버를 변경하는 메서드

```python
class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    print("{} 객체가 생성되었습니다.".format(self.name))
  
  def __del__(self):
    print("{}객체가 제거되었습니다.".format(self.name))
  
  def to_str(self):
    return "{}\t{}".format(self.__name, self.__age)
  
  def get_name(self):
    return self.__name       #__name 필드에 대해서는 getting메서드만 제공
  
  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    if age<0:
      raise TypeError("나이는 0이상의 값만 허용합니다.")
    self.__age = age
```



### 2. decorator 기능	

> - getter/setter를 대신해 사영 가능
>
> - 변수 이름과 같은 메서드를 만들어 사용 가능

```python
class Person:
  -
  	@property의 이름.setter
    def name(self):
```

```python
class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    print("{} 객체가 생성되었습니다.".format(self.name))
  
  def __del__(self):
    print("{}객체가 제거되었습니다.".format(self.name))
  
  def to_str(self):
    return "{}\t{}".format(self.__name, self.__age)
  
  @property
  def name(self):             #변수처럼 사용 가능
    return self.__name				#__name필드값을 반환하는 getter메서드 역할
  
  @property
  def age(self):						# 변수처럼 사용 가능
    return self.__age				# __age필드값을 반환하는 getter메서드 역할 
  
  @age.setter
  def age(self,age):			#변수처럼 사용 가능
		if age<0:							#__name 필드값응ㄹ 반환하는 setter메서드의 역할
      raise TypeError("나이는 0이상의 값만 허용합니다")
    self.__age = age
```

### 3. 클래스 변수

> - 클래스 내에서 `클래스명.변수` 형식으로 선언된 변수

Ex) 클래스 변수의 count 활용법

```python
class Person:
  count =0
  
  def __init__(self, name, age): #객체가 생성될 때마다 호출되는 __init__메서드
     self.__name = name
     self.__age = age
   	 Person.count += 1
     print("{} 객체가 생성되었습니다.".format(self.__name))
  
  def __del__(self):
    print("{} 객체가 제거 되었습니다.".format(self.__name))
    
  def to_str(self):
    return "{}\t{}".format(self.__name, self.__age)
  
  @property
  def name(self):             
    return self.__name				
  
  @property
  def age(self):						
    return self.__age				
  
  @age.setter
  def age(self,age):			
		if age<0:						
      raise TypeError("나이는 0이상의 값만 허용합니다")
    self.__age = age
    
people = [
  Person("홍길동", 20),
  Person("이순신", 45),
  Person("강감찬", 35)
]

print("현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(Person.count))

	@classmethod
  def get_info(cls):  #cls가 클래스 참조 정보가 인자로 넘어올 매개변수
		return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)
print(Person.get_info()) 
  #cls.count는 Person.count` +=1과 동일하다고 보면 됨
```



주말에 내용 추가 예정
