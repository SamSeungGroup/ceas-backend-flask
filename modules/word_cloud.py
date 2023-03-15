from wordcloud import WordCloud
from nltk.corpus import stopwords
from collections import Counter
from konlpy.tag import Okt

def get_word_cloud(string):
    okt = Okt()
    line = okt.pos(string)

    temp =[]
    for word, tag in line:
        if tag in ['Noun', 'Adjective', 'Verb']:
            temp.append(word)
    words = [n for n in temp if len(n) > 1]
    word_dic = Counter(words)
    word_cloud = WordCloud(font_path='font/malgun.ttf', 
                            width=400, height=400, scale=2.0, max_font_size=250,
                            stopwords=stopwords,
                            background_color="white")\
                            .generate_from_frequencies(word_dic)
    return word_cloud