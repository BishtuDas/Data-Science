# range use example renge(1,10)  that mins print 1 to 9 
# in pyhton loop is use like this 
Key_location = "chair";
location = ["room" , "chair" , "table" , "bed"]

for loc in location:
    if loc  == Key_location:
        print("key in", loc)
        
    else :
        print ('i dont get key :',loc)


        # continue

    for i in range(11):

       if i%2==1:
        continue
    print(i);


# while loop

n=0;
while n<=10:
    print(n);
    n=n+1;


    # question time Q>1 how many time get head
result = ["head", " head" , "tail" , "head" , "tail" , "head"]

c  = 0 ;
for item in result:

    if item == "head":
        c += 1;
        print("head get", c)

#Q>2 print square of all numbers in between 1 to 10 except even number
for x in range(1,11):
    if i% 2 == 0 :
        continue;
print(x*x)  

# q>3 patten

for q in range( 1,6):
    s = "";
for j in range(q):
     s+= '*';
print(s);

total=0;
expance_list  = [2340 , 2500 , 2100 , 3100 ]
for item in expance_list:
     total+=item;
     print("this is total ",total);





# lets says your running 5 km race ,write a  program that ,1.upon completing each 1 km asks you are tried 
# if you can say yes print you can not finish the race  and SAY no then print excilent

for i in range(5):
    print(f"you are complet {i+1}");
tried = input("are you tried ");
if tried == 'yes: