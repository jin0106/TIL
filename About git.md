# git



* commit: 커밋(create a snapshot) 만들기
* push : 현재까지의 역사 (commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

![](https://images.velog.io/images/jin0106/post/6ccfac78-a707-4684-95b8-69ccda448efe/image.png)

### 1. git init - 저장소 초기화
```
$ git init
```

* `.git` 폴더가 생성되고, 여기에 git과 관련된 모든 정보가 저장됨.

### 2. add
commit 하기전에 작업공간에 변경된 사항을 저장하기 위해 반드시 `staging area` 에 올려야한다.
 ```
$ git add name.md # 특정 파일
$ git add python/ # 특정 폴더
$ git add . # 	현재 디렉토리 모든 파일
$ git add -A # 	 작업 디렉토리 내의 모든 변경 내용을 모두 스테이지 영역으로 넘기고 싶을때 사용.
 ```

>git push origin 푸쉬 하기

### 3. Commit
* 해당 시점을 스냅샷으로 만들어서 기록을 한다.
* 커밋시 반드시 log 메시지 작성해야하며, log 메시지에 변경사항을 알 수 있도록 명확히 작성해주는게 좋다.
```
$ git commmit -m 'log'

```

### 4. repository 생성
* 원격 저장소를 local에 등록
```
$ git remote add origin 'github repositoy url'
$ git remote -v # 현재 등록된 정보 확인 가능

```
### 5. Push
* repository로 업로드

```
$ git push origin mast
```

### 6. status
* 현재 git 저장소 상태 확인
* 변경되거나 추가된 파일이 있으면 표시를 해준다
* 변경되었는데 add가 되어있지 않다면 해당 파일명을 붉은색, add는 되어있으나 commit이 되어있지 않으면 녹색으로 표시.

```
$ git status
```


### 7. Pull
- origin master 원격 저장소를 로컬 저장소에 반영하기
```
$ git pull origin master
```

### 8. log

- 현재까지 commit 한 기록을 보여줌
- 각 커밋별로 사용자, 날짜, 시간 그리고 커밋 메시지 보여준다
```
$ git log
```


### 총 정리

- `init`-`add`-`commit`-`push` (repository 등록 했단든 가정하에)


- 집에서 한것이 최신이고 클래스에서 git 작업 한번도 안한경우
		 
  - `'$ git clone 'github repository url'`
  	- 원격 저장소를 기준으로 최신 버전 파일이 다운 받아짐
    -.git 폴더도  자동 생성
  
 - 집에서 한것이 최신이고 집에서 작업
 	- `add -> commit -> push`	
 - 클래스에서 한것이 최신이고 집에서 작업

 	-`pull -> add -> commit -> push`

  

​    