```bash
# 기본
git add a.txt
git status
git commit -m 'first commit'
git log

git remote add https://github.com/park-js515/GitTest.git
git push origin +master

# staging area -> working area로 되돌리기
git init
git add .
git commit -m '1'

## 1. 파일 수정 -> modified 상태 -> 처음 commit 상태로 되돌리기
git restore a.txt

## 2. staging area에 있는 modified 파일을 working area로 내릴 때 

### 1 restore --staged
### working으로 내린 파일이 modified(tracted 상태로 git이 추적함)
### 변화가 없다면 untract가 된다...?
git restore --staged a.txt

### 2 reset (사용하지 않는 것을 권장: 협업 중에서 좋지 않음)
git 

### 3 rm --cached
### working으로 내린 파일이 untract file로 인식
git rm --cachced a.txt
```

```bash
# commit 시 메시지를 잘못 적었을 때
git commit --amend -m '2'

# a.txt를 commit 했는데, b.txt도 같이 커밋해야 했을 때
git add .
git commit --amend -m '3'
```

```bash
# revert / reset : 과거 커밋 이력으로 되돌릴 때
# 둘 다 과거 커밋으로 되돌릴 때 사용되나,
# reset - 과거 커밋으로 시점으로 돌아감과 동시에 과거 커밋 이력들이 다 삭제됨(협업 시 조심히 사용해야 한다.)
# revert - 과거에 커밋을 취소함과 동시에 취소한 이력이 새로 커밋됨. (협업 시 reset 보다 추천함.)

git add a.txt
git commit -m '1'
git add b.txt
git commit -m '2'
git add c.txt
git commit -m '3'

# 한줄로 로그 보기
git log --oneline
# 453d21b (HEAD -> master) 3
# 6d9ad1d 2
# 13ee2bf 1

# reset  

## hard - 이전 커밋 파일들 삭제
git reset --hard 13ee2bf

#####
git add b.txt
git commit -m '2'
git add c.txt
git commit -m '3'

## soft - 파일이 삭제되지 않고 staging area로 파일을 되돌림
git reset --soft 13eebf

#####
git add b.txt
git commit -m '2'
git add c.txt
git commit -m '3'

## mixed - 파일을 working area로 되돌림  
git reset --mixed 13ee2bf
```

```bash
# reset 사용 시 커밋한 히스토리를 다시 보고 싶다.
# reset 데이터가 삭제 되는 것이 아니라 보이지 않는 것

git add b.txt
git commit -m '2'
git add c.txt
git commit -m '3'

# reflog: 과거 이력 확인
git reflog
# 되돌리기
git reset 13ee2bf
```

```bash
# 기본 에디터 VSCode로 
git config --global core.editor "code --wait"

# revert: 해당 커밋 취소 후 새로운 커밋
git revert 13ee2bf
```

```bash
# branch 
# 처음부터 시작

git init 
git add work1.txt
git commit -m '1'
git add work2.txt
git commit -m '2'

# 현재 브랜치 확인
git branch

# 브랜치 생성
git branch studentA
git branch studentB

git branch
git log
# 새로운 파일 work3.txt 생성

# 브랜치로 이동  
git switch studentA

# 내용 변경 및 커밋
git add .
git commit -m 'studentA - 1'
git log --oneline
# 브랜치 별로 확인하기
git log --oneline --branches

# master에는 있고, studentA에 없는 커밋
git log master..studentA

# studentA에 있고, master에 없는 커밋  
git log studentA..master
```

```bash
# 합병하기
git swich master
git merge studentA


## 그래프로 확인하기
git log ---oneline --branches --graph
```

```bash
git switch studentA
# 동기화 시키기
git rebase master

git switch studentB
# 동기화 시키기
git rebase master

# => 모든 파일이 같아짐  
```

```bash
git switch studentA
# work1 내용 변경  

git switch studentB
# work1 내용 변경, 수정 부위가 다르게  

git switch master
git merge studentA
git merge studentB
git status

# work1 첫 번째 줄만 수정  
git switch studentA
# work1 첫 번째 줄만 수정  

git switch master
git merge studentA # 충돌 발생
# 수기로 고쳐야 함

git add .
git commit -m '충돌해결'

git log --oneline --branches --graph
```
