# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:37:41 2021

@author: gppcom
"""


import re
import urllib
import numpy as np


url= "https://g1.globo.com/" #o site de acesso as noticas
html = urllib.urlopen(url).read() #leitura da pagina web acima

urls = re.findall('(?<=href=["\'])https?://.+?(?=["\'])', html) #todas urls da pagina
urls= np.unique(urls).tolist()


listtitles=[] #lista que guarda os titulos das noticas
listsubtitles=[]# lista que guarda os subtitulos

#padráo de busca do titulo
patterntitle = r"<h1 class=\"content-head__title\" itemprop=\"headline\">(.*?)</h1>"
#padráo de busca do subtitulo
patternsubtitle = r"<h2 class=\"content-head__subtitle\" itemprop=\"alternativeHeadline\">(.*?)</h2>"



especificdate = False; #pego as noticias de uma data especifica ou simplesmente as ultimas "howmanynotices" noticias?

if especificdate:
    date = "/2021/03/29/" 
    for line in urls:
        if re.findall(date, line):
            htmlnoticia= urllib.urlopen(line).read()
            if ( (re.findall(patterntitle, htmlnoticia))):
                listtitles.append( (re.findall(patterntitle, htmlnoticia))[0])
                if ( (re.findall(patternsubtitle, htmlnoticia))):
                    listsubtitles.append( (re.findall(patternsubtitle, htmlnoticia))[0])
                else:
                    listsubtitles.append("")
else:
    pattern = r"/\d{4}/\d{2}/\d{2}/"
    for line in urls:
        if re.findall(pattern, line):
            htmlnoticia= urllib.urlopen(line).read()
            if ( (re.findall(patterntitle, htmlnoticia))):
                listtitles.append( (re.findall(patterntitle, htmlnoticia))[0])
                if ( (re.findall(patternsubtitle, htmlnoticia))):
                    listsubtitles.append( (re.findall(patternsubtitle, htmlnoticia))[0])
                else:
                    listsubtitles.append("")
                        
                    

  
sizelistnotices = len(listtitles)        
print("%d Notícias Foram Encontradas" % sizelistnotices )



howmanynotices = input('Quantas Notícias Deseja ver:?') 
while (howmanynotices > sizelistnotices):
    howmanynotices = input('Por favor, escolha um número menor ou igual a quantidade de notícias encontradas:')
    #quantas noticas devem ser impressas

for i in range(howmanynotices):

    print("NOTICIA %d:" % i)
    print("TITULO: ") 
    print(listtitles[sizelistnotices -1 - i])
    print("SUBTITULO: ")
    print(listsubtitles[sizelistnotices -1 - i])
    
