from functools import reduce


# must use reduce!

sentence = ['this','is','a','sentence']
out_str = str(reduce(lambda x,y: x+"z "+y, sentence))
print(out_str)

s = [-3,-6,3,5,0,-5]

print([x for x in s if x<0])