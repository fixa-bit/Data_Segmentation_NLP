#from sub_urdu.py import space_to_sub
List_dir='suffix_prefix.txt'
Input_dir='readme_tmp.txt'
Output_dir='./compound_word/Input/affix_output.txt'
def space_to_sub(index_sub,temp):
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
def nth_repl(s, sub, repl, n):
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
def suffix_prefix_list():
	temp = open(List_dir,'r').read().split('\n')
	i=0
	temp = list(filter(None, temp))#removes any empty lst 
	for line in temp:
		if i==0:
			prefix_list=line.split('،')
		else:
			suffix_list=line.split('،')
		i=i+1
	return prefix_list,suffix_list

def find_presuf(wordsx,list_sufpre,suf):
  ii=0
  sub1x=[]
  wordindex=[]
  for word in wordsx:
    for items in list_sufpre:
      if word==items and len(word)>0:
        if suf==True:
          print("Suffix: ",word)
          word_index=[ii-1]
        else:
          print("Prefix: ",word)
          word_index=[ii]
        wordindex.append(word_index)
    ii=ii+1
  return wordindex
prefix_list,suffix_list=suffix_prefix_list()
temp = open(Input_dir,'r').read().split('\n')
i=0
index_pre=[]
index_suf=[]
temp = list(filter(None, temp))#to remove any empty list of strings
for line in temp:
  word_lx=line.split(' ')
  if i==0: 
    word_l=[word_lx]
    index_pre=[find_presuf(word_l[0],prefix_list,False)]
    index_suf=[find_presuf(word_l[0],suffix_list,True)]

  else:
    word_l.append(word_lx)
    index_pre.append(find_presuf(word_l[i],prefix_list,False))
    index_suf.append(find_presuf(word_l[i],suffix_list,True))
  i=i+1
print('Index_pre',(index_pre))

print('Index_suf',(index_suf))

for iterx in range(0,len(index_suf)):
	if iterx==0:
		full_pre_suf=[index_pre[0]+index_suf[0]]
	else:
		pre_suf=index_pre[iterx]+index_suf[iterx]
		full_pre_suf.append(pre_suf)
print('full_pre_suf',full_pre_suf)

index_sort=[]
for items in full_pre_suf:
  items.sort()
  index_sort.append(items)
print('Sorted prefix list=',index_sort)
space_to_sub(index_sort,temp)

