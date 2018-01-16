import csv


# read csv files

matchFile = open('match.csv', 'r')
matchInfo = csv.reader(matchFile)

match=[]
match=list()

for info in matchInfo:
    match.append(info)

playerFile = open('players.csv', 'r')
playerInfo = csv.reader(playerFile)


heroFile = open('players_combine_heroname.csv', 'r')
heroInfo = csv.reader(heroFile)


heroname=[]
heroname=list()


for hinfo in heroInfo:
    heroname.append(hinfo)


# define parameters

n=0
current_matchid=0
carry_num_radiant=0
support_num_radiant=0
carry_num_dire=0
support_num_dire=0


a1=['player_id','match_id','GPM','XPM','KDA','P/F','C/P','result']
id_radiant=[0,1,2,3,4]
id_dire=[128,129,130,131,132]
num=[0,6,7]

KDA_num=[8,9,10]

PF_num=[14,16]


# write csv files

with open('players_combine_match.csv', 'w',newline='') as combineFile:
    abcsv = csv.writer(combineFile, dialect='excel')

    for i in playerInfo:

        if n==0:
            abcsv.writerow(a1)
            n += 1
            continue

       

        a=[]


        ######## append the playerid
        a.append(str(n))
        ##########################################
        
        ######## append matchid, GPM, XPM
        for j1 in num:
            a.append(i[j1])
        ##########################################

        ######### append KDA

        Kills=int(i[KDA_num[0]])
        Deaths=int(i[KDA_num[1]])
        Assists=int(i[KDA_num[2]])
        if Deaths==0:
        	Deaths=1

        KDA=(Kills+Assists)/Deaths
        a.append(KDA)


        ########################################

        ############ append P/F
        
        hero_damage=int(i[PF_num[0]])
        tower_damage=int(i[PF_num[1]])

        all_damage=hero_damage+tower_damage

        if all_damage==0:
        	all_damage=1


        PF=tower_damage/all_damage


        a.append(PF)


        ##########################################
        
        ########### append C/P






        ##########################################

        ###################append C/P, the game result
        matchid_plus_one=int(i[0])+1
        matchid=int(i[0])
        resultline=match[matchid_plus_one]

        player_slot=int(i[3])

        heroline=heroname[n]

        a.append(heroline[1])


        if player_slot in id_radiant and resultline[9]=='True':
            a.append('win')
        if player_slot in id_radiant and resultline[9]=='False':
            a.append('lose')    
        if player_slot in id_dire and resultline[9]=='True':
            a.append('lose')
        if player_slot in id_dire and resultline[9]=='False':
            a.append('win')

        ##########################################################

        if len(a)==8:
            abcsv.writerow(a)

        n += 1
    
        # if n>=30001:
        #     break














		



