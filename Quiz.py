
n = 0
marks = 10
#PPT question - Quiz game -- using if conditions
# name = input ("Please enter your name: ")
# print ("Hi " + name +" ,\nWelcome to online quiz game.\nYou have to answere ten multiple choice questions. ")
# wish = input ("Do you wish to continue? Y / N ")
# if (wish.upper() == "Y" ):
#     ans = input("Who was the first prime minister of independent India? \na) Jawahar Lal Nehru\t b) Indira Gandhi \nc) Sonia Gandhi\t\t d) Rahul Gandhi\nAnswere: " )
#     print ("You have scored 10 points!!!")
#     if (ans == "a"):
#         choice = input("Do you wish to continue? Y / N ")            
#         if choice == "Y":
#             print ("2nd question")
#         else:
#             print ("Have a great day. Bye!")
#             pass
#     else:
#         print("You have entered a wrong answere!!")
#         pass
# else:
#     print ("Have a great day. Bye!")
#     pass
## PPT question -- using dictionary
#passing n and marks as input parameters to all the functions
# def wish(n, marks):
#     if (n < 10) :
#         wishoption = input ("Do you wish to continue? Y / N ")
#         if (wishoption.upper() == "Y"):
#             print ("Questions")
#             questions(n , marks)
#         else:
#             pass
#     else:
#         print("Congratulations!! you have successfully answered all the questions!")
#         pass
# def questions(n , marks):
    
#     print (list(dictQuestions.values())[n])
#     ans = input("Answere : ")
#     if (ans.upper() == list(dictAnsweres.values())[n]) : 
       
#         print ("Correct Answere!!    You have scored "+ str(marks) +" points.")
#         wish(n+1, marks+10)
#     else: 
#         print ("Incorrect Answere. You have scored "+ str(marks) +" points. Bye.")

# dictQuestions = {1: "1)Who was the first Indian woman in Space?\nA)Kalpana Chawla\tB)Sunita Williams\nC)Koneru Humpy\t\tD)None of the above.\n"
# ,2: "2)Who was the first Indian in space?\nA)Vikram Ambalal \tB)Ravish Malhotra\nC)Rakesh Sharma\t\tD)Nagapathi Bhat.\n"
# ,3: "3)Who was the first Man to Climb Mount Everest Without Oxygen?\nA)Junko Tabei\t\tB)Reinhold Messner\nC)Peter Habeler\t\tD)Phu Dorji.\n"
# ,4: "4)Who built the Jama Masjid?\nA)Jahangir\t\tB)Akbar\nC)Imam Bukhari\t\tD)Shah Jahan.\n"
# ,5: "5)Who wrote the Indian National Anthem?\nA)Bakim Chandra Chatterji\tB)Rabindranath Tagore\nC)Swami Vivekanand\t\tD)None of the above.\n"
# ,6: "6)Who was the first Indian Scientist to win a Nobel Prize?\nA)CV Raman\t\tB)Amartya Sen\nC)Hargobind Khorana\tD) Subramanian Chrandrashekar.\n"
# ,7: "7)Who is the first Indian to win a Nobel Prize?\nA) Rabindranath Tagore\t\tB)CV Raman\nC)Mother Theresa\t\tD)Hargobind Khorana.\n"
# ,8: "8)Who was the first Indian woman to win the Miss World Title?\nA) Aishwarya Rai\tB)Sushmita Sen\nC)Reita Faria\t\tD)Diya Mirza\n"
# ,9: "9)Who was the first President of India?\nA)Abdul Kalam\t\tB)Lal Bahadur Shastri\nC)Dr. Rajendra Prasad\tD)Zakir Hussain\n"
# ,10: "10)Who was the first Indian to win the Booker Prize?\nA)Dhan Gopal Mukerji\tB)Nirad C. Chaudhuri\nC)Arundhati Roy\t\tD)Aravind Adiga \n"}

# dictAnsweres = {1:"A",2:"C",3:"D",4:"D",5:"B",6:"A",7:"A",8:"C",9:"C",10:"C"}

# name = input ("Please enter your name: ")
# print ("Hi " + name +" ,\nWelcome to online quiz game.\nYou have to answere ten multiple choice questions. ")
# n = 0
# marks = 10
# wish(n , marks)
## Quiz question using global variables
def wish():
    global n
    if (n < 10) :
        wishoption = input ("Do you wish to continue? Y / N ")
        if (wishoption.upper() == "Y"):
            print ("Questions")

            questions()
        else:
            pass
    else:
        print("Congratulations!! you have successfully answered all the questions!")
        pass

def questions():
    global n
    global marks
    print (list(dictQuestions.values())[n])
    ans = input("Answere : ")
    if (ans.upper() == list(dictAnsweres.values())[n]) : 
       
        print ("Correct Answere!!    You have scored "+ str(marks) +" points.")
        n = n + 1
        marks = marks + 10
        wish()
    else: 
        print ("Incorrect Answere. You have scored "+ str(marks) +" points. Bye.")

dictQuestions = {1: "1)Who was the first Indian woman in Space?\nA)Kalpana Chawla\tB)Sunita Williams\nC)Koneru Humpy\t\tD)None of the above.\n"
,2: "2)Who was the first Indian in space?\nA)Vikram Ambalal \tB)Ravish Malhotra\nC)Rakesh Sharma\t\tD)Nagapathi Bhat.\n"
,3: "3)Who was the first Man to Climb Mount Everest Without Oxygen?\nA)Junko Tabei\t\tB)Reinhold Messner\nC)Peter Habeler\t\tD)Phu Dorji.\n"
,4: "4)Who built the Jama Masjid?\nA)Jahangir\t\tB)Akbar\nC)Imam Bukhari\t\tD)Shah Jahan.\n"
,5: "5)Who wrote the Indian National Anthem?\nA)Bakim Chandra Chatterji\tB)Rabindranath Tagore\nC)Swami Vivekanand\t\tD)None of the above.\n"
,6: "6)Who was the first Indian Scientist to win a Nobel Prize?\nA)CV Raman\t\tB)Amartya Sen\nC)Hargobind Khorana\tD) Subramanian Chrandrashekar.\n"
,7: "7)Who is the first Indian to win a Nobel Prize?\nA) Rabindranath Tagore\t\tB)CV Raman\nC)Mother Theresa\t\tD)Hargobind Khorana.\n"
,8: "8)Who was the first Indian woman to win the Miss World Title?\nA) Aishwarya Rai\tB)Sushmita Sen\nC)Reita Faria\t\tD)Diya Mirza\n"
,9: "9)Who was the first President of India?\nA)Abdul Kalam\t\tB)Lal Bahadur Shastri\nC)Dr. Rajendra Prasad\tD)Zakir Hussain\n"
,10: "10)Who was the first Indian to win the Booker Prize?\nA)Dhan Gopal Mukerji\tB)Nirad C. Chaudhuri\nC)Arundhati Roy\t\tD)Aravind Adiga \n"}

dictAnsweres = {1:"A",2:"C",3:"D",4:"D",5:"B",6:"A",7:"A",8:"C",9:"C",10:"C"}

name = input ("Please enter your name: ")
print ("Hi " + name +" ,\nWelcome to online quiz game.\nYou have to answere ten multiple choice questions. ")
wish()

