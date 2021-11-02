# 데이터베이스 관계 (M:N)

## DB

* 1:N
  * 정의 : 모델 단수형 (.user)
  * ForeignKey => N
  * 역참조 : 모델이름_set (article_set)
* M : N
  * 정의 및 역참조 : 모델 복수형 (like_users, like_articles)
  * 

<hr>

#### 1. M:N (Many to Many)

##### 모델링

```python
class Doctor(models.Model):
  name = models.Charfield(max_lenght=10)
  
class Patient(models.Model):
  name = models.Charfield(max_length=10)

class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



* 환자와 의사 생성

  ```python
  d1 = Doctor.objects.create(name='a')
  d2 = Doctor.objects.create(name='b')
  
  p1 = Patient.objects.create(name='c')
  p2 = Patient.objects.create(name='d')
  ```

* 예약 생성

  ```python
  Reservation.objects.create(doctor=d1, patient=p1)
  Reservation.objects.create(doctor=d1, patient=p2)
  Reservation.objects.create(doctor=d2, patient=p1)
  ```

* 1번 의사의 예약 목록

  ```python
  d1.reservation_set.all()
  ```

  ```python
  Reservation.objects.filter(doctor_id=1)

* 1번 환자의 예약 목록

  ```python
  p1.reservation_set.all()
  ```

* 1번 의사의 환자 출력

  ```python
  for reservation in d1.reservation_set.all():
    print(reservation.patient.name)
  ```



##### 중계 모델 활용

> 의사 -환자들 / 환자 - 의사들로 직접 접근 위해서 `ManyToManyField`를 사용.
>
> `through` 옵션을 통해 중개 모델을 선언.

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    # M:N 관계. reservation 통해서, Doctor에 접근을 의미
    # DB X, ORM에서 메서드 조작을 편하게 하기 위함
    doctors = models.ManyToManyField(Doctor, through='Reservation')

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



* 의사, 환자 오브젝트 가져오기

  ```python
  p1 = Patient.objects.get(pk=1)
  d1 = Doctor.objects.get(pk=1)
  ```

* 1번 환자의 의사 목록

  > `Patient` 모델이 `Doctor` 모델을 참조하고 있기 때문에

  ```python
  p1.doctors.all()
  ```

* 1번 의사의 환자 목록

  > `Doctor` 입장에서는 `Patient` 를 역참조 하고 있음

  ```python
  d1.patient_set.all()
  ```

  * `related_name` : 역참조 옵션

    * 기본 값 `model name_set` 을 직접 바꾸기 위해 `related_name` 사용

    ```python
    class Patient(models.Model):
        name = models.TextField()
        # 역참조 설정. related_name
        doctors = models.ManyToManyField(Doctor, through='Reservation',
                            related_name='patients')
    ```

    위와 같으면 1번 의사의 환자목록을 다음과 같이 조회가 가능하다.

    ```python
    d1.patients.all()
    ```



##### 중개 모델 사용 하지 않는 경우

* 별도의 클래스 만들 필요없이 `ManyToManyField`로 구현.

  * `add()`와 `remove()` 로 추가 제거 가능

  ```python
  class Doctor(models.Model):
    name = models.CharField(max_length=20)
    
  class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
  ```

* 예약 만들기

  ```python
  d1 = Doctor.objects.create(name='dr.a')
  p1 = Patient.objects.create(name='b')
  d1.patients.add(p1)
  ```

* 예약 조회

  ```python
  d1.patients.all()
  p1.doctors.all()
  ```

* 예약 취소

  ```python
  d1.patients.remove(p1)
  ```

  

#### 좋아요 기능 구현

##### models.py

* related_name 피루

  역참조시 user.article_set이 겹치기 때문에 오류 발생

```django
class Article(models.Model):
  title = ..
  content = ..
   .
   .
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



##### urls.py

```python
path('<int:pk>/like/', views.like, name='like')
```

