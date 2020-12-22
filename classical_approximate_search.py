

pattern=input("Enter search pattern: ").lower()
text=input("Enter search text: ").lower()
k=int(input("Enter k-value (maximum number of allowed errors): "))
store_matrix=input("Store the entire DP-matrix in memory? (yes or no) ")



result_indices=[]

if store_matrix=="no":
    c=[*range(0,len(pattern)+1)]
    c_=[*range(0,len(pattern)+1)]


    for j in range(1,len(text)+1):
        c=c_.copy()
        for i in range(1,len(pattern)+1):
            if text[j-1]==pattern[i-1]:
                c_[i]=c[i-1]
            else:
                c_[i]=1+min(c[i-1],c_[i-1],c[i])
        if c_[-1]<=k:
            result_indices.append([j,c_[-1]])
        
    if len(result_indices)>=1:
        print("The pattern '"+pattern+"' was found in search text '"+text+"' at the following locations:")
    else:
        print("No matches with fewer than",k,"errors were found")

    for i in range(0,len(result_indices)):
        print("At index",result_indices[i][0],"with",result_indices[i][1],"errors")



elif store_matrix=="yes":
    dp_matrix=[]
    for i in range(0,len(pattern)+1):
        dp_matrix.append([int(i)]*int(len(text)+1))    


    for i in range(1,len(pattern)+1):
        for j in range(1,len(text)+1):
            if text[j-1]==pattern[i-1]:
                dp_matrix[i][j]=dp_matrix[i-1][j-1]
            else:
                dp_matrix[i][j]=1+min(dp_matrix[i-1][j-1],dp_matrix[i-1][j],dp_matrix[i][j-1])

            if i==len(pattern) and dp_matrix[i][j]<=k:
                result_indices.append([j,dp_matrix[i][j]])

    if len(result_indices)>=1:
        print("The pattern '"+pattern+"' was found in search text '"+text+"' at the following locations:")
    else:
        print("No matches with fewer than",k,"errors were found")

    for i in range(0,len(result_indices)):
        print("At index",result_indices[i][0],"with",result_indices[i][1],"errors")
        
    
    

    print("\nThe complete DP-matrix:")
    t=list(text)
    print('   - ','  '.join(t))
    for i in range(0,len(pattern)+1):
        if i>=1 and i<len(pattern)+1:
            print(pattern[i-1],dp_matrix[i])
        else:
            print('-',dp_matrix[i])


