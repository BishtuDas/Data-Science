list = [ 2000, 2350 ,  2600 , 2139 , 2190]

print('extra money speed commper to junuary :', list[1] - list[0]);
print('total expense in first quarter :' ,list[0]+ list[1] + list[2]);
print('spent exactly 2000 dollars in any month' , 2000 in list);
list.append(1950)


list[3]  = list[3]-200;
print("Expenses after 200$ return in April:",list)



heros=['spider man','thor','hulk','iron man','captain america']

heros.append('blackpanther')

print('afetr adding panther name in list :' , heros)


heros.remove('blackpanther');
heros.insert(3, 'black panther')

print('after adding blackpanhter name in after hulk :' , heros)
heros[1:3] = ['doctor strange'];

print(heros);

heros.sort();
print(heros);