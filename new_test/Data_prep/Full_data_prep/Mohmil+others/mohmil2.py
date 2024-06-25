from nltk.metrics.distance import edit_distance
Input_file='Data.txt'
Output_dir='./Affixes/readme_tmp.txt'
def find_simword(wordsx): # finds words that differs by one character 
  ii=-1
  sub1x=[]
  wordindex=[]
  for word in wordsx:
    #print(ii)
    ii=ii+1
    if ii>0:
      diff=edit_distance(wordsx[ii], wordsx[ii-1])
      #block that covers 3 cases of  replacing first 2 characters with م ، گ ، ب
      if diff==2 and len(wordsx[ii])==(len(wordsx[ii-1] )-1) and len(wordsx[ii])>2:
        #print("pochkuch",wordsx[ii-1],wordsx[ii] )
        a = list(wordsx[ii])
        b = list(wordsx[ii-1])
        compare_string_a=a[-(len(a)-1):]
        compare_string_b=b[-(len(a)-1):]
        if compare_string_a==compare_string_b and wordsx[ii][0]!=wordsx[ii-1][0]:
          if (wordsx[ii][0])=='گ'  :
            print('First two character replaces with گ ')         
            word_index=[ii-1]
            wordindex.append(word_index)  
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (wordsx[ii][0])=='ب'  :
            print('First character replaces with ب ')
            word_index=[ii-1]
            wordindex.append(word_index)  
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (wordsx[ii][0])=='م'  :
            print('First character replaces with م')
            word_index=[ii-1]
            wordindex.append(word_index)  
            print((wordsx[ii-1] ) ,(wordsx[ii]))
       

      #block that covers cases of  replacing first character with د، و، م، س،پ، ب ، ج
      if diff==1 and len(wordsx[ii])==len(wordsx[ii-1] ) and len(wordsx[ii])>2:
        a = list(wordsx[ii])
        b = list(wordsx[ii-1] ) 
        #case 11 and 12
        last_char_index=len(a)-1
        
        if a[last_char_index]!=b[last_char_index]:  #if second character is replaced as in 1st seven cases
          #Second characters ا replace with و          
          if b[last_char_index]=='م':
            print('last character replaced with م')
            word_index=[ii-1]
            wordindex.append(word_index) 
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          #Second characters ا replace with و          
          if a[last_char_index]=='ا'  and b[last_char_index]!='م':
            print('last character replaced with ا')
            word_index=[ii-1]
            wordindex.append(word_index) 
            print((wordsx[ii-1] ) ,(wordsx[ii]))
        
        #case 11 and 12
        if a[1]!=b[1]:  #if second character is replaced as in 1st seven cases
          #Second characters ا replace with و          
          if a[1]=='ا' and b[1]=='و':
            print('Second characters و replace with ا ')
            word_index=[ii-1]
            wordindex.append(word_index)   
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          #Second characters ا replace with و          
          if a[1]=='و' and b[1]=='ا':
            print('Second characters ا replace with و  ')
            word_index=[ii-1]
            wordindex.append(word_index) 
            print((wordsx[ii-1] ) ,(wordsx[ii]))
        if a[0]!=b[0]:  #if first character is replaced as in 1st seven cases        
          if (a[0])=='و'  :
            print('First character replaces with و  ')
            word_index=[ii-1]
            wordindex.append(word_index)         
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (a[0])=='د'  :
            print('First character replaces with د ')
            word_index=[ii-1]
            wordindex.append(word_index)         
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (a[0])=='م'  :
            print('First character replaces with م ')
            word_index=[ii-1]
            wordindex.append(word_index)         
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (a[0])=='س'  :
            print('First character replaces with س')    
            word_index=[ii-1]
            wordindex.append(word_index)          
            print((wordsx[ii-1] ) ,(wordsx[ii])) 
          if (a[0])=='پ'  :
            print('First character replaces with پ ')
            word_index=[ii-1]
            wordindex.append(word_index)     
            print((wordsx[ii-1] ) ,(wordsx[ii]))    
          if (a[0])=='ب'  :
            print('First character replaces with ب ')
            word_index=[ii-1]
            wordindex.append(word_index)         
            print((wordsx[ii-1] ) ,(wordsx[ii]))
          if (a[0])=='ج'  :
            print('First character replaces with ج ')      
            word_index=[ii-1]
            wordindex.append(word_index)  
            print((wordsx[ii-1] ) ,(wordsx[ii]))        

  return wordindex
def indexes(lst, element): # finds indexes of any particulat character(element) in list(lst)
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
def indexes_zair(lst,find_char):# finds indexes of zair
  result=[]
  i=0
  indexes_zair=[]
  for items in lst:
    if find_char in items[-1:]:
      print('Subspace after ',find_char)
      print(items)     

      indexes_zair.append(i)
    i=i+1

  return indexes_zair
def find_w(wordsx):   #calls indexes method to calculate 'و'


	idxs = indexes(wordsx, "و")

	return idxs
def find_zair(wordsx,find_char): #calls indexes method to calculate' ِ'
	idxs = indexes_zair(wordsx,find_char)

	return idxs

def nth_repl(s, sub, repl, n):  #replace particular strings'sub' by 'repl' in source stream 's'
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

def space_to_sub(index_sub,temp): # calls nth_repl to create new string and writes it in file
	with open(Output_dir, 'w') as f:
		i=0

		for line in temp:
	  		word_lx=line.split(' ')
	  		index=index_sub[i]

	  		for x in range(0,len(index)):

	  			iterx=int(index[x][0])+1-x
	  			#so to add decrement as space is replaced by sub in prev string so its occurence move one step back
	  			sub=" "

	  			line=nth_repl(line, sub, u'u200C', iterx)
	  		
	  		i=i+1
	  		f.write(line)
	  		f.write('\n')
		
temp = open(Input_file,'r').read().split('\n')

i=0
index_sub=[]
temp = list(filter(None, temp))#to remove any empty list of strings
#obtaining list of all indexes for wow,zair and  mohmil
for line in temp:
  word_lx=line.split(' ')
  if i==0: 
    l=[line]
    word_l=[word_lx]
    index_sub=[find_simword(word_l[i])]
    index_w=list(find_w(word_lx))
    if len(index_w):
    	for items in index_w:
    		index_sub[0].append([items-1])
    		index_sub[0].append([items])
    		
    index_zair=list(find_zair(word_lx,'ِ'))
    if len(index_zair):
    	for items in index_zair:
    		index_sub[0].append([items])
    index_hamza=list(find_zair(word_lx,'ء'))
    if len(index_hamza):
    	for items in index_hamza:
    		index_sub[0].append([items])
  else:
    l.append(line)
    word_l.append(word_lx)
    index_sub.append(find_simword(word_l[i]))
    
    
    index_w=list(find_w(word_lx))
    if len(index_w):
    	for items in index_w:
    		index_sub[i].append([items-1])
    		index_sub[i].append([items])

    index_zair=list(find_zair(word_lx,'ِ'))
    if len(index_zair):
    	for items in index_zair:
    		index_sub[i].append([items])
    index_hamza=list(find_zair(word_lx,'ء'))
    if len(index_hamza):
    	for items in index_hamza:
    		index_sub[i].append([items])

  i=i+1
#sorting all indexes to arrange them in ascending order to make space to sub function work
index_sort=[]
for items in index_sub:
  items.sort()
  index_sort.append(items)
space_to_sub(index_sort,temp)














	

