# 자주 쓰는 git 명령어 모음

## git init 

`git init`은 프로젝트 내에 숨겨진 `.git 디렉토리`를 생성하는데 해당 명령어를 입력하면 Git은 이제 현재 저장소에 대해 모든 변경 사항을 `추적/관리`할 수 있게 된다.


## git add 

`git add` 명령어는 `Staging area`에 파일을 추가하고 커밋을 남길 수 있게 해준다.

### 특정 파일 하나만 추가하기

```
git add test.py
``` 

### 여러 개의 파일 한 번에 추가하기

``` 
git add test.py test1.py, test2.py
```

### 모든 파일 한 번에 추가하기

```
git add .
```


## git commit

`git commit` 명령어는 특정 시간의 코드 스냅샷의 형태로 해당 repository의 커밋 기록에 남게 된다.
`git add` 명령어를 통해 `Staging area`에 추가된 파일들만 커밋 대상이 된다.

```
git commit -m "Commit message"
```

큰 따옴표 안에 남기고 싶은 커밋 메시지를 작성하면 된다.


## git remote add "git주소"

해당 명령어는 원격 저장소를 추가하는 명령어인데 이를 통해 현재 로컬 저장소가 원격 저장소와 연결되어 관리가 가능해진다.

```
git remote add https://github.com/Daphne-dev/wecode.git
```

## git push 

해당 명령어는 Staging area에 올라온 로컬 저장소의 내용을 원격 저장소로 보내는 역할을 한다.

```
git push -u origin main
```


