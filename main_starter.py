import pygame as p
python3 hello.py
###cols
BLACK=[0,0,0]
WHITE=[255,255,255]
RED=[255,0,0]
GREEN=[0,255,0]
GRAY=[120,120,120]
###pygame funcs
def fill_correct(vals):
    p.init()
    screen=p.display.set_mode((300,300))
    p.display.set_caption('NGC Research Checker')
    screen.fill(BLACK)
    font = p.font.Font(None,50)
    font2=p.font.Font(None,20)
    font3=p.font.Font(None,25)
    p.draw.rect(screen,fill_suplement(vals[1]),(6,10,88,100))
    screen.blit(font3.render("Research",False,WHITE),(10,45))
    p.draw.rect(screen,fill_suplement(vals[2]),(106,10,88,100))
    screen.blit(font3.render("Peripheral",False,WHITE),(108,30))
    screen.blit(font3.render("Nerve",False,WHITE),(110,52))
    screen.blit(font2.render("(non human)",False,WHITE),(110,82))
    p.draw.rect(screen,fill_suplement(vals[3]),(206,10,88,100))
    screen.blit(font.render("NGC",False,WHITE),(214,45))
    p.draw.rect(screen,GRAY,(20,140,260,90))
    screen.blit(font3.render(vals[4],False,WHITE),(37,183))
    screen.blit(font2.render(vals[0],False,WHITE),(129,270))
    p.display.update()
def fill_suplement(inp):
    if inp=="POSITIVE":
        return GREEN
    elif inp=="NEGATIVE":
        return RED
    else:
        return GRAY
##################################
print("Would you like to have an aditional window run with graphics? ")
startup=input("enter 'y' for yes, or 'n' to run the program just in this IDLE console     :   ")
running=True
if startup=="y":
    print(" ")
    print(" ")
    print("OK. every time abstract is entered, a window will pop up with the determined values.")
    print("red means NEGATIVE, green means POSITIVE.")
    print("the bottom number is the milimeter count.")
    print(" ")
    print(" ")
    print(" ")

    while running:
        abstract=input("abstract:  ")
        if abstract=="quit":
            running=False
        else:
            printvalues=[mmfinder(abstract),article_type(abstract,keywords,keyphrases),nerve_gap_check(abstract,nerve_gap_words),ngc_check(abstract,ngc_keywords),method_check(abstract,methods)]
            fill_correct(printvalues)
            print(" ")
            print(printvalues[0]+ " mm")
            print("Research Paper: "+printvalues[1])
            print("Peripheral Nerve non-Human Research: "+printvalues[2])
            print("NGC Research: "+printvalues[3])
            print("Method Used: "+printvalues[4])
            print(" ")
                          
elif startup!="n":
    print("not valid, program is closing now. Read better next time.")
    quit()
    
