# Script_Programming_class
Koreatech university Python class
<br>
<img src="https://user-images.githubusercontent.com/91319157/208688180-ba2c8567-a82b-4447-ac61-7a5ec218d03b.gif"  width="50px">
<br>

## 👋🏻 소개 
Koreatech Univ Script Programming
수업에서 내주셨던 과제와 공부 과정 & 해결 답안을 작성하여 올린 파일 입니다. 

거기에서 대표 문제 (과제5 [Incremental project] )만 소개

<br>

### 💻 환경 
- `Python`
- `Jupyter notebook`
- **IDE**: visual studio code 

<br><br>

## 수업 기간 ⏰
#### 

- 2021.09.02~2021.12.10

<br>

# 문제: 웹 파싱해 보기 (BeautifulSoup 사용 금지) 💯

<br>

### 개요

> 웹 파싱(Parshing)이란 어떤 페이지(문서, HTML 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보로 가공하는 것을
> 
> 말합니다. 주로 웹 페이지 소스나, 문서 등에서 행해지며 주로 HTML tag, Xpath 등을 분석해 1차 적인 파싱(Parshing) 작업
> 
> 거치며 Python에서는 BeautifulSoup 모듈을 이용합니다. 조금 더 자세한 정보 수집이 필요할 때는 re 모듈을 사용해서 
> 
> 정규 표현식을 사용한 데이터 파싱을 진행합니다. 
> 
> 웹이나 다른 유저의 정보를 추출해 원하는 정보만 볼 수 있도록 제공하는 등 현재에 많이 사용되는 기술 중 하나 입니다.

<br>
<img src="https://user-images.githubusercontent.com/91319157/208672941-97b9bb5a-75c8-49ec-a838-e7e7633527b8.png" width="300px">
<br>

## 구현 방법
- ### SearchEngine class : 사이트에 주소를 리스트 형태로 저장하고 관리하는 Class

***

```
  class SearchEngine:  
    def __init__(self,*args):     #생성자 부분 
        self.html_list = [] 
        for i in args:
            self.html_list.append(i)  #html 주소를 모두 list에 저장 

```

이렇게 리스트로 구현했기 때문에 삭제와 추가가 용이합니다. 

```
w1 = SearchEngine('https://cse.koreatech.ac.kr', 'http://www.cnn.com', 'https://www.koreatech.ac.kr/kor/Main.do')
w1.addUrl('https://github.com')
w1.removeUrl('http://www.cnn.com')
```
내장 함수: add, delete , getWordFrequency , getMaxFreqencyWords , searchUrlByWord
<br>
<br>
<br>
<br>

- ### getWordsFrequency

***

이제 핵심 기능인 웹사이트 파싱을 구현할 함수입니다. 
파이썬에서 제공해주는 re 모듈을 사용합니다. re 모듈은 정규화식을 이용해 문자열을 가공할 수 있도록 도와줍니다. 
<br>
1. 태그값 제거
<> 사이의 있는 값을 없애기 위해 다음과 같은 정규식을 사용하여 태그 값을 제거했습니다.

```
source =  re.sub(r'(?s)\<.*?\>[^\w\s]*', '', source).replace('\n', '')    # < > 사이 태그 문자 삭제 
```
그 외에도 특수문자, {}사이 문자를 제거하여 더욱 정확한 값을 추출할 수 있도록 제작했습니다. 

<br>
<br>

2. 긴 글 제거

```
     for i in source_list:
            if(len(i)>20):               #띄어쓰기가 안된 엄청 긴 단어들은 표현 x 
                source_list.remove(i)                #주석처리 해제 하면 결과 출력 됩니다! 
```

<br>
<br>
<br>

3. 영어 숫자 섞인 단어 제거 (ex : zw1321d)
```
  for s in source_list:                   #영어와 숫자가 혼합된 단어 삭제 (예를 들면 zfq412afn 같은 )
            if s.isalpha() :
                source_list1.append(s)  
            else:
                continue

```
<br>
<br>
<br>

4. 불용어 제거

추출을 진행하니 알 수 없는 단어만 추출되었습니다. (ex. fdq) 
더욱 정확한 단어만 추출하기 위해서 불용어를 제거하는 부분을 추가했습니다. 

불용어 리스트를 Text파일로 저장해 해당 값을 불러와 나의 source (즉, 위에서 가공된 단어들) 

에 존재한다면 삭제! 과정을 진행했습니다.


```
while(True):   #영어 불용어 처리 

            j = stop_word.readline()
            j = j.strip('\n')
            if(j in wordCount):
                del(wordCount[j])  #해당되는 단어 삭제
            if j=='':
                break
```
<br>
<br>
<br>


5. 사용자 불용어 처리 

이렇게 제거하더라도 웹페이지별로 쓰래기값이 분류되어 저장되는 현상이 발생했습니다. 

<img src="https://user-images.githubusercontent.com/91319157/208681422-70f10dac-05dc-478e-9f30-a9dadaebdf34.png" width="80%">

그래서 사용자 수동적으로 입력 받아 불용어를 처리할 수 있는 기능을 추가했습니다. 

```
 stopword_input=str(input(html + "의 불용어를 입력해주세요 (없을 시 -1 입력): "))                      #사용자 불용어 처리 
        while(stopword_input != str(-1)):                #-1이 입력될때 까지 삭제 
            stopword_input=str(input())
            if(stopword_input in wordCount):
                del(wordCount[stopword_input])
```
<br>
<br>
<br>
<br><br>

- ### searchUrlByWord

***

사용자가 입력한 값이 어떤 사이트에서 나타나는 지 확인하는 함수입니다. 
해당 단어가 여러 사이트에서 발견되었을 경우 빈도수가 높은 사이트를 결과로 반환합니다.

```
http=""
        max_num = 0
        a={}
        for i in self.html_list:
            a =  self.getWordsFrequency(i)           #word(keyword)와 관련된 단어를 찾는다. 
            if a.get(word) is not None:              #만약 키워드가 있다면 
                if  max_num < a.get(word) :          #여기서 사이트중 가장 빈도가 높은것을 가려낸다. 
                        max_num = a.get(word) 
                        http  = i
```

<br><br><br><br><br><br><br><br><br><br><br><br>



## 결과 

입력 사이트:
- http://www.times.com
- https://www.amazon.com
- https://github.com

```
w1 = SearchEngine('http://www.github.com', 'http://www.times.com', 'https://www.amazon.com')
w1.getMaxFreqencyWords()
w1.searchUrlByWord("exitcard")
```

<br><br>

> http://www.times.com 결과: 

[('exitcard', 195), ('relatedlink', 124), ('New', 73), ('York', 66), ('data', 63), ('The', 55), ('relatedlinkimg', 54)]

검색된 모든 단어의 갯수는 :  10946 개 입니다.

<br>

> https://www.amazon.com 결과:

[('span', 2), ('endifdiv', 1), ('Enter', 1), ('characters', 1), ('Sorry', 1), ('robot', 1), ('For', 1)]

검색된 모든 단어의 갯수는 :  36 개 입니다.

<br>

> https://github.com 결과:

[('path', 44), ('span', 31), ('dinlineblock', 19), ('div', 11), ('source', 11), ('strokecurrentColor', 10), ('GitHub', 9)]

검색된 모든 단어의 갯수는 :  1183 개 입니다.

<br>
해당단어  exitcard 
가장 관련있는 사이트는 :  http://www.times.com


<br><br><br><br><br><br><br><br><br>

## 피드백 🥊

get을 통해서 html 데이터 값을 불러 온 결과는 다음과 같습니다.
<br>
<img src="https://user-images.githubusercontent.com/91319157/208692524-ecbf7422-c811-4e39-b697-842cff10d3d7.png" width="50%">
<br>

여기서 Beautifulsoup를 사용하지 않고 이 많은 데이터를 가공해야하는데, 저는 정규표현식 Re 모듈을 이용하여 가공했습니다.

그 결과 한번이라도 잘못 < 기호를 만난다면 그 이후는 짝이 맞지 않아서 계속적으로 잘못된 단어를 추출하는 결과를 가져옵니다.

예를 들면 
```
<span class="a" <a href="">hi</a> hi  </span>
```
이와 같은 코드 < 안 < 이 존재하는 예외를 처리하지 않아 올바른 단어 추출이 되지 않았던 것 같습니다.

그래서 결과를 보더라도 Var , Span , path 같은 html 키워드만 추출된 것을 볼 수 있었습니다. 

그래서 겉에 <를 만나면 다시 < 를 만나도 무조건 >때 까지 삭제하도록 만드는 방안을 생각했습니다.

많이 부족한 부분이 많고 오류로 동작이 잘 되지 않는 부분도 있습니다....🥲



<br>
<br>
<br>

## 후기 🤔

컴퓨터공학부 2학년 스크립트 프로그래밍 수업에서 배운 내용을 토대로 프로젝트를 제작했습니다. 
<br>

정말 처음부터 하나하나씩 기능을 추가해가며 과제를 완성했습니다. 
<br>
그래서 삐그덕 거리고 부족했던 부분이 많았습니다. 
<br>

하지만, 스스로 오류가 발생할 때마다 구글링해가며 찾아보고 
<br>
공부해 직접 사용해보니 더욱 빨리 내 것, 내 지식으로 
<br>

만들 수 있었습니다. 자연스럽게 Python 에서 제공하는 자료구조, 모듈, 타입 계층 구조를 깨우칠 수 있었습니다. 
<br>

많이 부족하긴 했지만, 직접 알고리즘을 생각해보고 오류 없이 결과물을 만들 수 있었다는 것에 보람을 느끼고 
<br>

앞으로는 문제를 해결할 때나 코딩을 할때 더 깊게 생각해보고 다양한 입력값에 대한 에러를 어떻게 제어할 지 생각해보는 개발자가 되겠습니다. 
<br>

작고 소박한 나의 삐걱거리는 과제였습니다. 


<br><br><br><br>
<img src ="https://user-images.githubusercontent.com/91319157/208697708-98934f91-4cbc-4eb0-9578-13e84cb8ac84.jpg" width="20%">



 


<br>
<br>

## 감사합니다 

<img src="https://user-images.githubusercontent.com/91319157/208434073-c834c893-2aed-4ded-a079-dff65540063f.gif" width="30%"> 
