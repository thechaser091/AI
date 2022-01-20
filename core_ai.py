import pywhatkit as kt
import speech_recognition as sr
import gtts
import pyttsx3
import cloudprint
import webbrowser

# initialize Text-to-speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()
voices = engine.getProperty("voices")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.say("booting up")
engine.runAndWait()




    
        
        



def ai_maths():
    a = input("+, %, x ???");
    if(a == "+"):
        a = input("?")
        m = int(a)
        print("+");
        a = input("?");
        m2 = int(a)
        print(m + m2);
        ai_loop();
    if(a == "x" or a == "*"):
        a = input("?")
        m = int(a)
        print("*")
        a = input("?")
        m2 = int(a)
        print(m * m2);
        ai_loop();
    if(a == "/" or a == "%"):
        a = input("?")
        m = int(a)
        print("%");
        a = input("?");
        m2 = int(a);
        print(m / m2)
        ai_loop();
    


def ai_google(a):
    from googlesearch import search

    query = a

    for i in search(query, tld="co.in", num=10, stop=1, pause=2):
        print("\n")
        print(i)
        webbrowser.open(i, new=2)
    ai_loop();
    
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

		return audio
		
        
    
def ai_loop():
    
    a = input("?")
    if(a == "restart"):
            print("rebooting");
            import restart
            exit();
    if(a == "exit"):
        exit();
    if(a == "what is this"):
        engine.say("what is it")
        # play the speech
        engine.runAndWait()
        a = input("?");
        ip = a
        kt.search(ip);
        ai_loop();
    if(not a.find("what is") == -1):
        try:
            open("ai_speech/" + a + ".txt", "r")
        except:
            ai_google(a);
                
    if(not a.find("how to") == -1):
        ai_google(a);
    if(not a.find("how do") == -1):
        ai_google(a);

    if(not a.find("math") == -1 or not a.find("maths")):
        ai_maths();
    if(not a.find("my name") == -1):
        a = input("sorry whats your name???");
        file = open("user_name", "w")
        file.write();
            
        ai_loop();
            
    if(a == "hi"):
        try:
            file = open("user_name", "r")
            printstr = str('hi ' + file.read())
            print(printstr)
                
                
            if(printstr == 'hi '):
                print("error try 'reboot' command ");
                ai_loop();
                engine.say(printstr)
                # play the speechxss
                engine.runAndWait()
                ai_loop();
        except:
            print("hi what is your name");
            engine.say("hi what is your name")
            # play the speechxss
            engine.runAndWait()
            a = input();
            file2 = open("user_name", "w");
                
            file2.write(a);
            ai_loop();

                
       
    file = open("ai_speech/" + a + ".txt", 'r')        
    engine.say(file.read())
    # play the speechxss
    engine.runAndWait()
    if(file.read() == "restart"):
        print("rebooting");
        import restart
        exit();
    ai_loop();
    
        
ai_loop();


    
