import csv


# read csv files

# matchFile = open('match.csv', 'r')
# matchInfo = csv.reader(matchFile)

# match=[]
# match=list()

# for info in matchInfo:
#     match.append(info)

playerFile = open('players.csv', 'r')
playerInfo = csv.reader(playerFile)


heroFile = open('hero_names.csv', 'r')
heroInfo = csv.reader(heroFile)


heroname=[]
heroname=list()

count=0

for hinfo in heroInfo:
    heroname.append(hinfo)
    count += 1


#print("The length of heroname is "+str(count))
# print(heroname[count-1])


# define parameters

n=0
current_matchid=0
carry_num_radiant=0
support_num_radiant=0
carry_num_dire=0
support_num_dire=0


a1=['ForTest','C/P']
id_radiant=[0,1,2,3,4]
id_dire=[128,129,130,131,132]
num=[0]

KDA_num=[8,9,10]

PF_num=[14,16]


# write csv files

with open('players_combine_heroname.csv', 'w',newline='') as combineFile:
    abcsv = csv.writer(combineFile, dialect='excel')

    for i in playerInfo:

        if n==0:
            abcsv.writerow(a1)
            n += 1
            continue


        ###################append C/P
        matchid_plus_one=int(i[0])+1
        matchid=int(i[0])


        player_slot=int(i[3])
        heroid=int(i[2])
        # print(heroid)
        heroline=heroname[heroid]


        if matchid==current_matchid:
        	if player_slot in id_radiant:
        		#print("111")
        		if heroline[3]=="carry":
        			carry_num_radiant += 1

        		else:
        			support_num_radiant += 1	

        	if player_slot in id_dire:
        		#print("222")
        		if heroline[3]=="carry":
        			carry_num_dire += 1
        		else:
        			support_num_dire += 1

        else:

        	allnum_radiant=carry_num_radiant+support_num_radiant
        	# print("111111111111")
        	# print(allnum_radiant)

        	allnum_dire=carry_num_dire+support_num_dire
        	# print("222222222222")
        	# print(allnum_dire)


        	a_radiant=[]
        	a_radiant.append(n)
        	CP_radiant=carry_num_radiant/allnum_radiant
        	a_radiant.append(CP_radiant)

        	for playi in range(allnum_radiant):
        		abcsv.writerow(a_radiant)

        	a_dire=[]
        	a_dire.append(n)
        	CP_dire=carry_num_dire/allnum_dire
        	a_dire.append(CP_dire)


        	for playj in range(allnum_dire):
        		abcsv.writerow(a_dire)
     	
     	

        	current_matchid=matchid
        	carry_num_radiant=0
        	support_num_radiant=0
        	carry_num_dire=0
        	support_num_dire=0

        	if player_slot in id_radiant:
        		if heroline[3]=="carry":
        			carry_num_radiant += 1
        		else:
        			support_num_radiant += 1
        	if player_slot in id_dire:
        		if heroline[3]=="carry":
        			carry_num_dire += 1
        		else:
        			support_num_dire += 1	        	

        n += 1 

    
        # if n>=50:
        # 	break



    allnum_radiant=carry_num_radiant+support_num_radiant
    allnum_dire=carry_num_dire+support_num_dire

    a_radiant=[]
    a_radiant.append(n)
    CP_radiant=carry_num_radiant/allnum_radiant
    a_radiant.append(CP_radiant)

    for playi in range(allnum_radiant):
        abcsv.writerow(a_radiant)

    a_dire=[]
    a_dire.append(n)
    CP_dire=carry_num_dire/allnum_dire
    a_dire.append(CP_dire)


    for playj in range(allnum_dire):
        abcsv.writerow(a_dire)










		



