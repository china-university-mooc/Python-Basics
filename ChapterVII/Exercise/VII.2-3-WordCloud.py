import wordcloud as wc
import jieba
from imageio import imread

mask = imread('bear.png')
f = open('新时代中国特色社会主义.txt')
txt = f.read()
f.close()
w = wc.WordCloud(background_color='white', width=800, height=600, font_path='msyh.ttc', mask=mask)
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('government-wc.png')