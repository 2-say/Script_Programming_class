# Script_Programming_class
Koreatech university Python class

## 👋🏻 소개 
Koreatech Univ Script Programming
수업에서 내주셨던 과제와 공부 과정 & 해결 답안을 작성하여 올린 파일 입니다. 
거기에서 대표 문제 (과제5 [Incremental project] )만 소개

### 💻 환경 
- `Python`
- `Jupyter notebook`
- **IDE**: visual studio code 

## 수업 기간 ⏰
#### 

- 2021.09.02~2021.12.10

<br>
<br>

# 문제: 웹 파싱해 보기 (BeautifulSoup 사용 금지) 



### 개요

웹 파싱(Parshing)이란 어떤 페이지(문서, HTML 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보로 가공하는 것을

말합니다. 주로 웹 페이지 소스나, 문서 등에서 행해지며 주로 HTML tag, Xpath 등을 분석해 1차 적인 파싱(Parshing) 작업

을 거치며 Python에서는 BeautifulSoup 모듈을 이용합니다. 조금 더 자세한 정보 수집이 필요할 때는 re 모듈을 사용해서 

정규 표현식을 사용한 데이터 파싱을 진행합니다. 

웹이나 다른 유저의 정보를 추출해 원하는 정보만 볼 수 있도록 제공하는 등 현재에 많이 사용되는 기술 중 하나 입니다.


<img src="https://user-images.githubusercontent.com/91319157/208672941-97b9bb5a-75c8-49ec-a838-e7e7633527b8.png" width="300px">
<br>

### 구현 방법
- SearchEngine class : 사이트에 주소를 리스트 형태로 저장하고 관리하는 Class

```
  class SearchEngine:  
    def __init__(self,*args):     #생성자 부분 
        self.html_list = [] 
        for i in args:
            self.html_list.append(i)  #html 주소를 모두 list에 저장 

```

이렇게 리스트로 구현했기 때문에 

















## 후기 🤔

컴퓨터공학부 2학년 웹프로그래밍 수업에서 배운 것을 토대로 제작했습니다. 



제가 이 과목을 들으면서 가장 좋았던 점은 정말 아무것도 없는 백지에다가 내가 원하는 무엇이든지 나만의 세상을 만들 수 있다는 점이었습니다.


상상력을 마음 껏 표출할 수 있었고 제한이 없었기 때문입니다. 저의 색을 마음 껏 칠할 수 있어
더욱 흥미롭게 진행 할 수 있었던 것 같습니다. 

html & css 에서 제가 반영한 수정사항이 바로바로 눈에 확인 할 수 있었던 것이 
공부를 하는 데 많이 도움이 되었습니다. 


제 프로젝트에 부족한 부분이 많습니다. 
하지만 앞으로 더욱 발전해가며 이 프로젝트를 보며 참 귀여웠다는 생각이 들 수 있는 날이 
올 때까지 더욱 노력하겠습니다.


### 부족한 부분
- 코드 정리
- 중복 코드 관리
- 주석 부족
- 회원 닉네임이 매우 길 경우 메뉴와 겹치는 현상


<br>
<br>

## 감사합니다 

<img src="https://user-images.githubusercontent.com/91319157/208434073-c834c893-2aed-4ded-a079-dff65540063f.gif" width="30%"> 
