import requests
import re
import pickle
import operator
from collections import Counter


class SearchEngine:
    
    def __init__(self,*args):     #생성자 부분 
        self.html_list = [] 
        for i in args:
            self.html_list.append(i)  #html 주소를 모두 list에 저장 
                                                              
    
    def addUrl(self,html):      #html list에 추가 
        self.html_list.append(html)
        print("추가 후:  ",self.html_list)
        
        
    def removeUrl(self,html):  #html list 주소에서 제거
        if html in self.html_list:
            self.html_list.remove(html)
        print("제거후: ",self.html_list)
    
    def listUrls(self):       #모든 html_list 출력
        print("현재 저장된 사이트 목록 : ",self.html_list)
    
    def getMaxFreqencyWords(self):   #Counter 모듈을 이용해서 사전을 합치기 
        b = Counter()                #빈 카운터 변수를 만들고 
        
        if not self.html_list:        #만약 비어있으면 None을 출력 
            print("None")
            return None
            
        else:
            for i in self.html_list:            #아니라면 모든 사전을 합치는 작업을 진행 
                a= Counter(self.getWordsFrequency(i))
                b = b + a 
           
            list_a = list(dict(b).values())   #b에는 모든 리스트에 사전값이 합쳐진 값이 있음 
            value_a = list_a[0]               #거기서 최고 빈도만 value_a 에 넣는다. 


            for key, value in dict(b).items():        #만약에 빈도수가 같을 경우를 대비하여 
      
                if (value == value_a):                  #만약에 다음 value(빈도수)가 같다면 출력하자 ! 
                    print("가장 많은 key: ", key)
                    print("가장 많은 value: ", value)
                    value_a = value
                else:
                    break
        
    
    
        
    def getWordsFrequency(self,html):
        
        stop_word = open("stop_words_english.txt",encoding='UTF8') #영어 불용어
        stop_word_ko = open("stopwords-ko.txt",encoding='UTF8')    #한글 불용어

        stop_word.seek(0)            #위치 초기화 
        stop_word_ko.seek(0)         #위치 초기화 

        source_list = []
        source_list1= [] #마지막에 저장되는 리스트
        req = requests.get(str(html)) 

        
        source = req.text

        print(source)

        source =  re.sub(r'(?s)\<.*?\>[^\w\s]*', '', source).replace('\n', '')    # < > 사이 태그 문자 삭제 
        source =  re.sub(r'(?s)\>.*?\>[^\w\s]*', '', source).replace('\n', '')     # > > 사이 문자 삭제 
        source =  re.sub(r'(?s)\{.*?\}[^\w\s]*', '', source).replace('\n', '')     # {  }사이 문자 제거 
        source =  re.sub('[-=+,#/\?:^$.@*\"※◀ⓒ▶~&%ㆍ!』;}\\‘|\(\)\[\]\<\>`\'…》]', '', source)   #특수문자 제거 
        
        source_list = source.split()            # 공백으로 문자들을 나누고 
       
        for i in source_list:
            if(len(i)>20):               #띄어쓰기가 안된 엄청 긴 단어들은 표현 x 
                source_list.remove(i)                #주석처리 해제 하면 결과 출력 됩니다! 
                
                
        for s in source_list:                   #영어와 숫자가 혼합된 단어 삭제 (예를 들면 zfq412afn 같은 )
            if s.isalpha() :
                source_list1.append(s)  
            else:
                continue
            
            
            
            
        wordCount = {} 

        for word in source_list1:      # Get 명령어를 통해, Dictionary에 Key가 없으면 0리턴
            wordCount[word] = wordCount.get(word, 0) + 1 


        while(True):   #영어 불용어 처리 

            j = stop_word.readline()
            j = j.strip('\n')
            if(j in wordCount):
                del(wordCount[j])  #해당되는 단어 삭제
            if j=='':
                break


        while(True):     #한글 불용어 처리 

            k= stop_word_ko.readline()
            k = k.strip('\n')
            if(k in wordCount):
                del(wordCount[k])
            if k=='':
                break    
    
        for word in source_list:       #여기서 key정렬 
            keys = sorted(wordCount.keys())    

        
        stopword_input=str(input(html + "의 불용어를 입력해주세요 (없을 시 -1 입력): "))                      #사용자 불용어 처리 
        while(stopword_input != str(-1)):                #-1이 입력될때 까지 삭제 
            stopword_input=str(input())
            if(stopword_input in wordCount):
                del(wordCount[stopword_input])

        
        
        pickle_result= sorted(wordCount.items() , key = lambda item: item[1],reverse=True)   #여기서 빈도수를 계산하여 정렬 
        pickle_result= pickle_result[:7]                                                     #7개만 선별해서 출력 여기서 개수 정함
        dct = dict((x, y) for x, y in pickle_result)
        #print(dct)
        
        stop_word.close()
        stop_word_ko.close()
        print("사이트별 대표 단어입니다!", html ,"는")
        print(pickle_result)
        print("검색된 모든 단어의 갯수는 : ",len(source_list), "개 입니다.")   
        return dct   #정렬된 사전 반납

        

    def searchUrlByWord(self,word):
        http=""
        max_num = 0
        a={}
        for i in self.html_list:
            a =  self.getWordsFrequency(i)           #word(keyword)와 관련된 단어를 찾는다. 
            
            if a.get(word) is not None:              #만약 키워드가 있다면 
                
                if  max_num < a.get(word) :          #여기서 사이트중 가장 빈도가 높은것을 가려낸다. 
                        max_num = a.get(word) 
                        http  = i
                    
        print("가장 관련있는 사이트는 : ", http)
        print("해당 ",word,"의 반복횟수는 :",a.get(word))
                
            
            
        

        
w1 = SearchEngine('http://www.cnn.com', 'http://www.times.com', 'https://www.amazon.com')
w1.addUrl('https://github.com')
w1.removeUrl('http://www.cnn.com')
w1.listUrls()
w1.getMaxFreqencyWords()
w1.searchUrlByWord("exitcard")




# class SearchEngineWithOrderedWebWords(SearchEngine): 
#     def __init__(self,*args):
#         self.html_list = [] 
#         for i in args: 
#             self.html_list.append(i)
    
#     def __iter__(self):
#         a = self.generator()
#         return a
    
#     def generator(self):
#         c = self.getWordsFrequency()
#         for i in c: 
#             yield i 
    
#     def getWordsFrequency(self,reverse=False):
#         b = Counter()                #빈 카운터 변수를 만들고 
        
#         if not self.html_list:        #만약 비어있으면 None을 출력 
#             print("None")
#             return None
            
#         else:
#             for i in self.html_list:            #아니라면 모든 사전을 합치는 작업을 진행 
#                 a= Counter(super().getWordsFrequency(i))
#                 b = b + a 
#             if reverse == True:
#                 c = sorted(b.items() , key = lambda item: item[1])
#                 #print(c)
#                 return c 
               
                
                    
#             elif reverse == False: 
#                 c = sorted(b.items() , key = lambda item: item[1],reverse = True)
#                 #print(c)
#                 return c 

