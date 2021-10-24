# our gramme is the following 
# S> NP VP
# NP> DET NOUN | NOUN
# VP> VERB | VERB PREPOSITION NP |VERB NP
#So acording to this grammer we will get patterns in the following code

#we are going to use the medical domain in this project 
#message to let the user aware of the grammer


print(f"Hello to our NLP programme our grammer is\n\
          \n         S > NP VP\n\
         NP > DET NOUN | NOUN\n\
         VP > VERB | VERB PREPOSITION NOUN |VERB NP\n\n\
         So becarfull to your words\n")
    
sentence =input("enter your sentance : \n")

#detremines able to use
det=['a','an','the'] 
#---------------------------------
 #nouns able to use
nouns=['doctor','nurse','hospital','manger','operator','accident', 'allergy', 'ambulance', 'biopsy', 'consent', 'course', 'examination', 'excess',
'exercise' ,'injection', 'intake', 'overdose', 'paroxysm', 'progress', 'rash', 'recurrence',
'surgery', 'tendency', 'treatment', 'vaccination','clinc']
#------------------------------------------
#verba able to use
verbs =['helps','exmaines','gives','is',
'Cough','Cure','Deliver','Deteriorate','Diagnose','Die','Discard',
'Discharge','Ease','Examine','Explore','Faint','Fracture','Harm',
'Heal','Infect','Inflame','Inject','Irritate','Itch','Numb','Operate',
'Perform','Prescribe','Present','Probe','Radiate','Reassure','Recover',
'Refer','Relieve','Replace','Respond','Shiver','Sneeze','Soothe','Specialise',
'Sprain','Sterilise','Suffer'] 
#-----------------------------------------
 #preposition able to use
preposition=['with','in','on',
'above', 'across', 'against', 'along', 'among',
'around', 'at', 'before', 'behind', 'below', 'beneath',
'beside', 'between', 'by']
#------------------------------------------

# this is a function will make all of work easier by resizes the lists
def resizelists(det,nouns,verbs,preposition):
    m=max(len(det),len(nouns),len(verbs),len(preposition))
    for x in range(len(det),m):
        det.append(" ")
    for x in range(len(nouns),m):
        nouns.append(" ")
    for x in range(len(verbs),m):
        verbs.append(" ")
    for x in range(len(preposition),m):
        preposition.append(" ")

resizelists(det,nouns,verbs,preposition)
# end of the function 

result=[]
result2=[]
 #the input sentence
sentence_a=sentence.split(" ") #to split each word and put it into array
# x=True 
y1=len(sentence_a) # range will used in for loop
y2=len(nouns)     # range will used in for loop

# here we chek if the words are into our split array is in domain of words 
# and make an array save types of words to chek after the grammer
for x in range(0,y1):
    for y in range(0,y2):
        if sentence_a[x] == nouns[y]:
            result.append(nouns[y])
            result2.append("noun")
        elif sentence_a[x] == det[y]:
            result.append(det[y])
            result2.append("det")
        elif sentence_a[x] == verbs[y]:
            result.append(verbs[y])
            result2.append("verb")
        elif sentence_a[x] == preposition[y]:
            result.append(preposition[y])
            result2.append("preposition")
# for x in range(0,len(det)):
#     if sentence_a[x] == det[y]:
#             result.append(det[y])
#             result2.append("det")
        
# here is the pattern we will chek at
#we get this patterns from our Grammer
#and it's all posible sentence would come from the grammer

flag=False # flag to if 

pattern=["det","noun","verb","preposition","det","noun"]
pattern2=["det","noun","verb"]
pattern3=["det","noun","verb","preposition","noun"]
pattern4=["noun","verb","preposition","noun"]
pattern5=["noun","verb"]
pattern6=["noun","verb","preposition","det","noun"]
pattern7=["det","noun","verb","det","noun"]
pattern8=["det","noun","verb","noun"]
pattern9=["noun","verb","det","noun"]
pattern10=["noun","verb","noun"]

#to chek the sentance meets our pattern or not and change the flag 
if result2==pattern or result2==pattern2 or result2==pattern3 or result2==pattern4 or  result2==pattern5 or  result2==pattern6 or result2==pattern7 or result2==pattern8 or result2==pattern9 or result2==pattern10:
    flag=True
else:
    flag=False


if flag:
    print(f"sentnece is : {result}")
    print(f"result   is : {result2}")
    print("the sentence is accpeted due to the grammer")
elif not flag:
    print(f"sentnece is : {result}")
    print(f"result   is : {result2}")
    print("the sentence does not accepted due to the grammer")
