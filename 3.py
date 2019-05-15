inp=str(input())
if((inp>='a' and inp<='z') or (inp>='A' and inp<='Z')):
	if(inp=='a' or inp=='e' or inp=='i' or inp=='o' or inp=='u' or inp=='A' or inp=='E' or inp=='I' or inp=='O' or inp=='U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
