#coding=utf-8
'''
Created on 2017-09-25
@author: Panke
'''
import requests    
from handleJS import Py4Js      
      
def translate(tk,content):     
    if len(content) > 4891:      
        print("翻译的长度超过限制！！！")      
        return ""
    headers = {"origin":"https://translate.google.cn",
               "referer":"https://translate.google.cn/",
               "user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
               }
    param = {'tk': tk, 'q': content}  
  
    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en 
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss 
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param,headers=headers)  

    #返回的结果为Json，解析为一个嵌套列表
    res = ""
    #print result.json()
    for text in result.json()[0][:-1]:  
        res += text[0].replace('\n','').replace(' ','')
    return res
       
      
def get_translate(content):      
    js = Py4Js()      
    tk = js.getTk(content)      
    result = translate(tk,content)
    return result
          
if __name__ == "__main__":
    print 'I am google translate'
    #content = "2017 CCS Exploiting a Thermal Side Channel for Power Attacks in Multi-Tenant Data Centers "
