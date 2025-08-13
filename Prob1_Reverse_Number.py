num=12345
rev=0
#now looping the code to extract digits and storing them in a different variable (rev). So, that i could print it after the loop
while num>0:
  digit=num%10
  rev=rev*10+digit
  num=num//10
print(rev)  

  
