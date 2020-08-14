# bounce.py
#
# Exercise 1.5
init_height = 100
new_height = 0
#bounce_back = 3/5*height
bounce_num = 1
for i in range(1,11):
    #print(bounce_num, new_height)
    new_height = init_height*3/5
    init_height=new_height
    print(i, round(new_height,4))

