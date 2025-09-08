#---------------Q1---------------
''' 

dis = {
       "Hi" : "Thank You for connecting",
       "Good Moring" : "Good Moring /n How Can i help You",
       "Namste":"Hello",
       "Jaoo" : " Go",

}

words = input("Enter the words : ")
if words in dis:print(dis[words])
else: print("Sorry I don't understand")


#---------------Q2---------------

s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))
s = set()
n = input("Enter Your numbers :")
s.add(int(n))

print(s)

#---------------Q3---------------

s=set()
s.add(20)
s.add("20")
print(s)

#---------------Q4---------------

s = set()
s.add(20)
s.add(20.0)   
s.add("20")
print(len(s))



#---------------Q5---------------

s = {}
print(type(s))

'''



#---------------Q6---------------

dis = {
    
}

frind = input("Enter the Name of friends : ")
lang= input("Enter the Name of Language : ")
dis.update({frind:lang})


frind = input("Enter the Name of friends : ")
lang= input("Enter the Name of Language : ")
dis.update({frind:lang})


frind = input("Enter the Name of friends : ")
lang= input("Enter the Name of Language : ")
dis.update({frind:lang})


frind = input("Enter the Name of friends : ")
lang= input("Enter the Name of Language : ")
dis.update({frind:lang})


frind = input("Enter the Name of friends : ")
lang= input("Enter the Name of Language : ")
dis.update({frind:lang})

print(dis)
