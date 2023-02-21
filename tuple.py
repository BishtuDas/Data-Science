population ={
    'china' : 134,
    'india' : 123,
    'usa' : 23,
    'pakistan' : 21
}

def add():
    country = input( "enter your country name :")
    country = country.lower();
    if country in population:
        print( "this country name already here :")
        return
    p = input("enter population in enter city :")
    p = float(p);

    population[country]=p
    print_all();


    def remove():
      country = input("enter your delet country name :")
      country = country.lower()
      if country not in population:
        print("country does not exit")
        return
    del population[country];
    print_all();


    def quarry():
        country = input("enter your country name to quarry:")
        country = country.lower()

        if country not in population:
            country = country.lower()        
            print("your country not in the list please add :")
            return
        print(f"populatoion of {country} is : {population} core")
       
    def print_all():
        for country ,p in population.items():
            print(f"{country}==>{p}");


            def main():
                op = input("enter your option( add,remove, quarry to print :)")
                if op.lower() == 'add':
                    add();
                elif op.lower() == 'remove':
                    remove();
                elif op.lower() == "quarry":
                    quarry();
                print_all();


        if __name__ == '__main__':
         main()


   