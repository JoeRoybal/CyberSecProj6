# Used for reference 
#root:$1$h0oYf/69$l4JuFV3DF5bCyI2Maifaa/:16467:0:99999:7::: 
#sys:$1$fUX6BPOt$Miyc3UpOzQJqz4s5wFD9l0:14742:0:99999:7:::
import crypt 
def brutePass(salt, passHashed): 
	salt = "$1$"+salt 
	passHashed = salt+"$"+passHashed 
	dictFile = open('rockyou.txt', 'r') 
	for password in dictFile.readlines():
                password = password.strip('\n') 
		foundPassword = crypt.crypt(password, salt) 
		if passHashed == foundPassword:
                        return password 

def main(): 
	fname = open('shadow.txt','r') 
	for x in fname.readlines():
                line = x.strip() 
		user = line.split(':')[0] 
		salt = line.split('$')[2] 
                hash = line.split('$')[3].split(':')[0] 
		print "User: ",user,"\t","Salt: ",salt,"\t","Hash: ",hash 
			password = brutePass(salt, hash) 
			if password:
                       		print "The password is ", password 
			else: 
				print "no password found"
        fname.close() 

if __name__== "__main__": 
	main()

# Cyber Ducky Strikes Again!!!
#	    _
#	  >(.)__
#	   (___/
