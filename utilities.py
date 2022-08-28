import string
global CHAR_LOOKUP
CHAR_LOOKUP = list(string.digits + string.ascii_uppercase)


def convert(number, frombase, tobase):  # function to convert any base
    """
    How to use:
    convert(<number or character to convert>, <input base: 10>, <output base:2)
    => Example: convert(12,10,2) -> Output: 1100.
    => Example: convert(A,16,10) -> Output: 10.
    """

    global CHAR_LOOKUP
    try:
        fromdigits = CHAR_LOOKUP[:int(frombase)]
        todigits = CHAR_LOOKUP[:int(tobase)]

        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1

        else:
            neg = 0

        # make a string of the integer (ex: A=10)
        x = 0
        for digit in str(number):
            try:
                x = x * len(fromdigits) + fromdigits.index(digit)
            except ValueError:
                os.system('cls')
                print(f"\"{digit}\" is not in the selected input base")

        # create the result in the base 'len(todigits)'
        if x < 1:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res

                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res
    except:
        return " Kí tự nhập không thuộc kiểu cơ số đã chọn !"


def select_base(text):
    if text == "Binary":
        return 2
    elif text == "Decimal":
        return 10
    elif text == "Octal":
        return 8
    elif text == "Hexadec":
        return 16


def select_var_num(text):
    if text == "2 Biến":
        return 2
    elif text == "3 Biến":
        return 3
    elif text == "4 Biến":
        return 4


def ascii_decode(string):
    byte_array = string.encode()

    # Converting the byte_array into a binary
    # integer
    binary_int = int.from_bytes(byte_array, "big")

    # Converting binary_int to a string of
    # binary characters
    binary_string = bin(binary_int)
    return binary_string[2:]

def minFunc(numVar, stringIn):
	num= int(numVar)
	x= stringIn
	"""
    This python function takes function of maximum of 4 variables
    as input and gives the corresponding minimized function(s)
    as the output (minimized using the K-Map methodology),
    considering the case of Don’t Care conditions.
	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.
	"""
	l= []
	i=0
	while(x[i]!='d'):
		if(x[i].isdigit()==True):                         # taking the values from the input, and storing it in a list
			if(x[i+1].isdigit()==False):
				l.append(x[i])
				i+=1
			else:
				l.append(x[i]+x[i+1])
				i+=2
		else:
			i+=1
		y=i
	ess=list(l)                                             #storing essential prime implicant in a seprate list for further use
	if(x[y+1]!='-'):
		while(x[y]!=')'):
			if(x[y].isdigit()==True):
				if(x[y+1].isdigit()==False):                #storing the dont care condition giving in the input
					l.append(x[y])
					y+=1
				else:
					l.append(x[y]+x[y+1])
					y+=2
			else:
				y+=1
	if(num==4):
		for i in range(len(l)):								#converting to binary for 4 variables
			l[i] = format(int(l[i]), '04b')
	elif(num==3):
		for i in range(len(l)):								#converting to binary for 3 variables
			l[i] = format(int(l[i]), '03b')
	elif(num==2):
		for i in range(len(l)):								#converting to binary for 2 variables
			l[i] = format(int(l[i]), '02b')

	a,b,c,d,e,f,g,h,p,q,w,r,t,y,m,n,o,z,u,v = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]  	#creating list to be stored
	l.sort()
	count = 0
	t=0

	#  Quine-McCluskey and Petrick methods -

	for i in range(len(l)):
			for j in range(num):				#Storing the digit speratly on the basis of much many 1's they contain
				if(l[i][j]=='1'):
					count+=1
			if(count==0):
				a.append(l[i])
			if(count==1):						#appending into one of the list created above for seperation
				b.append(l[i])
			if(count==2):
				c.append(l[i])
			if(count==3):
				d.append(l[i])
			if(count==4):
				e.append(l[i])
			count=0

	def step1(a,b,f):  									# Proceding tp step 1 comparing a and b then follows on uptil all thrr couples are compared
		count=0
		for i in range(len(a)):
			for k in range(len(b)): 					#loops
				for j in range(num):
					if(a[i][j]!=b[k][j]):
						count+=1
				if(count==1):
					for j in range(num):
						if(a[i][j]!=b[k][j]):
							f.append(str(str(a[i][:j])+'x'+str(a[i][j+1:])+',('+str(int(a[i],2))+','+str(int(b[k],2))+')')) 	#slicing and appending
				count=0
		return(f)

	f=step1(a,b,f)					#calling the function and storing what it returns
	g=step1(b,c,g)
	h=step1(c,d,h)
	p=step1(d,e,p)

	def step2(f,g,q):
		count=0
		for i in range(len(f)): 		#same as step 1 , step 2 does the same on the output of step 1 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]!=g[k][j]):			#loops
						count+=1
				if(count==1):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							q.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+','+ str(g[k][num+2:])))   #slicing and appending
				count=0
		return(q)

	q = step2(f,g,q)                  #calling the function and storing what it returns
	w = step2(g,h,w)
	r = step2(h,p,r)

	def step3(f,g,q):
		count=0
		for i in range(len(f)):			#same as step 2 , step 3 does the same on the output of step 2 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]!=g[k][j]):
						count+=1				#loops
				if(count==1):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							q.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+ ',' +str(g[k][6:]))) 				#slicing and appending
				count=0
		return(q)
	m = step3(q,w,m)			#calling the function and storing what it returns
	n = step3(w,r,n)

	def step4(f,g,p):
		count=0
		for i in range(len(f)):				#same as step 3 , step 4 does the same on the output of step 3 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]=='x'):			#loops
						if(g[k][j]=='x'):
							count+=1
				if(count==2):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							p.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+ str(g[k][-4:])))  #slicing and appending
				count=0
		return(p)				#return
	o = step4(m,n,o)			#fuction calling

	z=list(o)
	if(len(z)==0):
		z=list(m)
		z.extend(n)	 			# getting the last unempty ist so that we can have the prime implicants stored in a particular list
	if(len(z)==0):
		z=list(q)
		z.extend(w)
		z.extend(r)
	if(len(z)==0):
		z=list(f)
		z.extend(g)
		z.extend(h)
		z.extend(p)
	if(len(z)==0):
		z=list(a)
		z.extend(b)
		z.extend(c)
		z.extend(d)
		z.extend(e)

	def concatinate(q):							#concatinating the list of unneccesary repeatation of the implicants
		for i in range(len(q)):
			for k in range(1+i,len(q)):
				if(q[i][:num]==q[k][:num]):
					q[k] = ''
		while '' in q:
			q.remove('')
		return(q)					#return

	z = concatinate(z)

	if ")" in z[0]:			#function call
		def left(q):											#getting whats left in quine method of table and storing it in another list
			for i in range(len(q)):
				j=num+1
				while(q[i][j]!=')'):
					if(q[i][j].isdigit()==True):
						if(q[i][j+1].isdigit()==False):
							u.append(q[i][j])
							j+=1
						else:
							u.append(q[i][j]+q[i][j+1])
							j+=2
					else:
						j+=1
			return(u)						#return
		u=left(z)								#fucntion call

		def simple(u):												#removing repeated entries
			for i in range (len(u)):
				for k in range(i+1,len(u)):
					if(u[i]==u[k]):
						u[k]=''
			while '' in u:
				u.remove('')
			return(u)			#return
		u=simple(u)					#function call


	# Further code deals with the dont care conditions and isnt neccssary if you want to simplify it further it adds up to beauty.

		def dcare(f,u,v):
			count=0
			for i in range(len(f)):
				j=5													#to find out whats left, for loop run all over
				while(f[i][j]!=')'):
					if(f[i][j].isdigit()==True):
						if(f[i][j+1].isdigit()==False):
							if(f[i][j] not in u):
								count+=1							#loops
								u.append(f[i][j])
							j+=1
						else:
							if(f[i][j]+f[i][j+1] not in u):
								count+=1
								u.append(f[i][j]+f[i][j+1])
							j+=2
					else:												#else condition
						j+=1
				if(count>=1):
					v.append(f[i])
				count=0
			return(v,u)

		def acare(a,b,c,d,e,v):
			if(len(a)==0 and len(c)==0):
				v.extend(b)															#checking the left over in the very first seperation table
			if(len(b)==0 and len(d)==0):
				v.extend(c)
			if(len(c)==0 and len(e)==0):
				v.extend(d)
			if(len(d)==0):
				v.extend(e)
			for i in range(len(v)):
				v[i]=str(int(v[i],2))							#converting to decimal in returning the value
			return(v)
		v=acare(a,b,c,d,e,v)
		v,u=dcare(n,u,v)
		v,u=dcare(m,u,v)
		v,u=dcare(r,u,v)					#checking each step of the quine table for left over elements
		v,u=dcare(w,u,v)
		v,u=dcare(q,u,v)
		v,u=dcare(p,u,v)
		v,u=dcare(h,u,v)
		v,u=dcare(g,u,v)
		v,u=dcare(f,u,v)
		v=concatinate(v)

		z.extend(v)
					#storing all implicants including dont care in the same list
		def order(z):
			for i in range(len(z)):
				count=0
				count1=0
				for j in range(num):
					if(z[i][j]=='x'):
						count1+=1
				a=num+1
				while(z[i][a]!=')'):
					if(z[i][a].isdigit()==True):
						if(z[i][a+1].isdigit()==False):
							if z[i][a] in ess:
								count+=1
							a+=1
						else:
							if((z[i][a]+z[i][a+1]) in ess):
								count+=1
							a+=2
					else:
						a+=1
				if(count==(2*count1)):
					temp = z[0]
					z[0]=z[i]
					z.pop(i)
					z.insert(1,temp)
			return(z)
		z=order(z)

		def imp(z):
			prime=[]
			for i in range(len(z)):
				count=0
				j=num+1
				while(z[i][j]!=')'):
					if(z[i][j].isdigit()==True):
						if(z[i][j+1].isdigit()==False):
							if z[i][j] in ess:
								count+=1
								ess.remove(z[i][j])
							j+=1
						else:
							if((z[i][j]+z[i][j+1]) in ess):
								count+=1
								ess.remove((z[i][j]+z[i][j+1]))
							j+=2
					else:
						j+=1
				if(count>=1):
					prime.append(z[i])
			return(prime)
		z=imp(z)

	# Expresing the prime implicants in the form of 4 variables

	def exp(z):
		if(num==4):
			dir = {0:'abcd',1:'abcz',2:'abyd',3:'abyz',4:'axcd',5:'axcz',6:'axyd',7:'axyz',8:'wbcd',9:'wbcz',10:'wbyd',11:'wbyz',12:'wxcd',13:'wxcz',14:'wxyd',15:'wxyz'}
		elif(num==3):
			dir = {0:'abc',1:'aby',2: 'axc',3:'axy',4:'wbc',5:'wby',6:'wxc',7:'wxy'}		#Dictionary
		elif(num==2):
			dir = {0:'ab',1:'ax',2: 'wb',3:'wx'}
		f=''
		if ')' in z[0]:
			for i in range(len(z)):
				s=[]								#loops
				j=num+1
				while(z[i][j]!=')'):
					if(z[i][j].isdigit()==True):
						if(z[i][j+1].isdigit()==False):
							s.append(dir[int(z[i][j])])				#string appending
							j+=1
						else:
							s.append(dir[int(z[i][j]+z[i][j+1])])
							j+=2
					else:
						j+=1
				for j in range(num):
					count=0
					for k in range(0,len(s)-1):
						if(s[k][j]==s[k+1][j]):				#adding up the variable to create expression
							count+=1
					if(count==(len(s)-1)):
						if(s[k][j]=='a'):
							f=f+'w\''
						elif(s[k][j]=='b'):
							f=f+'x\''
						elif(s[k][j]=='c'):
							f=f+'y\''
						elif(s[k][j]=='d'):
							f=f+'z\''
						else:
							f=f+s[k][j]
				if(i!=(len(z)-1)):
					f=f+'+'
		else:
			s=[]
			decimal =0
			for i in range(len(z)):
				for digit in z[i]:
					decimal = decimal*2 + int(digit)
				z[i]=decimal
				decimal=0
			for i in range(len(z)):
				s.append(dir[(z[i])])
			for i in range(len(s)):
				for j in range(len(s[i])):
					if(s[i][j]=='a'):
							f=f+'w\''
					elif(s[i][j]=='b'):
						f=f+'x\''
					elif(s[i][j]=='c'):
						f=f+'y\''
					elif(s[i][j]=='d'):
						f=f+'z\''
					else:
						f=f+s[i][j]
				if(i!=(len(z)-1)):
					f=f+'+'					#SOP operator
		return(f)
	stringOut=exp(z)		#storing
	stringOut = stringOut.replace('x','B').replace('y','C').replace('w','A').replace('z','D')
	return (stringOut)    	#returning the K map value back


##################################### SOP to POS #####################
def count_no_alphabets_SOP(SOP):
	i = 0
	no_var = 0

	# As expression is standard so total no.
	# of alphabets will be equal
	# to alphabets before first '+' character
	while (SOP[i]!='+'):

		# checking if character is alphabet
		if (SOP[i].isalpha()):
			no_var+= 1
		i+= 1
	return no_var

def count_unique(string):
    unique = []
    for char in string[::]:
        if char not in unique:
            unique.append(char)
    return(len(unique))

def get_unique_order(string):
    word = string

    unique_characters = ""

    for character in word:
        if character not in unique_characters:
            unique_characters += character

    return unique_characters


def get_POS(string):
	string_letter_only = string.replace(" ", "").replace("'","").replace("+","")

	unique_var = count_unique(string_letter_only) # number of unique variable
	#print("number of unique: ", unique_var)
	#if count_no_alphabets_SOP(string) != unique_var:
	    #print("wrong syntax")


	unique_str = get_unique_order(string_letter_only)

	#print("unique_str: ",unique_str)                              	# ABC

	string_plus = string.replace(" ", "")


	for i in range(len(unique_str)):
	    string_plus = string_plus.replace(unique_str[i] + "'", "0")  ### 111 + 011
	    string_plus = string_plus.replace(unique_str[i] , "1")

	minterm_arr = []

	first_string = string_plus[0:unique_var]
	##print("string_plus[0:unique_var]: ", string_plus[0:unique_var])


	#minterm_arr.append(str(int(first_string)))
	minterm_arr.append(first_string)
	#print("minterm_arr first:", minterm_arr)

	for i in range(len(string_plus)):
		if string_plus[i] == "+":
			str_temp = string_plus[i+1:i+4]
			minterm_arr.append(str_temp)

	#print("Step 2 minterm_arr: ",minterm_arr)
	##print("minterm_arr:  integer", int(minterm_arr))
	#print(string_plus)



	maxterm_arr = []
	for i in range(2**unique_var):
		temp = bin(i)[2:]

		if len(temp) == unique_var:
			pass
		else:
			for j in range(unique_var - len(temp)):
				temp =  '0' +temp
		maxterm_arr.append(temp)
	#print("maxterm_arr", maxterm_arr)

	maxterm_arr = [i for i in maxterm_arr if i not in minterm_arr]

	#print("maxterm_arr another ", maxterm_arr)
	#print("maxterm_arr[0][0]: ", maxterm_arr[0][0])

	POS = ""
	for i,maxterm in enumerate(maxterm_arr): 	### 110,
		temp_maxterm = "("
		for j in range(unique_var):
			unique_str_index = unique_str[j]
			if maxterm_arr[i][j] == "0":
				temp = maxterm_arr[i][j].replace("0",unique_str_index)
			elif maxterm_arr[i][j] == "1":
				temp = maxterm_arr[i][j].replace("1",unique_str_index + "'")
			temp_maxterm = temp_maxterm + temp + "+"
		temp_maxterm = temp_maxterm[0:-1] + ")"
		POS = POS + temp_maxterm + "."
		if i == len(maxterm_arr):
			POS = POS[0:-1]
	return POS[0:-1]


###################################### POS to SOP


def get_SOP(string):
	#print("string: ", string)
	string_letter_only = string.replace(" ", "").replace("'","").replace(".","").replace(")","").replace("(","").replace("+","")
	#print("string_letter_only: ",string_letter_only)
	unique_var = count_unique(string_letter_only) # number of unique variable
	#print("number of unique: ", unique_var)
	#if count_no_alphabets_SOP(string) != unique_var:
		#print("wrong syntax")

	unique_str = get_unique_order(string_letter_only)
	#print("unique_str: ",unique_str)

	str_dot = string.replace(" ", "").replace(")","").replace("(","").replace("+","")
	#print("str_dot: ", str_dot)
	for i in range(len(unique_str)):
		str_dot = str_dot.replace(unique_str[i] + "'", "1")
		str_dot = str_dot.replace(unique_str[i], "0")
	#print("str_bin: ", str_dot)

	maxterm_arr = []

	first_string = str_dot[0:unique_var]
	##print("string_plus[0:unique_var]: ", string_plus[0:unique_var])


	#minterm_arr.append(str(int(first_string)))
	maxterm_arr.append(first_string)
	#print("maxterm_arr first:", maxterm_arr)

	for i in range(len(str_dot)):
		if str_dot[i] == ".":
			str_temp = str_dot[i+1:i+4]
			maxterm_arr.append(str_temp)

	#print("Step 2 maxterm_arr: ",maxterm_arr)
	##print("minterm_arr:  integer", int(minterm_arr))

	minterm_arr = []
	for i in range(2**unique_var):
		temp = bin(i)[2:]

		if len(temp) == unique_var:
			pass
		else:
			for j in range(unique_var - len(temp)):
				temp =  '0' +temp
		minterm_arr.append(temp)
	#print("minterm_arr", minterm_arr)

	minterm_arr = [i for i in minterm_arr if i not in maxterm_arr]

	#print("maxterm_arr another ", minterm_arr)
	#print("len(minterm_arr): ",len(minterm_arr))  ## len = 4

	SOP = ""

	for i in range(len(minterm_arr)):
		for j in range(unique_var):
			if minterm_arr[i][j] == "1":
				SOP = SOP +  unique_str[j]
			elif minterm_arr[i][j] == "0":
				SOP = SOP + unique_str[j] + "'"
		SOP = SOP + " + "
	return SOP[0:-3]

# string = "ABC + A'B'C' + A'BC + ABC'"
string_SOP = "x'y'z + x'yz' + xy'z + xyz + xy'z'"
string_POS = "(x+y+z).(x+y'+z').(x'+y+z).(x'+y'+z)"
#print("string_SOP: ", string_SOP)
#print("String_POS: ", string_POS)

#print("SOP to POS:", SOPtoPOS(string_SOP))
#print("POS to SOP:", POStoSOP(string_POS))


def bin_to_BCD(string):
    dec = int(string, 2)

    # split
    dec = str(dec)

    # 4 digit
    def make_4_digit(string):
        length = len(string)
        for i in range(4-length):
            string = "0" + string
        return string

    bcd = ""
    for i in dec:
        bcd += make_4_digit(convert(i, 10, 2))
    return bcd


def BCD_to_bin(string):
    bin_string = ""
    for i in range(int(len(string)/4)):
        temp2 = string[i*4:i*4+4]
        bin_string += convert(temp2, 2, 10)
    bin_string = convert(bin_string, 10, 2)
    return bin_string


def bin_to_gray(n):
    n = int(n, 2)
    n ^= (n >> 1)

    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]


def gray_to_bin(n):

    n = int(n, 2)
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]


def get_code(string, input, output):
    if input == "2" and output == "bcd":
        return bin_to_BCD(string)
    elif input == "2" and output == "gray":
        return bin_to_gray(string)

    elif input == "bcd" and output == "2":
        return BCD_to_bin(string)
    elif input == "bcd" and output == "gray":
        temp = BCD_to_bin(string)
        return bin_to_gray(temp)

    elif input == "gray" and output == "2":
        return gray_to_bin(string)
    elif input == "gray" and output == "bcd":
        temp = gray_to_bin(string)
        return bin_to_BCD(temp)

    elif input == "2" and output == "2":
        return string
    elif input == "gray" and output == "gray":
        return string
    elif input == "bcd" and output == "bcd":
        return string


if __name__ == '__main__':
    print(minFunc('4','(0,1,3,7,8,9,11,15)d-'))
    # print(minFunc('3','(2,5)d(0,4,6)'))
    # print(minFunc('4','(3,9,12,15)d(0,1,4,7,8,10,11,14)'))
    # print(minFunc('4','(1,2,4,5,6,10,11,12,13)d-'))
    # print(minFunc('4','(0,2,3,5,7,8,10,11,14,15)d-'))
    # print(minFunc('3','(0,1,4)d(5,6)'))
    # print(minFunc('4','(0,4,8,10)d(2,12,15)'))
    # print(minFunc('4','(1,5,6,12,13,14)d(2,4)'))
    # print(minFunc('2','(1,2)d-'))

##################################### POS to SOP #####################
# Python code to convert standard POS form
# to standard SOP form
