indian = ["samosa" , "kachuri" , "nan"];
usa = ["puri" , "cha" , "kfc"];

dish = input('enter your food name ');

if dish in indian :
    print("this is indian food ");

elif dish in usa :
    print('this  is a usa food ');

else:
    print('i dont know')

#    this is a question
coochbehar = ['natabari' , 'tufanganj' , 'dhalpal']
siliguri = ['hakim para' , 'dabgram' , 'ashigar']

city1 = input('enetr your 1st city :');
city2 = input('enter your 2nd city : ');

if city1 and city2 in coochbehar:
    print("your are now cooch behar");

elif city1 and city2 in siliguri:
    print( ' you are in siliguri')

else:
        print('error not found')


        # suegr level test

suger = input('Enter your suger levvel :')
suger = int(suger)

if 80<=suger<=100 :
    print('suger is normal');
elif suger<80:
    print('your suge level low');
elif suger<100:
        print('your suge level heigh');

