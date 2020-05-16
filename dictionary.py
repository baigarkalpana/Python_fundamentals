dict={1:100,2:200,3:300}

for x in dict:   //we get key 1,2,3
    print(x)


for i in dict:   // we get values 100,200,300
    print(dict[i])


for j in dict.values():      // we get values 100,200,300
    print(j)


for x,y in dict.items():     // we get both key and values
    print(x,y)

'''
output:
1
2
3

100
200
300

100
200
300

1 100
2 200
3 300
'''
