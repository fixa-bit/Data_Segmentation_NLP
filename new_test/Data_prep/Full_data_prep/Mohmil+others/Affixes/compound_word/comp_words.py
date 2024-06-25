input_file='./Input/affix_output.txt'
list_file='./Input/compound_words.txt'
def find_comp_words(wordsx,comp_words_list):#finds whether its word 1/2
  ii=0
  sub1x=[]
  wordindex=[]
  for word in wordsx:
    for items in list_sufpre:
      if word==items:
        if suf==True:
          word_index=[ii-1]
        else:
          word_index=[ii]
        wordindex.append(word_index)
    ii=ii+1
  return wordindex
def comp_words_list():
	temp = open(list_file,'r').read().split('\n')
	i=0
	temp = list(filter(None, temp))#removes any empty lst 
	for line in temp:
		if i==0:
		  compound_words=[line.split('_')]
		else:
		  compound_words.append(line.split('_'))

		i=i+1
	comp_dict=compound_words
	return comp_dict

def comp_words_list_join(rep):
	temp = open(list_file,'r').read().split('\n')
	i=0
	temp = list(filter(None, temp))#removes any empty lst 
	for line in temp:
		char_len=line.split("_")
		#filter empty elements
		char_len = list(filter(None, char_len))
		char_lenx=len(char_len)
		if char_lenx==2:
			if i==0:
			  compound_words=[line.replace('_',rep)]
			else:
			  compound_words.append([line.replace('_',rep)])

			i=i+1
	comp_dict2=compound_words
	return comp_dict2

def filter_list(comp_words_list):
    i=0
    for items in comp_words_list:
      item2 = list(filter(None, items))#to remove any empty element in list of strings
      item = list(filter(lambda name: name.strip(), item2))  #removes any space in list
      
      if(len(item)>1):
          if i==0:
              compound_words=[item]
          else:
              compound_words.append(item)

          i=i+1
    return compound_words
      
def match_comp_word(word_comp,comp_words_list,index_comp,three_word_length):
   #print('kk',word_comp)
   if word_comp in comp_words_list:
      if three_word_length==True:
        print('Word from dictionary',word_comp,' at index', index_comp-1," and  ", index_comp)
        compound_word_index.append(index_comp-1)
        compound_word_index.append(index_comp)
      else:        
        print('Word from dictionary',word_comp,' at index', index_comp)
        compound_word_index.append(index_comp)

      return compound_word_index
      
def match_comp_joinerword(line,word_comp,comp_words_list,index_comp):
   #for line in temp:
     if word_comp in comp_words_list:      
       dict_joiner_index = comp_words_list.index(word_comp)
       print(dict_joiner_index)
       print("joiner word from dict",comp_parallel_list[dict_joiner_index])
       dict_word.append(comp_parallel_list[dict_joiner_index])
       comp_parallel_list_index.append(dict_joiner_index)
       print('Word from joiner dictionary',word_comp,' at index', index_comp)
       word_compf.append(word_comp)
       compound_joinerword_index.append(index_comp)
     return compound_joinerword_index,comp_parallel_list_index,word_compf,dict_word

def nth_repl(s, sub, repl, n):
    #print('s',s)
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

def space_to_sub(index_sub,temp):
	temp = open(input_file,'r').read()
	with open('./Output/com_word_output.txt', 'w') as f:#its output file
	  	i=0
	  	print(index_sub)
	  	for x in range(0,len(index_sub)):
	  	    sub=" "
	  	    my_index=(index_sub[x])+1-x
	  	    
	  	    print("within fn",my_index,index_sub[x])
	  	    temp=nth_repl(temp, ' ', u'u200C', my_index)
	  	    i=i+1
	  	f.write(temp)
	  	f.write('\n')

	  	

        
#main      

comp_words_list=comp_words_list()
comp_words_list2=comp_words_list_join('')
comp_parallel_list=comp_words_list_join('_')

global comp_word_length
global compound_word_index
global compound_joinerword_index
comp_parallel_list_index=[]
compound_word_index=[]
compound_joinerword_index=[]
word_compf=[]
dict_word=[]
comp_words_mod=filter_list(comp_words_list)
temp = open(input_file,'r').read().split('\n')
i=0
index_sub=[]
temp = list(filter(None, temp))#to remove any empty list of strings
#for replacing word with subspace
index=0
for line in temp:
  word_lx=line.split(' ')
  if i==0: 
    word_l=[word_lx]
  else:
    word_l.append(word_lx)
  i=i+1
for xxx in range(0,len(word_l)):
    for iterx in range(0,len(word_l[xxx])):
      if iterx > 0:
        comp_word_check=[word_l[xxx][iterx-1]]+[word_l[xxx][iterx]]
        if iterx>1:
                  comp_word_check2=[word_l[xxx][iterx-2]]+[word_l[xxx][iterx-1]]+[word_l[xxx][iterx]]
                  #if match_comp_word(comp_word_check2,comp_words_list,index,True)!=None:
                  index_sub=match_comp_word(comp_word_check2,comp_words_list,index,True)
        #if match_comp_word(comp_word_check,comp_words_list,index,False)!=None:
        index_sub=match_comp_word(comp_word_check,comp_words_list,index,False)
        
        index=index+1
#print('index_subf',index_sub)

space_to_sub(index_sub,temp)




temp = open('./Output/com_word_output.txt','r').read().split('\n')
i=0
index_sub=[]
#print('word_l',temp)
temp = list(filter(None, temp))#to remove any empty list of strings
#for replacing word with subspace
for line in temp:
  index=0
  word_lx=line.split(' ')
  if i==0: 
    word_l=[word_lx]
  else:
    word_l.append(word_lx)
  i=i+1

for xxx in range(0,len(word_l)):#for each line
    for iterx in range(0,len(word_l[xxx])):#for each word in line
      comp_joinword_check=[word_l[xxx][iterx]]
      
      joinerword_index,parallel_list_index,word_compf,dict_word=match_comp_joinerword(line,comp_joinword_check,comp_words_list2,index)
      index=index+1
print("joinerword_index",joinerword_index)
print("parallel_list_index",parallel_list_index)
temp = open('./Output/com_word_output.txt','r').read()
with open('./Output/com_word_output_tmp.txt', 'w') as f:#its output file
	for joinwords in range(0,len(joinerword_index)):
		temp=temp.replace(word_compf[joinwords][0], dict_word[joinwords][0])
		#print(temp)
	f.write(temp)
with open('./Output/com_word_output2.txt', 'w') as f:#its output file
	for joinwords in range(0,len(joinerword_index)):
		temp=temp.replace('_',u'u200C')
		#print(temp)
	f.write(temp)

        



