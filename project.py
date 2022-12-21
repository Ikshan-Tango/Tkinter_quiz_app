from tkinter import *
from playsound import playsound
from gtts import gTTS
import time
import os

window = Tk()
window.resizable(0, 0)

solution= [1,4,3,4,2,1,3,1,2,2]


def submit():
    global count
    count=0
    print(count)
    entered= []
    a1 = r1.get()
    entered.append(a1)    
    a2 = r2.get()
    entered.append(a2)  
    a3 = r3.get()
    entered.append(a3)  
    a4 = r4.get()
    entered.append(a4)    
    a5 = r5.get()
    entered.append(a5)
    a6 = r6.get()
    entered.append(a6)    
    a7 = r7.get()
    entered.append(a7)    
    a8 = r8.get()
    entered.append(a8)
    a9 = r9.get()
    entered.append(a9)
    a10 = r10.get()
    entered.append(a10)
    print(entered)
    marks=0
    correct=0
    incorrect=0
 
   


    for i in range(0,10):
        if solution[i]==entered[i]:
            marks= marks+1
            correct= correct+1
        else:
            incorrect= incorrect+1
            #marks=marks-1
   
    marksmessage="YOU SCORED: "+str(marks)
    correctmessage="CORRECT: "+str(correct)
    incorrectmessage="INCORRECT: "+str(incorrect)
   
    marks_label = Label(window, text=marksmessage, width="30", height="5", wraplength=1000, bg="light blue")
    marks_label.config(font=("Courier", 50))
    correct_label = Label(window, text=correctmessage, width="30", height="4", wraplength=1000)
    correct_label.config(font=("Courier", 30))
    incorrect_label = Label(window, text=incorrectmessage, width="30", height="4", wraplength=1000)
    incorrect_label.config(font=("Courier", 30))
   
   
    question10.pack_forget()
    q10option1.pack_forget()
    q10option2.pack_forget()
    q10option3.pack_forget()
    q10option4.pack_forget()
    audiobutton1.pack_forget()
    submit_btn.pack_forget()
    back_key.pack_forget()
   
    marks_label.pack()
    correct_label.pack()
    incorrect_label.pack()
   
def enter_quiz():
    #quiz entering
    global count
    count += 1
    quiznamelabel.pack_forget()
    xspacewidget.pack_forget()
    startkey.pack_forget()
    quizdesclabel.pack_forget()
    question1.pack()
    q1option1.pack()
    q1option2.pack()
    q1option3.pack()
    q1option4.pack()
    audiobutton1.pack()
    next_key.pack(side="right")
   
    #Timer
    seconds=0
    minutes=0
    hours=0
    run="y"

    while run.lower()=="y":        
        time_screen=(str(hours)+":"+str(minutes)+":"+str(seconds))
        tym=Label(text=time_screen)
        tym.config(font=("Courier", 20))
       
        for i in range(10):
            tym.pack()
            window.update()
       
            time.sleep(0.1)
            tym.forget()
            window.update()
       
        seconds+=1        
        if seconds==60:
            seconds=0
            minutes+=1
        if minutes==60:
            seconds=0
            minutes=0
            hours+=1
       
       
           
#--------#time over condition    
        if seconds==00 and minutes==1 or count==0:      
            print("Time over BOI")      
            run="no"
            print(count)
            if (count == 1):
                question1.pack_forget()
                q1option1.pack_forget()
                q1option2.pack_forget()
                q1option3.pack_forget()
                q1option4.pack_forget()
                next_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 2):
                question2.pack_forget()
                q2option1.pack_forget()
                q2option2.pack_forget()
                q2option3.pack_forget()
                q2option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 3):
                question3.pack_forget()
                q3option1.pack_forget()
                q3option2.pack_forget()
                q3option3.pack_forget()
                q3option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 4):
                question4.pack_forget()
                q4option1.pack_forget()
                q4option2.pack_forget()
                q4option3.pack_forget()
                q4option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 5):
                question5.pack_forget()
                q5option1.pack_forget()
                q5option2.pack_forget()
                q5option3.pack_forget()
                q5option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 6):
                question6.pack_forget()
                q6option1.pack_forget()
                q6option2.pack_forget()
                q6option3.pack_forget()
                q6option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 7):
                question7.pack_forget()
                q7option1.pack_forget()
                q7option2.pack_forget()
                q7option3.pack_forget()
                q7option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 8):
                question8.pack_forget()
                q8option1.pack_forget()
                q8option2.pack_forget()
                q8option3.pack_forget()
                q8option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 9):
                question9.pack_forget()
                q9option1.pack_forget()
                q9option2.pack_forget()
                q9option3.pack_forget()
                q9option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()
            elif (count == 10):
                question10.pack_forget()
                q10option1.pack_forget()
                q10option2.pack_forget()
                q10option3.pack_forget()
                q10option4.pack_forget()
                next_key.pack_forget()
                back_key.pack_forget()
                audiobutton1.pack_forget()
                submit()



def pageno_add():
    global count
    count += 1
    print(count)
   
    if (count == 2):
        question1.pack_forget()
        q1option1.pack_forget()
        q1option2.pack_forget()
        q1option3.pack_forget()
        q1option4.pack_forget()
        next_key.pack_forget()
        audiobutton1.pack_forget()

        question2.pack()
        q2option1.pack()
        q2option2.pack()
        q2option3.pack()
        q2option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
        # submit_btn.pack()
    elif (count == 3):
        question2.pack_forget()
        q2option1.pack_forget()
        q2option2.pack_forget()
        q2option3.pack_forget()
        q2option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question3.pack()
        q3option1.pack()
        q3option2.pack()
        q3option3.pack()
        q3option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 4):
        question3.pack_forget()
        q3option1.pack_forget()
        q3option2.pack_forget()
        q3option3.pack_forget()
        q3option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question4.pack()
        q4option1.pack()
        q4option2.pack()
        q4option3.pack()
        q4option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 5):
        question4.pack_forget()
        q4option1.pack_forget()
        q4option2.pack_forget()
        q4option3.pack_forget()
        q4option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question5.pack()
        q5option1.pack()
        q5option2.pack()
        q5option3.pack()
        q5option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 6):
        question5.pack_forget()
        q5option1.pack_forget()
        q5option2.pack_forget()
        q5option3.pack_forget()
        q5option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question6.pack()
        q6option1.pack()
        q6option2.pack()
        q6option3.pack()
        q6option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 7):
        question6.pack_forget()
        q6option1.pack_forget()
        q6option2.pack_forget()
        q6option3.pack_forget()
        q6option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question7.pack()
        q7option1.pack()
        q7option2.pack()
        q7option3.pack()
        q7option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 8):
        question7.pack_forget()
        q7option1.pack_forget()
        q7option2.pack_forget()
        q7option3.pack_forget()
        q7option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question8.pack()
        q8option1.pack()
        q8option2.pack()
        q8option3.pack()
        q8option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 9):
        question8.pack_forget()
        q8option1.pack_forget()
        q8option2.pack_forget()
        q8option3.pack_forget()
        q8option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question9.pack()
        q9option1.pack()
        q9option2.pack()
        q9option3.pack()
        q9option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")
    elif (count == 10):
        question9.pack_forget()
        q9option1.pack_forget()
        q9option2.pack_forget()
        q9option3.pack_forget()
        q9option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question10.pack()
        q10option1.pack()
        q10option2.pack()
        q10option3.pack()
        q10option4.pack()
        audiobutton1.pack()
        submit_btn.pack()
        back_key.pack(side="left")
     
   

def pageno_subtract():
    global count
    count -= 1
    print(count)
    if (count == 1):
        question2.pack_forget()
        q2option1.pack_forget()
        q2option2.pack_forget()
        q2option3.pack_forget()
        q2option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question1.pack()
        q1option1.pack()
        q1option2.pack()
        q1option3.pack()
        q1option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")

    elif (count == 2):
        question3.pack_forget()
        q3option1.pack_forget()
        q3option2.pack_forget()
        q3option3.pack_forget()
        q3option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question2.pack()
        q2option1.pack()
        q2option2.pack()
        q2option3.pack()
        q2option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 3):
        question4.pack_forget()
        q4option1.pack_forget()
        q4option2.pack_forget()
        q4option3.pack_forget()
        q4option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question3.pack()
        q3option1.pack()
        q3option2.pack()
        q3option3.pack()
        q3option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 4):
        question5.pack_forget()
        q5option1.pack_forget()
        q5option2.pack_forget()
        q5option3.pack_forget()
        q5option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question4.pack()
        q4option1.pack()
        q4option2.pack()
        q4option3.pack()
        q4option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 5):
        question6.pack_forget()
        q6option1.pack_forget()
        q6option2.pack_forget()
        q6option3.pack_forget()
        q6option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question5.pack()
        q5option1.pack()
        q5option2.pack()
        q5option3.pack()
        q5option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 6):
        question7.pack_forget()
        q7option1.pack_forget()
        q7option2.pack_forget()
        q7option3.pack_forget()
        q7option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question6.pack()
        q6option1.pack()
        q6option2.pack()
        q6option3.pack()
        q6option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 7):
        question8.pack_forget()
        q8option1.pack_forget()
        q8option2.pack_forget()
        q8option3.pack_forget()
        q8option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question7.pack()
        q7option1.pack()
        q7option2.pack()
        q7option3.pack()
        q7option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 8):
        question9.pack_forget()
        q9option1.pack_forget()
        q9option2.pack_forget()
        q9option3.pack_forget()
        q9option4.pack_forget()
        next_key.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question8.pack()
        q8option1.pack()
        q8option2.pack()
        q8option3.pack()
        q8option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

    elif (count == 9):
        question10.pack_forget()
        q10option1.pack_forget()
        q10option2.pack_forget()
        q10option3.pack_forget()
        q10option4.pack_forget()
        submit_btn.pack_forget()
        back_key.pack_forget()
        audiobutton1.pack_forget()

        question9.pack()
        q9option1.pack()
        q9option2.pack()
        q9option3.pack()
        q9option4.pack()
        audiobutton1.pack()
        next_key.pack(side="right")
        back_key.pack(side="left")

user_answer = []

#def submit():
#   global

def convert_audio1():
    global count
    global question1_string
    global question2_string
    global question3_string
    global question4_string
    global question5_string
    global question6_string
    global question7_string
    global question8_string
    global question9_string
    global question10_string

    if (count == 1):
        mytext = question1_string
        language = 'en'
        if (os.path.isfile("audio1.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio1.mp3")
            playsound("audio1.mp3")
        else:
            playsound("audio1.mp3")
    elif (count == 2):
        mytext = question2_string
        language = 'en'
        if (os.path.isfile("audio2.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio2.mp3")
            playsound("audio2.mp3")
        else:
            playsound("audio2.mp3")
    elif (count == 3):
        mytext = question3_string
        language = 'en'
        if (os.path.isfile("audio3.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio3.mp3")
            playsound("audio3.mp3")
        else:
            playsound("audio3.mp3")
    elif (count == 4):
        mytext = question4_string
        language = 'en'
        if (os.path.isfile("audio4.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio4.mp3")
            playsound("audio4.mp3")
        else:
            playsound("audio4.mp3")
    elif (count == 5):
        mytext = question5_string
        language = 'en'
        if (os.path.isfile("audio5.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio5.mp3")
            playsound("audio5.mp3")
        else:
            playsound("audio5.mp3")
    elif (count == 6):
        mytext = question6_string
        language = 'en'
        if (os.path.isfile("audio6.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio6.mp3")
            playsound("audio6.mp3")
        else:
            playsound("audio6.mp3")
    elif (count == 7):
        mytext = question7_string
        language = 'en'
        if (os.path.isfile("audio7.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio7.mp3")
            playsound("audio7.mp3")
        else:
            playsound("audio7.mp3")
    elif (count == 8):
        mytext = question8_string
        language = 'en'
        if (os.path.isfile("audio8.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio8.mp3")
            playsound("audio8.mp3")
        else:
            playsound("audio8.mp3")
    elif (count == 9):
        mytext = question9_string
        language = 'en'
        if (os.path.isfile("audio9.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio9.mp3")
            playsound("audio9.mp3")
        else:
            playsound("audio9.mp3")
    elif (count == 10):
        mytext = question10_string
        language = 'en'
        if (os.path.isfile("audio10.mp3") == False):
            output = gTTS(text=mytext, lang=language, slow=False)
            output.save("audio10.mp3")
            playsound("audio10.mp3")
        else:
            playsound("audio10.mp3")


count = 0
# intro screen
# name of quiz
quiznamelabel = Label(window, text="Mindforge Quiz", width="30", height="5", anchor="center", bg="light blue")
quiznamelabel.pack()
quiznamelabel.config(font=("Courier", 50))

# space
xspacewidget = Label(window, text="", height="2")
xspacewidget.pack()

# start button
startkey = Button(text="Begin quiz", width="10", height="1", bg="light blue", command=enter_quiz)
startkey.pack()
startkey.config(font=("ariel", 20))

# description
quizdesclabel = Label(window, text="Crack competetive exams with ease!", height="4")
quizdesclabel.pack()
quizdesclabel.config(font=("ariel", 20))
# ------------------------------------------------------------------------------------------------------------------------------------------------

#answer list =

# questions
# question1
question1_string = "what is a solenoid?"
question1 = Label(window, text=question1_string, width="30", wraplength=1000, height="5", anchor="center",
                  bg="light blue")
question1.config(font=("Courier", 50))
# options q1
r1 = IntVar()
q1option1 = Radiobutton(window, text="wire coil with current passing", variable=r1, value=1, )
q1option1.config(font=("Courier", 20))
q1option2 = Radiobutton(window, text="horrible question", variable=r1, value=2)
q1option2.config(font=("Courier", 20))
q1option3 = Radiobutton(window, text="a horseshoe magnet", variable=r1, value=3)
q1option3.config(font=("Courier", 20))
q1option4 = Radiobutton(window, text="a bar magnet", variable=r1, value=4)
q1option4.config(font=("Courier", 20))
audiobutton1 = Button(text="convert to audio", command=convert_audio1, width="30", height="2", bg="grey")



#answer1
#ans1_choice = ['1', '2', '3', '4'] - ishita 2021

# ----------------------------------------------
# question2
question2_string = "What phenomena did Young's double slit experiment explain?"
question2 = Label(window, text=question2_string, width="30", height="5", wraplength=1000, bg="light blue")
question2.config(font=("Courier", 50))

# options q2
r2 = IntVar()
q2option1 = Radiobutton(window, text="Monke", variable=r2, value=1, )
q2option1.config(font=("Courier", 20))
q2option2 = Radiobutton(window, text="No cLue", variable=r2, value=2)
q2option2.config(font=("Courier", 20))
q2option3 = Radiobutton(window, text="Banana everywhere", variable=r2, value=3)
q2option3.config(font=("Courier", 20))
q2option4 = Radiobutton(window, text="Wave nature of light", variable=r2, value=4)
q2option4.config(font=("Courier", 20))

#ans2_choice = ['1', '2', '3', '4']- ishita 2021


# ------------------------------------

# question3
question3_string = "radiocarbon is produced in the atmosphere as a result of what?"
question3 = Label(window, text=question3_string, width="30", height="5", wraplength=1000, bg="light blue")
question3.config(font=("Courier", 50))

# options q3
r3 = IntVar()
q3option1 = Radiobutton(window, text="Collision between fast neutrons and nitrogen nuclei present in the atmosphere.",
                        variable=r3, value=1, wraplength=1200)
q3option1.config(font=("Courier", 20))
q3option2 = Radiobutton(window, text="Action of ultraviolet light from the sun on atmospheric oxygen.", variable=r3,
                        value=2, wraplength=1200)
q3option2.config(font=("Courier", 20))
q3option3 = Radiobutton(window,
                        text="Action of solar radiations particularly cosmic rays on carbon dioxide present in the atmosphere.",
                        variable=r3, value=3, wraplength=1200)
q3option3.config(font=("Courier", 20))
q3option4 = Radiobutton(window, text="Lightning discharge in atmosphere.", variable=r3, value=4, wraplength=1200)
q3option4.config(font=("Courier", 20))

# ------------------------------------


# question4
question4_string = "It is easier to roll a stone up  a sloping road than to lift it vertical upwards because?"
question4 = Label(window, text=question4_string, width="30", height="5", wraplength=1000, bg="light blue")
question4.config(font=("Courier", 50))

# options q4
r4 = IntVar()
q4option1 = Radiobutton(window, text="Work done in rolling is more than in lifting.   ", variable=r4, value=1, )
q4option1.config(font=("Courier", 20))
q4option2 = Radiobutton(window, text="Work done in lifting the stone is equal to rolling it.   ", variable=r4, value=2)
q4option2.config(font=("Courier", 20))
q4option3 = Radiobutton(window, text="Work done in both is same but the rate of doing work is less in rolling.",
                        variable=r4, value=3)
q4option3.config(font=("Courier", 20))
q4option4 = Radiobutton(window, text="Work done in rolling a stone is less than in lifting it. ", variable=r4, value=4)
q4option4.config(font=("Courier", 20))
# ------------------------------------

# question5
question5_string = "the absorption of ink by plotting paper involves what?"
question5 = Label(window, text=question5_string, width="30", height="5", wraplength=1000, bg="light blue")
question5.config(font=("Courier", 50))

# options q5
r5 = IntVar()
q5option1 = Radiobutton(window, text="Viscosity of ink  ", variable=r5, value=1, )
q5option1.config(font=("Courier", 20))
q5option2 = Radiobutton(window, text="Capillary action phenomenon", variable=r5, value=2)
q5option2.config(font=("Courier", 20))
q5option3 = Radiobutton(window, text="Diffusion of ink through the blotting.", variable=r5, value=3)
q5option3.config(font=("Courier", 20))
q5option4 = Radiobutton(window, text="Siphon action .", variable=r5, value=4)
q5option4.config(font=("Courier", 20))


# ----------------------------------------------------------------------

# question6
question6_string = "Nuclear sizes are expressed in a unit named ?"
question6 = Label(window, text=question6_string, width="30", height="5", wraplength=1000, bg="light blue")
question6.config(font=("Courier", 50))

# options q6
r6 = IntVar()
q6option1 = Radiobutton(window, text="Fermi", variable=r6, value=1, )
q6option1.config(font=("Courier", 20))
q6option2 = Radiobutton(window, text="Angstrom", variable=r6, value=2)
q6option2.config(font=("Courier", 20))
q6option3 = Radiobutton(window, text="Newton", variable=r6, value=3)
q6option3.config(font=("Courier", 20))
q6option4 = Radiobutton(window, text="Tesla", variable=r6, value=4)
q6option4.config(font=("Courier", 20))

# ----------------------------------------------------------------------
# question7
question7_string = "Light year is a unit  of?"
question7 = Label(window, text=question7_string, width="30", height="5", wraplength=1000, bg="light blue")
question7.config(font=("Courier", 50))

# options q7
r7 = IntVar()
q7option1 = Radiobutton(window, text="Light", variable=r7, value=1, )
q7option1.config(font=("Courier", 20))
q7option2 = Radiobutton(window, text="Time", variable=r7, value=2)
q7option2.config(font=("Courier", 20))
q7option3 = Radiobutton(window, text="Distance", variable=r7, value=3)
q7option3.config(font=("Courier", 20))
q7option4 = Radiobutton(window, text="Intensity Of Light", variable=r7, value=4)
q7option4.config(font=("Courier", 20))

# ----------------------------------------------------------------------
# question8
question8_string = "Mirage is due to _____"
question8 = Label(window, text=question8_string, width="30", height="5", wraplength=1000, bg="light blue")
question8.config(font=("Courier", 50))

# options q8
r8 = IntVar()
q8option1 = Radiobutton(window, text="Unequal heating of different parts of the atmosphere", variable=r8, value=1, )
q8option1.config(font=("Courier", 20))
q8option2 = Radiobutton(window, text="Magnetic disturbances in the atmosphere", variable=r8, value=2)
q8option2.config(font=("Courier", 20))
q8option3 = Radiobutton(window, text="Depletion of ozone layer in the atmosphere", variable=r8, value=3)
q8option3.config(font=("Courier", 20))
q8option4 = Radiobutton(window, text="Equal heating of different parts of the atmosphere", variable=r8, value=4)
q8option4.config(font=("Courier", 20))

# ----------------------------------------------------------------------
# question9
question9_string = "Stars appears to move from east to west because?"
question9 = Label(window, text=question9_string, width="30", height="5", wraplength=1000, bg="light blue")
question9.config(font=("Courier", 50))

# options q9
r9 = IntVar()
q9option1 = Radiobutton(window, text="All stars move from east to west   ", variable=r9, value=1, )
q9option1.config(font=("Courier", 20))
q9option2 = Radiobutton(window, text="The earth rotates from west to east", variable=r9, value=2)
q9option2.config(font=("Courier", 20))
q9option3 = Radiobutton(window, text="The earth rotates from east to west", variable=r9, value=3)
q9option3.config(font=("Courier", 20))
q9option4 = Radiobutton(window, text="The background of the stars moves from west to east", variable=r9, value=4)
q9option4.config(font=("Courier", 20))

# -------------------------------------------------------------------------------------------------------
# question10
question10_string = "pa(pascal) is the unit "
question10 = Label(window, text=question10_string, width="30", height="5", wraplength=1000, bg="light blue")
question10.config(font=("Courier", 50))

# options q10
r10 = IntVar()
q10option1 = Radiobutton(window, text="Thrust", variable=r10, value=1, )
q10option1.config(font=("Courier", 20))
q10option2 = Radiobutton(window, text="Pressure", variable=r10, value=2)
q10option2.config(font=("Courier", 20))
q10option3 = Radiobutton(window, text="Frequency", variable=r10, value=3)
q10option3.config(font=("Courier", 20))
q10option4 = Radiobutton(window, text="Conductivity", variable=r10, value=4)
q10option4.config(font=("Courier", 20))

# --------------------------------------------------------------------------------------------------------
#submit page




# --------------------------------------------------------------------------------------------------------
#submit button
submit_btn = Button(text="SUBMIT", width="9", height="1", bg="light blue" ,command=submit)
submit_btn.config(font=("ariel", 15))
# ----------------------------------------------------------------------------------
# next button
next_key = Button(text=">>>", width="5", height="1", bg="light blue", command=pageno_add)
next_key.config(font=("ariel", 15))

# back button
back_key = Button(text="<<<", width="5", height="1", bg="light blue", command=pageno_subtract)
back_key.config(font=("ariel", 15))

# --------------------------------------------------------------------------------------------------------      
window.mainloop()