#coding=utf-8

# from split_word import *
# from get_tfidf import get_tfidf


# #sp = separateWords()
# #sp.split_word()

# get_tfidf()

# now clean the company description data

f = open("company.csv")

g = open("test.txt", 'wb')

str_1 = f.readline().decode('gb2312').encode('utf-8')
cnt = 0
while str_1:
	g.write(str_1)
	g.write('\n')
	str_1 = f.readline()
	try:
		str_1 = str_1.decode('gb2312').encode('utf-8')
	except:
		# g.write(str_1)
		cnt = cnt + 1
		print cnt
		# break

g.close()