from GetData import *

def offByK(s1,s2,k):

	""" Two non-empty strings s1 and s2 are said to be off-by-k if they have the same length and differ
in exactly k positions."""
	count = 0
	i = 0
	j = 0
	while i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			count = count + 1
		i = i + 1
		j = j + 1


	if count == k:
		return True
	else:
		return False






def offBySwaps(s1,s2):

	""" Two non-empty strings s1 and s2 are said to be off-by-swaps if s1 and s2 may be different but
of same length, but s2 can be obtained by arranging/swapping characters in s1, any number of
times."""
	length1 = len(s1)
	length2 = len(s2)
	if length1 == length2:
		for ch1 in s1:
			for ch2 in s2:
				if ch1 == ch2:
					return True
	else:
		return False






def offByKExtra(s1,s2,k):
    """Two non-empty strings s1 and s2 are off-by-k-extra if removing exactly k characters from s1
    gives s2 or if removing k characters from s2 gives s1 """
    s1=s1.lower()
    s2=s2.lower()
    count=0
    if len(s1)>len(s2):
        for i in s2:
            if s2.count(i)<=s1.count(i) and len(s1)-len(s2)==k:
                count+=1
            elif s2.count(i)>s1.count(i) or len(s1)-len(s2)!=k:
                break
        if count==len(s2):
            return True
        else:
            return False
                
    elif len(s1)<len(s2):
        for i in s1:
            if s1.count(i)<=s2.count(i) and len(s2)-len(s1)==k:
                count+=1
            elif s1.count(i)>s2.count(i) or len(s2)-len(s1)!=k:
                break
        if count==len(s1):
            return True
        else:
            return False

    elif len(s1)==len(s2):
        if k==0:
            return True
        else:
            return False
            



	



def ListOfNearString(s,L,k):
	""" Returns a list of all entries in L that are near to s for a given value of k.
PreC: s is a nonempty string, k is a non-negative integral value and L is a list of
nonempty strings. """
	
	length = len(L)
	list = []
	for i in range(length):
		
		if s != L[i]:
			if offByK(s,L[i],k) == True or offBySwaps(s,L[i]) == True or offByKExtra(s,L[i],k) == True:
				list.append(L[i])
		
	return list 


new_list = fileToStringList("EnglishWords.txt")

len_list = len(new_list)

blank_list = []
for i in range(len_list):
	blank_list.append(stringToWordList(new_list[i]))

print(ListOfNearString("abduct",new_list[1:100],2))#['aah', 'aahing', 'aahs', 'aardvark', 'aardwolf', 'abacus', 'abacuses', 'abalones', 'abandons', 'abased', 'abasedly', 'abaser', 'abases', 'abashing', 'abatable', 'abated', 'abater', 'abates', 'abatis', 'abatises', 'abator', 'abattoir', 'abbacies', 'abbacy', 'abbatial', 'abbe', 'abbess', 'abbesses', 'abbeys', 'abbots', 'abbott', 'abbr', 'abbrev', 'abdicable', 'abdicate', 'abdicated', 'abdicates', 'abdicating', 'abdication', 'abdications', 'abdicator', 'abdomens', 'abducted', 'abductor'])



def compare_distr(L1,L2,bi):
    """ L1 and L2 represent two lists, of same size, and containing integers. The function
        checks if the frequency distributions of the two lists are same or not, for a given bin
        width(class interval).
        Return True if the distributions are same, False, otherwise"""

    L3=[]
    freq1=[]
    L1.sort()
    c=0
    for i in range(min(L1),max(L1)+bi+1,bi):
        L3.append(i)
        freq1.append(0)
    for i in L1:
        for j in range(len(L3)):
            try :
                if L3[j]<=i<L3[j+1]:
                    freq1[j]+=1
            except IndexError:
                pass
    freq1.pop()

    L5=[]
    freq2=[]
    L2.sort()
    c=0
    for i in range(min(L2),max(L2)+bi+1,bi):
        L5.append(i)
        freq2.append(0)
    for i in L2:
        for j in range(len(L5)):
            try :
                if L5[j]<=i<L5[j+1]:
                    freq2[j]+=1
            except IndexError:
                pass
    freq2.pop()

    if freq1==freq2:
        return True
    else:
        return False


 








	





		


