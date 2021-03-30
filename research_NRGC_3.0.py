researchpath="keyword_banks/RSRCH_kywd.txt"
nervegappath="keyword_banks/NRVGP_kywd.txt"
nhumanpath="keyword_banks/~HMN_kywd.txt"
ngcpath="keyword_banks/NGC_kywd.txt"
methods=[["Morphological Assesment","morphologic","Morphologic"],["Functional Assesment","functional","Functional"],["Electrophysiology","electrophysiology","electrophysiological"],["Histology","histological","histology"],["Fluorogold Retrograde Tracing","retrograde","tracing"],["TEM","micrograph","transmission"],["Biocompatibility","biocompatibility","Biocompatibility"]]

keyphrases=[["were evaluated ",50],["were assessed ",40],["were higher in ",85],["were lower for ",75],["were performed ",45],["were implanted ",50],["were prepared ",50],["we have ",40],["We have ",40],["In this study ",60],["in this study ",60],["was similar ",40],["was assessed ",66]]
########################
###funcs
def list_maker(directory):
    parsethru=open(directory,'r')
    filelength=len(parsethru.readlines())
    parsethru.close()
    setparse=open(directory,'r')
    setlist=[["base case", 0]]
    for i in range(0,filelength):
        line=setparse.readline()
        keyword=""
        val=""
        keywordadd=False
        valadd=False
        for char in line:
            if char=="[":
                keywordadd=True
            elif char==",":
                keywordadd=False
                valadd=True
            elif char=="]":
                valadd=False
            else:
                if keywordadd:
                    keyword+=char
                if valadd:
                    val+=char
        setlist.append([keyword,float(val)])
    return setlist
    setparse.close()
def sentence_brk(text):
    sentences=[]
    sentence=""
    for x in text:
        if x==".":
            sentences.append(sentence)
            sentence=""
        else:
            sentence+=x
    return sentences

def mmfinder(text):
    lastword=""
    newword=""
    for i in text:
        if i ==" " or i=="." or i=="-":
            if newword == "millimeters" or newword=="mm":
                return lastword
            else:
                lastword=newword
                newword=""
        else:
            newword+=i
    return "NONE"
        
def article_type(text, keywords,keyphrases):
    wordfiller=""
    phrase=""
    phrasingpass=False
    words_in_phrase=0
    point_sway=-27
    for y in text:
        if y==" " or y=="." or y=="," or y=="(" or y==")":
            for x in range(0,len(keywords)):
                if wordfiller==keywords[x][0]:
                    point_sway+=keywords[x][1]
            if wordfiller=="were" or wordfiller=="was" or wordfiller=="in" or wordfiller=="we" or wordfiller=="We" or wordfiller=="In":
                phrasingpass=True
            if phrasingpass:
                words_in_phrase+=1
                phrase+=wordfiller+" "
                for q in range(0,len(keyphrases)):
                    if phrase==keyphrases[q][0]:
                        point_sway+=keyphrases[q][1]
                        phrasingpass=False
                        phrase=""
                        words_in_phrase=0
                if words_in_phrase>2:
                    phrasingpass=False
                    phrase=""
                    words_in_phrase=0
            wordfiller=""
        else:
            wordfiller+=y
    
    if point_sway>0:
        return "POSITIVE"
    else:
        return "NEGATIVE"

def nerve_gap_check(text,nervekeywords):
    wordfiller=""
    point_sway=-5
    for r in text:
        if r==" " or r=="." or r=="," or r=="(" or r==")":
            for p in range(0,len(nervekeywords)):
                if wordfiller==nervekeywords[p][0]:
                    point_sway+=nervekeywords[p][1]
            wordfiller=""
        else:
            wordfiller+=r
    if point_sway>0:
        return "POSITIVE"
    else:
        return "NEGATIVE"

def ngc_check(text,ngcwords):
    wordfiller=""
    point_sway=-0.1
    for g in text:
        if g==" " or g=="." or g=="," or g=="(" or g==")":
            for f in range(0,len(ngcwords)):
                if wordfiller==ngcwords[f][0]:
                    point_sway+=ngcwords[f][1]
            wordfiller=""
        else:
            wordfiller+=g
    if point_sway>0:
        return "POSITIVE"
    else:
        return "NEGATIVE"

def method_check(text,methodoptions):
    wordfiller=""
    method=[]
    for r in text:
        if r==" " or r=="." or r=="," or r=="(" or r==")":
            for x in range(0,len(methodoptions)):
                for y in range(0,3):
                    if methodoptions[x][y]==wordfiller:
                        method.append(methodoptions[x][0])
            wordfiller=""

        else:
            wordfiller+=r
    if len(method)==0:
        return "NONE FOUND"
    else:
        methodprevalence=[["test",0]]
        for r in range(0,len(method)):
            passer=True
            for g in range(1,len(methodprevalence)):
                if method[r]==methodprevalence[g][0]:
                    passer=False
                    methodprevalence[g][1]=int(methodprevalence[g][1])+1
            if passer:
                methodprevalence.append([method[r],1])
        most_relevant=[0,0]
        for x in range(1,len(methodprevalence)):
            if methodprevalence[x][1]>most_relevant[1]:
                most_relevant=[x,methodprevalence[x][1]]
            elif methodprevalence[x][1]==most_relevant[1]:
                if methodprevalence[x][0]!="Functional Assesment":
                    most_relevant.append(x)
                    most_relevant.append(methodprevalence[x][1])
        if len(most_relevant)>2:
            if methodprevalence[most_relevant[0]][0]!="Functional Assesment":
                return methodprevalence[most_relevant[0]][0]+" and "+methodprevalence[most_relevant[2]][0]
        return methodprevalence[most_relevant[0]][0]
############################

running=True

while running:
    abstract=input("abstract:  ")
    if abstract=="quit":
        running=False
    else:
            print(" ")
            print(mmfinder(abstract)+ " mm")
            print("Research Paper: "+article_type(abstract,list_maker(researchpath),keyphrases))
            print("Peripheral Nerve non-Human Research: "+nerve_gap_check(abstract,list_maker(nervegappath)))
            print("NGC Research: "+ngc_check(abstract,list_maker(ngcpath)))
            print("Method Used: "+method_check(abstract,methods))
            print(" ")
