import csv
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

start,end,n_bins = 0,1,100


a1=['GPM','XPM','KDA','P/F','C/P','result']



for i in range(5):
	matchFile = open('normalized_data.csv', 'r')
	matchInfo = csv.reader(matchFile)

	winlist=[]
	loselist=[]
	for info in matchInfo:
		if info[5]=="1":
			winlist.append(float(info[i]))
		if info[5]=="0":
			loselist.append(float(info[i]))

	plt.figure(i)
	plt.hist(loselist, bins=n_bins, range=(start,end), color='red')
	plt.hist(winlist, bins=n_bins, range=(start,end), color='blue')
	
	plt.legend(handles=[mpatches.Patch(color='red', label='Lose_'+a1[i]), mpatches.Patch(color='blue', label='Win_'+a1[i])])
	plt.xlabel('Value of '+a1[i])
	plt.ylabel('Number of '+a1[i])
	plt.show()


	anova_result = stats.f_oneway(winlist, loselist)
	pvalue=anova_result.pvalue
	pvalue_show=pvalue*100
	print('About '+ a1[i] + ': 1) The P-value of one-way ANOVA is '+ str(pvalue_show) +'2) Can we reject H0? ', 'Yes' if pvalue<0.01 else 'No')


	kw_result = stats.kruskal(winlist, loselist)
	pvalue=kw_result.pvalue
	pvalue_show=pvalue*100
	print('About '+ a1[i] + ': 1) The P-value of Kruskall-Wallis H-test is '+ str(pvalue_show) +'2) Can we reject H0? ', 'Yes' if pvalue<0.01 else 'No')





