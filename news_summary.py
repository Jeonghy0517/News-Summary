
##진행순서##
#1. 뉴스 기사 (base64 파일) 디코딩
#2. 문서 요약/키워드 추출
#3. 요약 리포트 작성
#4. html 파일로 Export

#1. 뉴스 기사 디코딩
#1-1. base64 파일 읽기
import base64

f = open("image", 'rb') #rb(read byte)
image = f.readlines() #파일 전체를 한 라인씩 읽어와 리스트를 만들어주는 메소드
f.close()

print(image[0])

f = open("article", 'rb')
article = f.readlines()
f.close()

print(article)

#1-2. 기사 이미지 디코딩
file_base64 = image[0]

path = "image.jpg"
with open(path, 'wb') as f: #wb(write byte)
    decoded_data = base64.decodebytes(file_base64)
    f.write(decoded_data)

from PIL import Image
img = Image.open(path)
img

#1-3. 기사 디코딩
file_base64 = article[0]
decoded_data = base64.decodebytes(file_base64)
decoded_data

article = decoded_data.decode('utf-8')
print(article)

#2. 문서 요약/키워드 추출
from gensim.summarization.summarizer import summarize
from gensim.summarization.textcleaner import split_sentences

#2-1. 단어수 기반 요약 (word_count)
print(summarize(article, word_count=50))

#2-2. 비율 기반 요약(ratio)
print(summarize(article, ratio=0.1))

#2-3. 요약한 텍스트 저장
article_summarize = summarize(article, ratio=0.1)

#2-4. 키워드 추출
import collections
import textwrap
import re

#2-5. 줄바꿈 정렬
article_align = textwrap.fill(article, width=50)
print(article_align)

#2-6. 단어 추출
words = re.findall(r'\w+', article_align)
#findall : 정규식과 매치되는 모든 문자열을 list로 반환
#\w+ 는 문자+숫자와 매치 공백 기준으로 단어 추출(?)

print(words)

#2-7. 빈도수 산출
counter = collections.Counter(words)
print(counter)

#2-8. 키워드 추출
print(counter.most_common(5))
keywords = counter.most_common(5)[1:]
print(keywords)

#3. 요약 리포트 작성 
from IPython.display import Image
Image(filename=path, width=300)

print(article_summarize)

keys = ['#' + i[0] for i in keywords]
keys = ' '.join(keys) #매개변수로 들어온 리스트를 문자열로 합쳐서 반환해주는 함수
print(keys)

#3-1. html 파일로 저장
htmlfile = open("summary.html", "w")
htmlfile.write("<html>\n")
htmlfile.write("<h1>" + '카운트다운 들어간 아르테미스 계획 "달의 여신"은 미소지을까' + "</h2>\n")
htmlfile.write("<img src='image.jpg' />\n")
htmlfile.write("<h2>" + article_summarize + "</h2>\n")
htmlfile.write("<h2 style='background-color:powderblue;''>"+ keys + "</h2>\n")
htmlfile.write("</html>\n")
htmlfile.close()