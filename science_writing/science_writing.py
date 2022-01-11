import sys
import os
import time
import matplotlib.pyplot as plt
import spacy
import pandas as pd 
import numpy as np
from matplotlib.font_manager import FontProperties
from collections import defaultdict
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import  PDFParser,PDFDocument


def parse(pdf_path,wordcount):
    nlp = spacy.load("en_core_web_sm")
    fp = open(pdf_path,'rb')
    #用文件对象创建一个PDF文档分析器
    parser = PDFParser(fp)
    #创建一个PDF文档
    doc = PDFDocument()
    #连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)
    
    #提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    #检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr,laparams=laparams)
        #创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr,device)
 
        #循环遍历列表，每次处理一个page内容
        # doc.get_pages() 获取page列表
        pdfwords = ""
        for page in doc.get_pages():
            interpreter.process_page(page)
            #接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if(isinstance(x,LTTextBoxHorizontal)):
                    pagetext = x.get_text()
                    words = pagetext.split()
                    for word in words:
                        if word.isalpha() and word.__len__()>2:
                            pdfwords += word + ' '
        test_doc = nlp(pdfwords)
        for token in test_doc:
            #print(token, token.lemma_)
            wordcount[token.pos_][token.lemma_.lower()] = wordcount[token.pos_][token.lemma_.lower()]+1

if __name__ == '__main__':
    pdf_dir = '/home/cui/science writting/astro_paper'
    #pdf_dir = input("pdf_dir path:")
    # time1 = time.time()
    wordcount = defaultdict(lambda: defaultdict(lambda: 0))
    for root, dirs, files in os.walk(pdf_dir):
        for file in files:
            pdf_path = pdf_dir+"/"+file
            parse(pdf_path,wordcount)
    #需要六类单词词性        
    type=['NOUN','VERB','ADJ','ADV','CCONJ','PROPN']
    #根据需要改变'astro'
    for ty in type:                                             #wordcount为总的词语出现次数，包含了各种种类，
        globals()['astro'+ty]=  []                              #定义全局变量名NOUN/VERB......
        globals()['astro'+ty+'ct']=[]                           #定义全局变量名NOUNct/VERBct......
        words = wordcount[ty]                                   
        wordlist = list(words.items())                          
        wordlist.sort(key=lambda x:x[1],reverse=False)          
        i = wordlist.__len__()
        if i > 10 : i = 10
        while i > 0:
            globals()['astro'+ty].append(wordlist[-i][0])        #将单词名字加入进去
            globals()['astro'+ty+'ct'].append(wordlist[-i][1])   #将单词数量加入进去
            i = i-1 


#computer_data
type=['NOUN','VERB','ADJ','ADV','CCONJ','PROPN','DET','SCONJ','PRON','PART','AUX','SYM','INTJ','PUNCT']
df=pd.DataFrame([])
for i in type:
    #将字典倒入Pandas可用的DataFrame
    df1=pd.DataFrame.from_dict(wordcount[i],orient='index',columns=['number'])
    df1=df1.reset_index().rename(columns={'index':'vocabulary'})
    #加入一列为词性
    POS=[]
    for j in range(0,len(df1)):
        POS.append(i)
    POS=pd.Series(POS)
    df1['part of speech']=POS
    df1=df1.set_index(['part of speech','vocabulary'])
    #用单词出现次数排序
    df1=df1.sort_values('number',ascending=False)
    #将不同词性的单词拼接
    df=df.append(df1)
df.to_csv('computer_data.csv') #根据需要改变文件名

#computer figure
fig,axes=plt.subplots(3,2,figsize=(16,12))
fig.suptitle('$Computer$ $Vocabulary$',fontsize=20)
axes[0,0].barh(compNOUN,compNOUNct) 
axes[0,0].set_title('$Noun$',fontsize=16)
axes[0,1].barh(compVERB,compVERBct)
axes[0,1].set_title('$Verb$',fontsize=16)
axes[1,0].barh(compADJ,compADJct)
axes[1,0].set_title('$Adjective$',fontsize=16)
axes[1,1].barh(compADV,compADVct)
axes[1,1].set_title('$Adverb$',fontsize=16)
axes[2,0].barh(compCCONJ,compCCONJct)
axes[2,0].set_title('$Conjunction$',fontsize=16)
axes[2,0].set_xlim(0,250)
axes[2,1].barh(compPROPN,compPROPNct)
axes[2,1].set_title('$Pronoun$',fontsize=16)
#fig.tight_layout()
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
fig.savefig('comp_figure.jpg')

#astro figure
fig,axes=plt.subplots(3,2,figsize=(16,12))
fig.suptitle('$Astronomy$ $Vocabulary$',fontsize=20)
axes[0,0].barh(astroNOUN,astroNOUNct) 
axes[0,0].set_title('$Noun$',fontsize=16)
axes[0,1].barh(astroVERB,astroVERBct)
axes[0,1].set_title('$Verb$',fontsize=16)
axes[1,0].barh(astroADJ,astroADJct)
axes[1,0].set_title('$Adjective$',fontsize=16)
axes[1,1].barh(astroADV,astroADVct)
axes[1,1].set_title('$Adverb$',fontsize=16)
axes[2,0].barh(astroCCONJ,astroCCONJct)
axes[2,0].set_title('$Conjunction$',fontsize=16)
axes[2,0].set_xlim(0,250)
axes[2,1].barh(astroPROPN,astroPROPNct)
axes[2,1].set_title('$Pronoun$',fontsize=16)
#fig.tight_layout()
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
fig.savefig('astro_figure.jpg')


#名词分析
fig,axes=plt.subplots(1,2,figsize=(16,6))
axes[0].bar(df_astro.loc['NOUN'][0:10].sort_values('number')['vocabulary'],df_astro.loc['NOUN'][0:10].sort_values('number')['number'],width=0.5,alpha=0.9) 
axes[0].set_title('$Noun$ $of$ $Astronomy$  ',fontsize=16)
axes[0].tick_params(axis='x',labelsize=12,rotation=45)
axes[1].bar(df_comp.loc['NOUN']['vocabulary'][0:10],df_comp.loc['NOUN']['number'][0:10],color='r',width=0.5,alpha=0.8)
axes[1].set_title('$Noun$ $of$ $Computer$',fontsize=16)
axes[1].tick_params(axis='x',labelsize=12,rotation=315)
fig.savefig('Noun.svg')


#动词分析
fig,axes=plt.subplots(1,2,figsize=(16,6))
axes[0].bar(df_astro.loc['VERB'][0:10].sort_values('number')['vocabulary'],df_astro.loc['VERB'][0:10].sort_values('number')['number'],width=0.5,alpha=0.9) 
axes[0].set_title('$Verb$ $of$ $Astronomy$  ',fontsize=16)
axes[0].tick_params(axis='x',labelsize=12,rotation=45)
axes[1].bar(df_comp.loc['VERB']['vocabulary'][0:10],df_comp.loc['VERB']['number'][0:10],color='r',width=0.5,alpha=0.8)
axes[1].set_title('$Verb$ $of$ $Computer$',fontsize=16)
axes[1].tick_params(axis='x',labelsize=12,rotation=315)
fig.savefig('verb.svg')