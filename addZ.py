from functools import reduce


# must use reduce!

sentence = ['this','is','a','sentence']
out_str = str(reduce(lambda x,y: x+"z "+y, sentence))
print(out_str)