#Importing the necessary Modules
from time import sleep
from os import system as device
import os

# The Activity Starts Here
sleep(4 - 3)
print "Hi! Let's Play Fill-Up Game:\n\n"
sleep(.3)
init = raw_input("Let's St").lower().strip()
score_0 = 0
if init == "art" :
    print "*Correct*"
elif init == "@999f":         # A Bonus Cheat Code! #    
    score_0 = 999
    print "\t Let's Begin !!! "
else :
    print "Wrong!!\t", "You must have typed 'art' to make it \"Let's Start\" "
raw_input(" ")
device('cls')
print "OK Then! Be Active Now!"

def Rules() :
    """Contains just the essential rules of the game."""
    print "Now you have to Answer 15 short Answers. You may type correct answer directly! Press Enter to confirm your Answer. \nRemember, you can't undo once your answer is confirmed! Type N if you wish to skip a question, or else it will be considered as wrong! \n"
    sleep(1.009)
    print "-->For every Right Answer, you'll be Awarded +10 Points!\n-->For every Wrong Answer, your 5 marks will be deducted! \n-->Skipped Questions would cause no change in marks.",
    sleep(2.1)
    print " \n\n            All The Best"
    sleep(.20)
Rules()

raw_input("[Press Enter to Begin]\n\n")
print "\n (Hint: Correct!)"
b = raw_input("Alr").lower().strip()
if b == "ight" :
    print "Correct!"
    score_1 = 10
elif b == "n" :
    print "Next!"
    score_1 = 0
else :
    print "Wrong!!"
    score_1 = -5
print "\n (Hint: Apologize)"
c = raw_input("So").lower().strip()
if c == "rry" :
    print "Correct!"
    score_2 = 10
elif c == "n" :
    print "Next!"
    score_2 = 0
else :
    print "Wrong!!"
    score_2 = -5
print "\n (Hint: Being Bigger)"
d = raw_input("Su").lower().strip()
if d == "perior" :
    print "Correct!"
    score_3 = 10
elif d == "per" :
    print "Correct!"
    score_3 = 10
elif d == "n" :
    print "Next!"
    score_3 = 0
else :
    print "Wrong!!"
    score_3 = -5
print "\n (Hint: The Blue Dye)"
e = raw_input("Wo").lower().strip()
if e == "ad" :
    print "Correct!"
    score_4 = 10
elif e == "n" :
    print "Next!"
    score_4 = 0
else :
    print "Wrong!!"
    score_4 = -5
print "\n (Hint: Cruel)"
f = raw_input("H").lower().strip()
if f == "arsh" :
    print "Correct!"
    score_5 = 10
elif f == "n" :
    print "Next!"
    score_5 = 0
else :
    print "Wrong!!"
    score_5 = -5
print "\n (Hint: Old and Indifferent)"
g = raw_input("Anti").lower().strip()
if g == "que" :
    print "Correct!"
    score_6 = 10
elif g == "n" :
    print "Next!"
    score_6 = 0
else :
    print "Wrong!!"
    score_6 = -5
if score_1+score_2+score_3+score_4+score_5+score_6 <= -30 :     #Checking whether all of the initial answers were wrong.
    handlift = raw_input('It seems like you\'re having a hard-time playing it, Literally! \n So, would you like to re-read the instructions? [yes/no] : ').upper()
    if handlift == 'YES' or handlift == 'Y':
        print "I Appericiate It! For this, you've been given +10 Points."
        sleep(.5)
        print "Please wait till the Rules Reload ... "
        sleep(.3)
        os.system('cls')
        Rules()
        score_1 += 10
    else :
        os.system('cls')
        pass
print "\n (Hint: Programming Language whose name resembles with a reptile family member)"
g = raw_input("Py").lower().strip()
if g == "thon" :
    print "Correct!"
    score_7 = 10
elif g == "n" :
    print "Next!"
    score_7 = 0
else :
    print "Wrong!!"
    score_7 = -5
print "\n (Hint: One who have no faith in deities(gods) )"
h = raw_input("Ath").lower().strip()
if h == "eist" :
    print "Correct!"
    score_8 = 10
elif h == "eists" :
    print "Correct!"
    score_8 = 10
elif h == "n" :
    print "Next!"
    score_8 = 0
else :
    print "Wrong!!"
    score_8 = -5
print "\n (Hint: To get in the way of(to hinder) )"
h = raw_input("Im").lower().strip()
if h == "pede" :
    print "Correct!"
    score_9 = 10
    cont1 = raw_input("What's the opposite of impede?\n").lower()
    if cont1 == "expede" :
        print " Well, That's Obsolete(No Longer in use)! ", " [Still, You'll Get +3 Points for this] "
        score_9 = score_9+3
    elif cont1 == "expedict" :
        print " That's Right! ", " [For this, You'll Get +4 Points] "
        score_9 = score_9+4
    elif cont1 == "assist" :
        print " That's Right! ", " [For this, You'll Get +4 Points] "
        score_9 = score_9+4
    elif cont1 == "help" :
        print " That's Right! ", " [For this, You'll Get +4 Points] "
        score_9 = score_9+4
    else :
        print " [It was 'Expedict', 'Assist', or 'Help'.] "
elif h == "n" :
    print "Next!"
    score_9 = 0
else :
    print "Wrong!!"
    score_9 = -5
print "\n (Hint: Something that's able to solve all the problems)"
h = raw_input("Pan").lower().strip()
if h == "acea" :
    print "Correct!"
    score_10 = 10
elif h == "n" :
    print "Next!"
    score_10 = 0
else :
    print "Wrong!!"
    score_10 = -5
print "\n (Hint: A feeling of contempt(inferior) or scorn)"
h = raw_input("Disdain").lower().strip()
if h == "" :
    print "Correct!"
    score_11 = 10
elif h == "n" :
    print "Skipping to Next!"
    score_11= 0
else :
    print "Wrong!!"
    score_11 = -5
print "\n (Hint: A layer within a body of water or air where the temperature changes rapidly with depth.)"
i = raw_input("Thermo").lower().strip()
if i == "cline" :
    print "Correct!"
    score_12 = 10
elif i == "cline layer" :
    print "Correct!"
    score_12 = 10
elif i == "cline " :
    print "Correct!"
    score_12 = 10
elif i == "n" :
    print "Next!"
    score_12= 0
else :
    print "Wrong!!"
    score_12 = -5
print "\n (Hint: The state of being notched minutely, like a fine saw. )"
h = raw_input("Serrulation").lower().strip()
if h == "" :
    print "Correct!"
    score_13 = 10
elif h == "n" :
    print "Moving on to Next One!"
    score_13= 0
else :
    print "Wrong!!"
    score_13 = -5
print "\n (Hint: Incapable of producing results; useless; not worth attemping.)"
print " (Hint2: Synonyms -- Vain, Idle, Incapable, Ineffectual, Unavailing, Fruitless\n         Antonyms -- Availing, Effectual, Effective)"
h = raw_input("Fut").lower().strip()
if h == "ile" :
    print "Correct!"
    score_14 = 10
elif h == "ile." :
    print "Correct!"
    score_14 = 10
elif h == "ile " :
    print "Correct!"
    score_14 = 10
elif h == "ile. " :
    print "Correct!"
    score_14 = 10
elif h == "n" :
    print "Next!"
    score_14 = 0
else :
    print "Wrong!!"
    score_14 = -5
print "\n (Hint:Tactile, Of or relating to the sense of touch, touching(reaching the heart) )"
print " (Hint2: Similar Meaning   -- Very Emotional talk, A feeling that makes us realsise something(realisation)\n         Opposite Meaning -- Cruel in a manner of having no emotions!)"
h = raw_input("Hap").lower().strip()
if h == "tic" :
    print "Correct!"
    score_15 = 10
elif h == "n" :
    print "Next!"
    score_15 = 0
else :
    print "Wrong!!"
    score_15 = -5
    query = raw_input("Would you like to see what it was?(It will Cost you 2 points)\n[Yes or No]").lower().strip()
    if query == "yes" or query == "y" or query == "yeah" :
        print "It was 'Haptic' ! "
        score_15 = score_15 -2
    elif query == "not now" or query == "no" or query == "n" :
        print "As You Wish!"
    elif query == "why":
        print "This is a word that we feel must be known to you"
        query = raw_input("So, would you like to see what it was?(It will Cost you 2 points)\n[Yes or No]").lower().strip()
        if query == "y" or query == "yes" or query == "yeah" :
            print "It was 'Haptic' ! "
            score_15 = score_15 -2
        elif query == "nope" or query == "no" or query == "n" :
            print "As You Wish!"
        else :
            print "Invalid Answer! Let's Move On!"

    else :
        print "Invalid Answer! Let's Move On!"

# Calculating the total score
net_score = score_0+score_1+score_2+score_3+score_4+score_5+score_6+score_7+score_8+score_9+score_10+score_11+score_12+score_13+score_14+score_15
print "\nYour Score Is:", net_score
sleep(43 - 41.3)        # Function Arguments accept Calculations, as given Here

# A chance to view all correct answers, a feature just for meritorious game players.
ask = 'no'
if net_score > 100 :
    ask = raw_input("   >>> Congratulations! You've scored above 100 points.<<<\n Would You like to see all the answers? (It will Cost you 100 Points). \n[Yes or No] : ").lower().strip()
    if ask in ('yes', 'y') :
        print "Alright! Your new score is :", net_score - 100, "\n"
        print "S. No.\tAsked\t\tAnswer\t\tSub-Question(If Any)\n1. \tAlr\t\tight\t\t\t-\n2.\tSo\t\trry\t\t\t-\n3.\tSu\t\tper/perior\t\t-\n4.\two\t\tad\t\t\t-\n5.\tH\t\tarsh\t\t\t-\n6.\tAnti\t\tque\t\t\t-\n7.\tPy\t\tthon\t\t\t-\n8.\tAth\t\teist\t\t\t-\n9.\tIm\t\tpede\t\t\tExpede\n10.\tPan\t\tacea\t\t\t-\n11.\tDisdain\t\t-\t\t\t-\n12.\tThermo\t\tcline/cline layer\t-\n13.\tSerrulation\t-\t\t\t-\n14.\tFut\t\tile\t\t\t-\n15.\tHap\t\ttic\t\t\t-\n"
        sleep(1.0 - 0.51)
    elif ask in ("n", "nope", "no") :
        print "As You Wish!"
    else :
        print "Please learn to write valid Answers for any Question asked!\n Anyways,"

print "\n ---Thanks for Playing! Please Visit Again---"
sleep(.59)

# One last step "Press ENTER to EXIT"  #Could be made Optional with >> if ask == 'yes':
raw_input('  [Press Enter to Exit]')
exit()
