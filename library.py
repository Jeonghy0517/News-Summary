# -*- coding: utf-8 -*-
#base64
#바이너리 파일을 문자열로 변경
import base64
string = "Life is too short"

#ascii 인코딩 : base64는 byte단위의 바이너리 파일만 읽을 수 있음 => ascii 코드로 변환 필요
bstring = string.encode('ascii')
print(bstring)

encoded = base64.b64encode(bstring)
print(encoded)

decoded = base64.b64decode(encoded)
print(decoded)

#ascii 디코딩
decode_string = decoded.decode('ascii')
print(decode_string)

#이미지 인코딩, 디코딩
path = "image.jpg"

from PIL import Image
img = Image.open(path)

#바이너리 파일 읽기
with open(path, 'rb') as img:
    image = img.read()
print(image)

#바이트 정보 확인
from bitstring import BitArray
input_str = '0xff'
c = BitArray(hex=input_str)
c.bin

#base64 인코딩
with open(path, 'rb') as img:
    image = img.read()

encoded = base64.b64encode(image)
print(image)

#base64 디코딩
decoded = base64.b64decode(encoded)
print(encoded)

#이미지 파일로 저장
file = "decoded.png"
with open(file, 'wb') as file:
    file.write(decoded)

#---------------------------------------------------------------------------------------------------------------------
#textwrap
import textwrap

text = 'SQL과 파이썬은 전 세계에서 가장 인기 있는 프로그래밍 언어이자 미래에도 수요가 높을 것으로 예상된다. 파이썬과 SQL은 활용 범위가 겹치기만, 보통 SQL은 직접 데이터베이스를 다룰 때 이용하며 파이썬은 보다 범용적으로 프로그래밍에 활용한다. SQL은 데이터에 대한 신속한 분석이 필요하거나 기록을 불러오고 결론을 내릴 때 가장 많이 이용되는 언어이다. SQL도 좋은 언어이지만 R과 파이썬은 복잡한 통계 분석이나 머신러닝, 자동화 기능에 활용할 때, 그 장점이 빛을 발한다. 하지만 최근, 데이터 분야 채용 공고 중 45.4%가 SQL 기술을 요구하여 취업 시장에서 SQL의 수요가 가장 높은 것으로 나타났다. 데이터 사이언스, 데이터 분석, 데이터 엔지니어링, 머신러닝 분야에 취업하고 싶다면, 파이썬과 SQL 능력이 유용할 것이다. 이에, 인도 IT·빅데이터 전문 잡지 애널리틱스 인사이트가 아래와 같이 파이썬과 SQL을 비교했다. SQL은 데이터를 요청하고 추출하기 위하여 설계된 언어이다. 따라서 SQL을 이용하면, 데이터를 불러올 수 있다. 파이썬을 이용한다면, 구조화된 데이터를 수정할 수 있다. SQL은 파이썬보다 코딩이 어렵다. 채용 공고만 보면 SQL은 가장 수요가 높은 프로그래밍 기술로 보인다. 하지만 SQL이 수요가 높은 것은 단순히 기업들이 SQL을 다룰 줄 아는 개발자를 원해서가 아니다. 그들은 보통 다른 프로그래밍 언어에 SQL까지 다룰 수 있는 개발자를 원한다. 파이썬은 애널리틱스 인사이트 자체 조사에서 가장 인기 있는 프로그래밍 언어 1위를 차지했다. SQL은 10위를 기록하였다. 개발자들은 SQL로 데이터베이스를 관리 및 유지하며, 가벼운 분석을 수행하기도 하고 방대한 데이터베이스로부터 기록을 추출하기도 한다. 보통 설문조사에서 자바스크립트가 프로그래밍 언어 인기도 1위를 차지하지만, 이번 조사에서 파이썬이 1위를 차지했다. 개발자는 파이썬으로 회귀 분석을 수행하여 데이터를 분석하고 수정한다. 반면, SQL의 최대 장점은 여러 테이블의 데이터를 통합하여 하나의 데이터베이스를 구성할 수 있다는 점이다. 파이썬이나 R과 같은 범용 언어의 기본을 아는 것은 매우 중요하다. 하지만 SQL을 무시한다면, 데이터 사이언스 분야에 취업할 때 쉽지 않을 것이다. 파이썬을 다룰 수 있지만, SQL 능력이 없다면, 데이터 사이언티스트 취업 기회의 60%를 놓칠 수 있다. SQL은 여전히 데이터를 다루기 위한 인기 있는 언어로 SQL을 배우는 것은 데이터 분야 취업을 위해 필수이다. 계속해서 개발되는 새로운 언어와 프레임워크에 주목하기 쉽다. 그러나 SQL을 한 번 학습해 놓으면 데이터 산업에서 커리어를 쌓는 동안 똑똑히 그 값을 할 것이다.'
print(text)

print(textwrap.shorten(text, width=200))
print(textwrap.shorten(text, width=100, placeholder='...[이하줄임]'))

wrapped_text = textwrap.wrap(text, width=40) #40자 단위로 끊어서 리스트로 만들어줌
print(wrapped_text)

print('\n'.join(wrapped_text)) #리스트를 줄바꿈하여 문자열로 만듬

filled_text = textwrap.fill(text, width=40) #40자 단위로 끊어서 문자열로 만들어줌
print(filled_text)

#re
#정규 표현식 : 복잡한 문자열을 처리할 떄 사용하는 기법, 파이썬 뿐만 아니라 C, 자바 심지어 문서 작성 프로그램 등 문자열을 처리해야 하는 다양한 곳에서 활용, 특정 문자열 추출, 변환 등에 사용
import re

#단어 추출
words = re.findall(r'\w+', text)
print(words)

#전화번호 추출
contact = '''김미키 21 010-3344-5566 Mike@google.com 
             김소은 20 010-5032-1111 Soeun@naver.com
             유한슬 34 010-2789-1476 Lyu@school.ac.com
             박민철 40 010 4040 1313 Zoe@school.ac.com
             이민아 23 010-7777-2222 Kate@google.com'''

regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'
#\d는 숫자 범위
#[문자] : 문자 중에 하나
#ex) [Pp] : Python or python
#? : 바로 앞의 글자 혹은 그룹이 1개 혹은 0개

phone = re.findall(regex, contact) #contact에서 regex(정규표현식)으로 추출
print(phone)

phone = '\n'.join(phone)
print(phone)

#변환마스킹
pat = re.compile(r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}') #정규식 객체를 리턴
print(pat.sub("***-****-****", contact)) #정규식과 매치되면 변경시킴

#------------------------------------------------------------------------------------------------------------------
#단어 개수 구하기

import collections
import textwrap
import re

text = textwrap.fill(text, width=50) #50자 단위로 잘라서 문자열 변환
print(text)

#단어 추출
words = re.findall(r'\w+', text)
print(words)

#빈도수 산출
counter = collections.Counter(words)
print(counter)

#상위 빈도수 산출
print(counter.most_common(5))

#덧셈
a = collections.Counter(['a','b','c','b','d','a'])
b = collections.Counter(['e', 'f', 'f', 'b', 'a', 'd'])

print(a)
print(b)
print(a+b)
print(a-b)
print(a&b) #교집합
print(a|b) #합집합

#---------------------------------------------------------------------------------------------------------------------
#문서 요약하기
#gensim : 자연어 처리, 토픽 모델링에 활발히 사용되는 파이썬 머신러닝 라이브러리
#summarization 내장 모듈로 긴 문장을 요약할 수 있음 (gensim 3.7.3 사용)
import gensim

#모델 불러오기(Word2Vec 알고리즘을 통해 자연어의 벡터화)
model = gensim.models.Word2Vec.load('../ko/ko.bin')
print(model)

#유사한 단어 검색
print(model.wv.most_similar("뉴스"))
#유사도 검색
print(model.wv.similarity('자동차','강아지'))
#유사도 검색
print(model.wv.similarity('자동차','버스'))

#문서 요약하기
from gensim.summarization.summarizer import summarize
import pandas as pd
import numpy as np

df = pd.read_csv('Book_test.csv')
df = df.iloc[0:100] #전체 데이터 프레임에서 0부터 100까지 행에 있는 값을 추출
#iloc : integer location, 행이나 칼럼의 순서를 나타내는 정수
df.reset_index(inplace=True) #기존 인덱스 제거

print(df.head())
print(df.loc[0,'passage']) #index 0의 passage
print(df.loc[0,'summary']) #index 0의 summary

#첫번째 데이터 요약
print(summarize(df.loc[0,'passage']))
print(summarize(df.loc[0,'passage'], ratio=0.4))

#전체 데이터 적용
df['extract'] = df.passage.apply(lambda  x : summarize(x, ratio=0.4))
print(df.head)

#시각화
for i in range(0,1):
    random_num = np.random.randint(0, 100,size=1)
    print("="*120)
    print(f'{random_num[0]}' + '번째 문장 \n')
    print('원문 : \n\n' + df['passage'][random_num[0]] + '\n\n')
    print('AI 요약 : \n\n' + df['summary'][random_num[0]] + '\n\n')
    print('Gensim 요약 : \n\n' + df['extract'][random_num[0]] + '\n\n')

#----------------------------------------------------------------------------------------------------------------------
#텍스트 파일 저장
#open, close

#텍스트 파일 생성
f = open("새파일.txt","w")
f.close

#텍스트 파일 쓰기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다. \n' % i
    f.write(data)
f.close()

#한 줄 읽기
# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

#여러 줄 읽기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#내용 추가하기
# w 모드 사용 시 (write)
f = open("새파일.txt",'w')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# a 모드 사용 시 (append)
f = open("새파일.txt",'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with 문 사용
# close() 사용 불필요
with open("새파일.txt", "w") as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
