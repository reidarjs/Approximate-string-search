def add(a,b):    #I needed to create a custom add-function to prevent the carry-bit from expanding the length of D0
    c=a+b
    if c>=2**len(pattern):
        c=c-2**len(pattern)
    return c



print("The search pattern and search text can only contain characters from the following set:")
print(" a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9")

pattern=input("Enter search pattern: ").lower()
text=input("Enter search text: ").lower()
k=int(input("Enter k-value (maximum number of allowed errors): "))

charset="abcdefghijklmnopqrstuvwxyz0123456789 "



PM={}

#Pre-processing
for a in charset:
    PM[a]=0

for i in range(1,len(pattern)+1):
    PM[pattern[i-1]]=PM[pattern[i-1]] | int(("0"*(len(pattern)-i))+"1"+("0"*(i-1)),2)
    

VP=int("1"*len(pattern),2)
VN=0

Dmj=len(pattern)


#Searching
for j in range(0,len(text)):
    
    D0=(((add((PM[text[j]] & VP),VP))^VP) | PM[text[j]] | VN)
    
    HP=(VN | (~(D0 | VP)))& 2**(len(pattern))-1 #I needed to AND with ones due Python's handling of bit-negations
    HN=D0 & VP
    

    if HP & int("1"+"0"*(len(pattern)-1),2) != 0:
        Dmj=Dmj+1
    if HN & int("1"+"0"*(len(pattern)-1),2) != 0:
        Dmj=Dmj-1
    if Dmj<=k:
        print("Match found at ending position ",text[j],"[",j+1,"]")

    
    hn=HN << 1
    hp=HP << 1
    
    #These if-statements are needed to prevent left-shift from expanding the size of HN and HP
    if hn>=2**len(pattern):
        hn=hn-2**len(pattern)
    if hp>=2**len(pattern):
        hp=hp-2**len(pattern)
        
        
    VP=(hn | ~(D0 | hp))& 2**(len(pattern))-1 #I needed to AND with ones due Python's handling of bit-negations
    

    VN=D0 & hp
    



