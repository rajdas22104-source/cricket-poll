



# import streamlit as st
# from PIL import Image
# st.title("sunday poll")

# who=st.text_input("naam daalo")
# b=who.capitalize()
# team={"Ansh":1,"Raj":2,"Kepler":3,"Rajat":4,"Ankush":5,"Akash":6,"Sumit":7,"Tushar":8,"Nithlesh":9,"Shiva":10,}
# if b in team:
#      (st.write(f'ram ram {b} bhai ko'))
# c=(team[b])

# if c==1:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ansh bhai.png",width=200)
# elif c==2:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\raj.png",width=200)
# elif c==3:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\kepler mc.jpeg",width=200)
# elif c==4:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\rajat bhai.png",width=200)
# elif c==5:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ankush bhai.png",width=200)
# elif c==6:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\akash bhai.png",width=200)
# elif c==7:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\sumit bhaiya.png",width=200)
# elif c==8:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\tushar bhai.png",width=200)
# elif c==9:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\nithlesh bhai.png",width=200)
# elif c==10:
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\shiva bhai.png",width=200)
# else:
#           print("tu team mai hi nhi hai")
# whs=st.radio("batao bhai:",["Yes","No"])
# if whs=="Yes":
#           print(st.write("Welcome"))
#           motivate=st.slider("g-faad motivation kitna hai",0,10,2)
# else:
#      print(st.write("you have not one day to play"))
# d=st.selectbox("ball ke paise dedo",["10","20","30","mai toh berozgaar hu"])
# if d!="mai toh berozgaar hu":
#       st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\qr.jpeg",width=200)

# import streamlit as st
# from PIL import Image
# st.title("sunday poll")

# who=st.text_input("naam daalo")
# b=who.capitalize()
# team={"Ansh":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ansh bhai.png",
#       "Raj":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\raj.png",
#       "Kepler":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\kepler mc.jpeg",
#       "Rajat":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\rajat bhai.png",
#       "Ankush":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ankush bhai.png",
#       "Akash":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\akash bhai.png",
#       "Sumit":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\sumit bhaiya.png",
#       "Tushar":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\tushar bhai.png",
#       "Nithlesh":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\nithlesh bhai.png",
#       "Shiva":r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\shiva bhai.png"}
# if b in team:
#      st.write(f'ram ram {b} bhai ko')
#      st.image(f'{team[b]}',width=200)
# else:
#      print("tu team mai hi nhi hai")
# whs=st.radio("batao bhai:",["Yes","No"])
# if whs=="Yes":
#           print(st.write("Welcome"))
#           motivate=st.slider("g-faad motivation kitna hai",0,10,2)
# else:
#      print(st.write("you have not one day to play"))
# d=st.selectbox("ball ke paise dedo",["10","20","30","mai toh berozgaar hu"])
# if d!="mai toh berozgaar hu":
#       st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\qr.jpeg",width=200)
    
# import streamlit as st
# import time

 
# st.title("Sunday Poll")
 
# who = st.text_input("Naam daalo")
# b = who.strip().capitalize()
 
# team = {
#      "Ansh": 1, "Raj": 2, "Kepler": 3, "Rajat": 4, "Ankush": 5,
#      "Akash": 6, "Sumit": 7, "Tushar": 8, "Nithlesh": 9, "Shiva": 10
#  }
 
# photos = {
#      1: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ansh bhai.png",
#      2: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\raj.png",
#      3: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\kepler mc.jpeg",
#      4: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\rajat bhai.png",
#      5: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ankush bhai.png",
#      6: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\akash bhai.png",
#      7: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\sumit bhaiya.png",
#      8: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\tushar bhai.png",
#      9: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\nithlesh bhai.png",
#      10: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\shiva bhai.png",
#  }
 
# if b:
#      if b in team:
#          st.write(f"Ram Ram {b} bhai ko 🙏")
#          c = team[b]
#          st.image(photos[c], width=200)
#      else:
#          st.error("Tu team mai hi nhi hai 😅")
 
# whs = st.radio("Batao bhai:", ["Yes", "No"])
 
# if whs == "Yes":
#      st.success("Welcome")
#      motivate = st.slider("G-faad motivation kitna hai", 0, 10, 2)
#      if motivate==10:
#           st.success("saamne wale ki bund faad denge")
#      else:
#           st.warning("ghanta teri baski nhi hai")
# else:
#      st.warning("You have not one day to play")
 
# d = st.selectbox("Ball ke paise dedo", ["10", "mai toh berozgaar hu"])
 
# if d != "mai toh berozgaar hu":
#      st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\qr.jpeg", width=200)     
     
# else:
#      st.warning("thik hai but rozgaar hoke hai click kiya na toh 10 rs jyada lunga")


import streamlit as st
import time
import webbrowser as wb
import pyautogui as ag


 
st.title("Sunday Poll")
 
who = st.text_input("Naam daalo")
b = who.strip().capitalize()
 
team = {
     "Ansh": 1, "Raj": 2, "Kepler": 3, "Rajat": 4, "Ankush": 5,
     "Akash": 6, "Sumit": 7, "Tushar": 8, "Nithlesh": 9, "Shiva": 10
 }
 
photos = {
     1: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ansh bhai.png",
     2: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\raj.png",
     3: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\kepler mc.jpeg",
     4: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\rajat bhai.png",
     5: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\ankush bhai.png",
     6: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\akash bhai.png",
     7: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\sumit bhaiya.png",
     8: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\tushar bhai.png",
     9: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\nithlesh bhai.png",
     10: r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\shiva bhai.png",
 }
phone= {
     1: "9315697169",
     2: "9958366983",
     3: "8448234527",
     4: "9310325601",
     5: "8595133012",
     6: "7827809273",
     7: "8800300229",
     8: "9625154201",
     9: "8208719186",
     10: "9654782249"
 }

 
if b:
     if b in team:
         st.write(f"Ram Ram {b} bhai ko 🙏")
         c = team[b]
         st.image(photos[c], width=200)
     else:
         st.error("Tu team mai hi nhi hai 😅")
 
whs = st.radio("Batao bhai:", ["clickit","Yes", "No"])
 
if b:
     if whs == "Yes":
          st.success("Welcome")
          phno = team[b]
          wb.open(f"https://web.whatsapp.com/send?phone={phone[phno]}")                #reach you to chat webpage
          time.sleep(50)
          a=0
          while a<1:                                                   #this type and send msg in loop 
               ag.typewrite("yes kara hai na toh ana padega woh bhi ek call nhi jayegi iss baar chup chap ajou")
               ag.press("Enter")
               time.sleep(0.6)
               a+=1
          motivate = st.slider("G-faad motivation kitna hai", 0, 10, 2)
          if motivate==10:
               st.success("saamne wale ki bund faad denge")
     else:
          st.warning("ghanta teri baski nhi hai")
else:
     st.warning("You have not one day to play")
     

 
d = st.selectbox("Ball ke paiso dedo", ["click it","10", "mai toh berozgaar hu"])
# qr=st.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\qr.jpeg", width=200)    
if d == "10":
     st.warning("1 minute ke andar karde warna qr chala jayega")
     qr_placeholder=st.empty()
     qr_placeholder.image(r"C:\Users\rajat\OneDrive\Desktop\cricket poll\photos\qr.jpeg",width=200)
     time.sleep(10)
     qr_placeholder.empty()
     st.status("lets admin check")

          
else:
     st.warning("thik hai but rozgaar hoke hai click kiya na toh 10 rs jyada lunga")



admin=st.text_input("admin hi khede")
password=st.text_input("password tumhe nhi pata hoga")
if password=="raj@1234#&raj":
     ok=st.checkbox("ok")
     if ok is True:
          phno = team[b]
          wb.open(f"https://web.whatsapp.com/send?phone={phone[phno]}")                #reach you to chat webpage
          time.sleep(20)
          a=0 
          while a<1:                                                   #this type and send msg in loop 
               ag.typewrite("chal bhai paise aagye ustaad ball ke liye")
               ag.press("Enter")
               time.sleep(0.6)
               a+=1

else:
     st.empty()
# if b:
      
#       if ok is True:
#           phno = team[b]
#           wb.open(f"https://web.whatsapp.com/send?phone={phone[phno]}")                #reach you to chat webpage
#           time.sleep(50)
#           a=0 
#           while a<1:                                                   #this type and send msg in loop 
#                ag.typewrite("yes kara hai na toh ana padega woh bhi ek call nhi jayegi iss baar chup chap ajou")
#                ag.press("Enter")
#                time.sleep(0.6)
#                a+=1
