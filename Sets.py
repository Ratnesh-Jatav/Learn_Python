'''
# ---------------- Dictionary -----------------
dis = {
    "Name": "Ratnesh Jatav",
    "Age": 20,
    "City": "Ghaziabad",
    "Qualification": "MCA",
    "College": "AKTU"
}

print( type(dis))

print(dis["Name"])

#  ------------------- Set ------------------

s = {1, 2, 3, 4, 5}
print(type(s))
s.add(6)
s.remove(3)
print(s)
print(len(s))

# -------------union------------------
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)


# intersection
s1 = {1, 2, 3, 8}
s2 = {3, 4, 5, 8}
s4 = s1.intersection(s2)  
print(s4)    
'''