# -*- coding: utf-8 -*-
'''
Created on 2017-09-25
@author: Panke
'''
import string

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
    
def get_text_from_pdf(filename, threshold = 20):
    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)

    #检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    #创建一个PDF资源管理器对象来存储共享资源
    #caching = False不缓存
    rsrcmgr = PDFResourceManager(caching = False)
    # 创建一个PDF设备对象
    laparams = LAParams()
    # 创建一个PDF页面聚合对象
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    #创建一个PDF解析器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    #处理文档当中的每个页面
    
    # doc.get_pages() 获取page列表
    #for i, page in enumerate(document.get_pages()):
    #PDFPage.create_pages(document) 获取page列表的另一种方式
    start_flag = False
    end_flag = False
    text_list = []
    other_list = []
    
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout=device.get_result()
        for x in layout:
            if(isinstance(x,LTTextBoxHorizontal)):
                text=x.get_text().replace('-\n','').replace('\n',' ')
                if start_flag == False and ('INTRODUCTION' in text or 'Abstract' in text): start_flag = True
                if text.startswith("[1]") or "REFERENCES" in text: 
                    end_flag = True
                    break
                elif '. ' not in text: continue
                if len(text) > threshold and start_flag:
                    if text[0] in string.ascii_lowercase:
                        while len(text_list) != 0:
                            if text_list[-1].startswith("Fig"):
                                other_list.append(text_list.pop())
                            else: 
                                text_list[-1] += text
                                break
                        if len(text_list) == 0 : text_list.append(text) 
                    else:
                        text_list.append(text) 
        if end_flag: break
        
    sum = len(text_list)+len(other_list)

    print len(text_list)
    return text_list,other_list,sum
    
if __name__ == '__main__':
    filename = ""
    get_text_from_pdf(filename)