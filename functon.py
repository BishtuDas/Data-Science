def find (bishtu) :
    total = 0 ;
    for item in bishtu:
        total +=item
    return total

bishtu_expancess=[20,13,20,20]
bishtu_total = find(bishtu_expancess);

souvhik_expancess = [30,23,34,56];
souvhiik_total = find(souvhik_expancess)

print(bishtu_total);
print(souvhiik_total)

def math(redius,heigh):
 print("redius",redius);
 print("heigh",heigh);

 vol = 3.14*(redius**2)*heigh;
 return vol;

 r=5;
 h=10;
 print(math(r,h)); 