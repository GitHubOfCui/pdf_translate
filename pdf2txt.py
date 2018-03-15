# -*- coding: utf-8 -*-
'''
Created on 2017-09-25
@author: Panke
'''
import os
import random
import time
import codecs

from get_text import get_text_from_pdf
from google_translate_spider import get_translate


location = 'C:\\Users\\Administrator\\Desktop\\PaperWeek\\'

def test(pdfname):
    filename = pdfname+'.pdf'
    print ("Start extracting....")
    text_list,other_list,sum = get_text_from_pdf(location+filename)
    out_html = location+pdfname+'.html'
    if os.path.exists(out_html):
        os.remove(out_html)
    with codecs.open(out_html,'wb',encoding='utf-8') as f:
    
        #print (text_list[30])
        index = 1
        trans_list = []
        print ("Start translating....")
        for text in text_list:
            try:
                f.write("<p>"+text+"</p>\n")
                trans = get_translate(text)
                print text
                print trans
                trans_list.append(trans)
                f.write("<p>"+trans+"<p>\n")
                f.write("<hr>\n")
                print ("%d/%d:" % (index,sum))
                index += 1
                
                delay_time = random.randint(1,3)
                if index % 5 == 0: delay_time *= 2
                print ("time wait:%d" % delay_time)
                time.sleep(delay_time)
            except Exception:
                print ("This is not a normal json")
    f.close()

if __name__ == '__main__':
    pdfname = "2014 Endmember Extraction Guided by Anomalies and Homogeneous Regions for Hyperspectral Images"
    test(pdfname)
