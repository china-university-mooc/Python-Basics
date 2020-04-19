import wordcloud as wc
import jieba

txt = 'life is short, you need python'
w = wc.WordCloud(background_color='white', width=800, height=600)
w.generate(txt)
w.to_file('lift-wc.png')

txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种操作体系"
w = wc.WordCloud(background_color='white', width=800, height=600, font_path='msyh.ttc')
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('lang-wc.png')