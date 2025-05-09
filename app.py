#Password Strength checker 
import streamlit as st
import re #regular expression is a module which helps to find patterns or special character in text, modify it , replace and match it

st.markdown("""
<style>
.Note{
       border: 2px solid red;
       border-radius : 12px;  
       padding : 15px;
       font-family: sans-serif;  
       font-size: 20px;
       background-color:lightblue ;  
            color: black;   
                             
            }           
 
 .Note p {
            margin : 8px}   


div.stButton>button {
            width : 30%;
            font-size : 40px;
          
             }        
            
            /*center button*/
            .stButton{
  display: flex;
  justify-content: center;
  align-items: center;
  
  }           
            </style>

""" , unsafe_allow_html=True)






#Title
st.title("🔐Password Strength Checker")

#Subtitle
st.subheader("💡Check how secure your password is in real-time")


st.markdown('<div class="Note"><p>Note: your password will not be stored, this is only for checking password strength.</p> <br> <p>Use at least 8 characters, including letters, numbers, and special symbols.</p></div>', unsafe_allow_html=True  )


st.markdown("<br>", unsafe_allow_html=True)

#Input from user
Password = st.text_input("Enter your Password", type="password")

score = 0

if Password:
#check for length, atleast 8 character
 if len(Password) >= 8:
    score += 1
 else:
   st.warning("password should contain at least 8 characters")    


#check for lowercase character, atleast one character    
 if any(lower.islower for lower in Password):
    score += 1
 else:
   st.warning("password should contain at least one lower case character")    

#check for  Uppercase, atleast one character        
 if any(upper.isupper() for upper in Password):
    score +=1
 else:
   st.warning("password should contain at least one Upper case character")    

#check for digit
 if any(digit.isdigit() for digit in Password):
    score += 1   
 else:
   st.warning("password should contain at least one digit character")      

# check for special characte
 if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", Password) :
    score +=1
 else:
   st.warning("password should contain at least one digit character")    


#Check button

if st.button("check password strength "):
    if score == 1 or score == 2:
     st.warning("🔴Your password is weak. Try making it longer or adding special characters")

    elif score == 3 or score == 4:
     st.warning("🟡Your password is okay, but could be stronger. Add more variety.")

    elif score >= 5:
     st.success("🟢Strong password! You're good to go")

    else:
       st.error("❌ Invalid")





