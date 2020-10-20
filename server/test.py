#! /usr/bin/python3
from selectolax.parser import HTMLParser
import requests as r
import sys
import urllib.parse
import re
import pandas as pd
import time 

def getDefinition(terme):
    termeHttp = terme
    termeHttp = urllib.parse.quote_plus(termeHttp, encoding='iso-8859-1')
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + termeHttp + '&rel=1'
    html = r.get(url)
    #print (terme + "   " +termeHttp)
    tree = HTMLParser(html.text)
    
    try:
        definition = tree.css_first('def').text()
        code = tree.css_first('CODE').text()
    except AttributeError as error:
        print("Le mot" + terme + " n'existe pas" , error)
        return
    
    print("Definition pour " + terme + ": \n" + definition)
    
    #code = re.sub(r'(?m)^ *//.*\n?', '', code)
    #code = code.strip("\n")
    #code = code.split(";")
    #writer = csv.writer(open(terme+".csv","w"))
    #writer.writerow(code)
    
    match = re.findall(r"("+ terme + "\>[^0-9].*)", code)
    match.reverse()
    #print(code)
    #print(match)
    
    
    for m in match:
        m = m[:-1] # il faut corriger dans expressions reguliers (m') !!
        getDefinition(m)
    
def getThemeDomaine(terme):
    termeHttp = terme
    termeHttp = urllib.parse.quote_plus(termeHttp, encoding='iso-8859-1')
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + termeHttp + '&rel=3'
    html = r.get(url)
    #print (terme + "   " +termeHttp)
    tree = HTMLParser(html.text)
    
    try:
        code = tree.css_first('CODE').text()
    except AttributeError as error:
        print("Le mot" + terme + " n'existe pas" , error)
        return    
    print("Theme/domaine pour " + terme + ": \n")
    
    lines = re.findall(r'e;\d+;.+',code)
    dico = {
            'eid' : [],
            'nom': [],
            'type' : [],
            'poids': []
            }
    #print(lines )
    #testJoin = '\n'.join(test)
   
    eid = []
    nom = []
    typeM = []
    poids = []

    for l in lines:
        info = l.split(';')
        eid.append(int(info[1]))
        nom.append(info[2])
        typeM.append(int(info[3]))
        poids.append(int(info[4]))

    
    dico.update({'eid' : eid})
    dico.update({'nom' : nom})
    dico.update({'type' :typeM})
    dico.update({'poids' : poids})

    for key, val in dico.items():
        print((key, val))
    
    df = pd.DataFrame(dico)
    #df2 = df[df['poids'] == df['poids'].max()]
    #print(df2)
    df = df.sort_values(by=['poids'])

    #df.to_csv('./test3.csv')

    print(df)

def getAssociations(terme):
    termeHttp = terme
    termeHttp = urllib.parse.quote_plus(termeHttp, encoding='iso-8859-1')
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + termeHttp + '&rel=0'
    html = r.get(url)
    #print (terme + "   " +termeHttp)
    tree = HTMLParser(html.text)
    
    try:
        code = tree.css_first('CODE').text()
    except AttributeError as error:
        print("Le mot" + terme + " n'existe pas" , error)
        return    
    print("Associasions pour " + terme  + ": \n")

    lines = re.findall(r'e;\d+;.+',code)
    dico = {
            'eid' : [],
            'nom': [],
            'type' : [],
            'poids': []
            }
    #print(lines )
   
    eid = []
    nom = []
    typeM = []
    poids = []
    i = 0
    for l in lines:
        info = l.split(';')
       
        eid.append(int(info[1]))
        nom.append(info[2])
        typeM.append(int(info[3]))
        poids.append(int(info[4]))
        i+=1
    
    dico.update({'eid' : eid})
    dico.update({'nom' : nom})
    dico.update({'type' :typeM})
    dico.update({'poids' : poids})
    df = pd.DataFrame(dico)
    #df2 = df[df['poids'] == df['poids'].max()]
    #print(df2)
    df = df.sort_values(by=['poids'])
    #df.to_csv('./test3.csv')
    print(df)

def getParties(terme):

    termeHttp = terme
    termeHttp = urllib.parse.quote_plus(termeHttp, encoding='iso-8859-1')
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + termeHttp + '&rel=9'
    html = r.get(url)
    #print (terme + "   " +termeHttp)
    tree = HTMLParser(html.text)
    
    try:
        code = tree.css_first('CODE').text()
    except AttributeError as error:
        print("Le mot" + terme + " n'existe pas" , error)
        return    
    print("Parties pour " + terme  + ": \n")

    lines = re.findall(r'e;\d+;.+',code)
    dico = {
            'eid' : [],
            'nom': [],
            'type' : [],
            'poids': []
            }
    #print(lines )
   
    eid = []
    nom = []
    typeM = []
    poids = []
    i = 0
    for l in lines:
        info = l.split(';')
       
        eid.append(int(info[1]))
        nom.append(info[2])
        typeM.append(int(info[3]))
        poids.append(int(info[4]))
        i+=1
    
    dico.update({'eid' : eid})
    dico.update({'nom' : nom})
    dico.update({'type' :typeM})
    dico.update({'poids' : poids})
    df = pd.DataFrame(dico)
    #df2 = df[df['poids'] == df['poids'].max()]
    #print(df2)
    df = df.sort_values(by=['poids'])
    #df.to_csv('./test3.csv')
    print(df)

def getContraire(terme):

    termeHttp = terme
    termeHttp = urllib.parse.quote_plus(termeHttp, encoding='iso-8859-1')
    url = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel=' + termeHttp + '&rel=7'
    html = r.get(url)
    #print (terme + "   " +termeHttp)
    tree = HTMLParser(html.text)
    
    try:
        code = tree.css_first('CODE').text()
    except AttributeError as error:
        print("Le mot" + terme + " n'existe pas" , error)
        return    
    print("Contraires pour " + terme  + ": \n")

    lines = re.findall(r'e;\d+;.+',code)
    dico = {
            'eid' : [],
            'nom': [],
            'type' : [],
            'poids': []
            }
    #print(lines )
   
    eid = []
    nom = []
    typeM = []
    poids = []
    i = 0
    for l in lines:
        info = l.split(';')
       
        eid.append(int(info[1]))
        nom.append(info[2])
        typeM.append(int(info[3]))
        poids.append(int(info[4]))
        i+=1
    
    dico.update({'eid' : eid})
    dico.update({'nom' : nom})
    dico.update({'type' :typeM})
    dico.update({'poids' : poids})
    df = pd.DataFrame(dico)
    #df2 = df[df['poids'] == df['poids'].max()]
    #print(df2)
    df = df.sort_values(by=['poids'])
    #df.to_csv('./test3.csv')
    print(df)

start_time = time.time()
terme = sys.argv[1]
getDefinition(terme)
end_def = time.time()
print('Definitions----%s seconds----' %(end_def - start_time))

getThemeDomaine(terme)
end_theme = time.time()
print('Theme/domaine----%s seconds----' %(end_theme - end_def))

getAssociations(terme)
end_assoc = time.time()
print('Associations----%s seconds----' %(end_assoc - end_theme))

getParties(terme)
end_parties = time.time()
print('Parties----%s seconds----' %( end_parties - end_assoc))

getContraire(terme)
end_contraire = time.time()
print('Contraires----%s seconds----' %(  end_contraire - end_parties))
print('Total----%s seconds----' %(  end_contraire - start_time))
