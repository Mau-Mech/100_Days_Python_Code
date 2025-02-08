hour = 0
mins = 1
dura = 2939

hour = hour + ((mins + dura)//60)
mins = (mins + dura) % 60

if hour >= 24:
       hour = hour % 24
       print(hour,":", mins)
else:
   print(hour ,":", mins)
   
y = 2 + 3 * 5.
print(Y)

 
