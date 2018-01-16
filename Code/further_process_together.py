import csv



matchFile = open('players_combine_match.csv', 'r')
matchInfo = csv.reader(matchFile)

match=[]
match=list()

a1=['player_id','match_id','GPM','XPM','KDA','P/F','C/P','result']

n=0


max_GPM=0
max_XPM=0
max_KDA=0
max_PF=0
max_CP=0

min_GPM=100000000
min_XPM=100000000
min_KDA=100000000
min_PF=100000000
min_CP=100000000



# data=[]
# label=[]



for info in matchInfo:

	if n==0:
		n += 1
		continue

	GPM=float(info[2])
	XPM=float(info[3])
	KDA=float(info[4])
	PF=float(info[5])
	CP=float(info[6])
	#result=info[7]

##############################
	if GPM > max_GPM:
		max_GPM=GPM

	if GPM < min_GPM:
		min_GPM=GPM


##############################
	if XPM > max_XPM:
		max_XPM=XPM

	if XPM < min_XPM:
		min_XPM=XPM


##############################
	if KDA > max_KDA:
		max_KDA=KDA

	if KDA < min_KDA:
		min_KDA=KDA


##############################
	if PF > max_PF:
		max_PF=PF

	if PF < min_PF:
		min_PF=PF


##############################
	if CP > max_CP:
		max_CP=CP

	if CP < min_CP:
		min_CP=CP

# print(max_GPM)


def normal(x,max,min):
	final=(x-min)/(max-min)
	return final


matchFile = open('players_combine_match.csv', 'r')
matchInfo = csv.reader(matchFile)

n=0

with open('normalized_data.csv', 'w',newline='') as combineFile:
    abcsv = csv.writer(combineFile, dialect='excel')
    for info in matchInfo:

    	# print(info)

    	data=[]



    	if n==0:
    		n += 1
    		# print(n)
    		continue

    	GPM=float(info[2])
    	XPM=float(info[3])
    	KDA=float(info[4])
    	PF=float(info[5])
    	CP=float(info[6])



    	GPM=normal(GPM,max_GPM,min_GPM)
    	XPM=normal(XPM,max_XPM,min_XPM)
    	KDA=normal(KDA,max_KDA,min_KDA)
    	PF=normal(PF,max_PF,min_PF)
    	CP=normal(CP,max_CP,min_CP)


    	data.append(GPM)
    	data.append(XPM)
    	data.append(KDA)
    	data.append(PF)
    	data.append(CP)



    	result=info[7]
        
    	if result=="win":
    		data.append(1)
    	else:
    		data.append(0)

    	abcsv.writerow(data)

    	n +=1

















