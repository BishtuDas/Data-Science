# read , write , and delet file

#any folder open use

f = open("class.py","r")

line = f.readlines()

print(line)

#  all modes work  r = open file and read  , w = open file for write, if the file does not exits that create , r+ = this is use file read and write,
# w+ = this is same as r+ but in this case the file cannot exits this is crate also    and last one a = this is use to append the file

#now  use w

f = open("mode.txt", "w")
f.write("this is make with python mode")

# use a when already line exit but and new line;

f = open('mode.txt',"a")
f.write("\n this is add with appened mode ")



#other way to read file;

with open("loop.py","r") as f:
    for line in f :
        print(line)
