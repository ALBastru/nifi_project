import matplotlib.pyplot as plt
import pandas as pd
import json
import sys
from decimal import Decimal
import numpy as np
import matplotlib
matplotlib.style.use('ggplot')
import seaborn as sns
import os
 
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)


#sns.set(style="white", context="talk")

#df = pd.read_csv("all_results.csv", sep=",", usecols = ["goal", "duration"], nrows=20)

cols = list(pd.read_csv("all_results_lb.csv", nrows =1))
print (str(cols))

allNodes = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6']

fig = plt.figure()






# Use list comprehension to remove the unwanted column in **usecol**
######df= pd.read_csv("all_results.csv", usecols =[i for i in cols if i != 'goal'], sep=",", nrows=6)
			#df= pd.read_csv("all_results.csv", sep=",", nrows=12).drop_duplicates()
#df= pd.read_csv("all_results.csv", sep=",").drop_duplicates()
df= pd.read_csv("all_results_lb.csv", sep=",")
#df = pd.read_csv("all_results.csv", sep="," usecold =[fire_team,state,radio_silence,node,ignored_node,process_type,resource_qty,duration,time_since_start,goal_duration,type_a_count,type_b_count,type_c_count] , nrows=20)
df[sorted(df)]



print(df.describe() )

#sys.exit()

######df_custom = df.groupby(['goal','task', 'state', 'info_experiment_code','info_run_number', 'duration']).size()
#print ( df.groupby(['goal','task', 'state', 'info_experiment_code','info_run_number', 'duration']).size())




#print("\n\n\n\n" + str(list(df['state'].groupby(df['node'])))  )

print(df['duration'].groupby([ df['state'], df['goal'], df['info_experiment_code'], df['info_run_number'] ]).describe())

print("\n\n")

print(df['duration'].groupby([ df['state'], df['info_experiment_code'], df['task'] ]).describe())

print("\n\n")

print(df['duration'].groupby([ df['state'], df['info_experiment_code'] ]).describe())

bench_by_size = df['duration'].groupby([ df['state'], df['fire_team'] ])
means = bench_by_size.mean()/1000

print ("\n\n___________________________\n" + str(list(means.unique())))

print("\n\n\n\n\n\n\n \t\tMEANS:\n\n\n" + str(means) + "\n\n")




						# x = ['Def - FT A', 'Def - FT B', 'Man - FT A', 'Man - FT B']

						# y_values = list(means.unique())

						# x_pos = [i for i, _ in enumerate(x)]

						# plt.bar(x_pos, y_values)
						# plt.xlabel("Bound and team")
						# plt.ylabel("Time spent")
						# plt.title("Time spent by nodes in a specific bound")

						# plt.xticks(x_pos, x)




						# plt.show()

#					sys.exit()

for node in allNodes:		
	df_local = df.loc[df['node'] == node]
	print("\n\t " + node + "\t avg runtime " +str(df_local["duration"].mean()) + "\n\n")


print ("\n\nmean goal duration: " + str(df['goal_duration'].mean()) + "\n")

print ( df.groupby(['node', 'info_run_number']).size())

#####print ("\n\n\n mean of goal duration : \t" + str(df["duration"].mean()) )


#print ( df.groupby(['goal','info_experiment_code','info_run_number', 'duration']).size())


#print ( str(df.groupby(['node', 'info_experiment_code', 'info_run_number', 'goal_duration']).size()) )



means.unstack().plot.bar(color=list('rbg')+['0.75'], rot=0, figsize=(8,8)) 

#df.mean().unstack().plot.bar(color=list('rbg')+['0.75'], rot=0, figsize=(8,8)) 


plt.xlabel("State")
plt.ylabel("Average time spent (s)")
plt.title("Average time spent by teams in bounds LOAD BALANCING")
plt.savefig("fig1_" + foldername+"_LB.png")


plt.show()












groups = [[23,135,3], [123,500,1]]
group_labels = ['views', 'orders']


# Plot.
####pd.concat([df.groupby([['node']['duration'].mean(), df['fire_team'], df['state'], df['state']]).plot.bar())


#df.groupby([df['node'], df['fire_team'], df['state'], df['state']])['node'].count().plot(kind='bar', stacked=True, legend=True)


#       df.groupby('state')['duration'].mean().plot(kind='bar')




#              sys.exit()




df2 = df.groupby(['node'])['duration'].mean()/1000

ax = df2.plot(kind='bar', figsize=(10,6), color="indigo", fontsize=13);


#fig.suptitle('Distribution running time per node (s) NON Load Balancing', fontsize=20)
plt.xlabel('Node', fontsize=18)
plt.ylabel('Run time (s)', fontsize=16)
plt.title("Distribution running time per node (s) LOAD BALANCING")
plt.savefig("fig2_" + foldername+"_LB.png")
plt.show()












# df.plot(x="fire_team", y=["duration", "state"], kind='bar', stacked=True, legend=True)
# plt.show()




week_groups = df.groupby([df['node'], df['state']]
                          )['node'].count()
week_groups.plot(kind='bar',figsize=(20,10),legend=None , stacked=False)
#plt.legend(nodes_names, loc="center")
plt.savefig("tsk_t_pn_pie.png", dpi=360)
plt.xticks(rotation=360)



#fig.suptitle('Distribution of tasks per node and team NON Load Balancing', fontsize=20)
plt.xlabel('Nodes and Teams', fontsize=18)
plt.ylabel('Number of tasks', fontsize=16)
plt.title("Distribution of tasks per node and team LOAD BALANCING")
plt.savefig("fig3_" + foldername+"_LB.png")

plt.show()

















week_groups = df.groupby([df['node'], df['fire_team'], df['state'], df['state']]
                          )['node'].count()
week_groups.plot(kind='bar',figsize=(20,10),legend=None )
#plt.legend(nodes_names, loc="center")

plt.xticks(rotation=360)



#fig.suptitle('Distribution of tasks per node and team NON Load Balancing', fontsize=20)
plt.xlabel('Nodes and Teams', fontsize=18)
plt.ylabel('Number of tasks', fontsize=16)
plt.title("Distribution of tasks per node and team LOAD BALANCING")
plt.savefig("fig4_" + foldername+"_LB.png")

plt.show()



ax2 = pd.crosstab([ df['node'], df['state']],df['fire_team']).T.plot.bar()
	
#ax2.set_xlabel(all_nodes)
ax2.set_ylabel("tasks completed")
plt.xticks(rotation=360)
plt.savefig("tasks_per_node.png")


fig.suptitle('Distribution of tasks per node and team LOAD BALANCING', fontsize=20)
plt.xlabel('Node and Team', fontsize=18)
plt.ylabel('Number of tasks', fontsize=16)

plt.savefig("fig5_" + foldername+"_LB.png")
plt.show()



#######here

ax2 = pd.crosstab([ df['node'], df['state']],df['fire_team']).T.plot.bar()
	
#ax2.set_xlabel(all_nodes)
ax2.set_ylabel("tasks completed")
plt.xticks(rotation=360)
plt.savefig("fig6_" + foldername+"_LB.png")


#fig.suptitle('Distribution of tasks per node and team NON Load Balancing', fontsize=20)
plt.xlabel('Node and Team', fontsize=18)
plt.ylabel('Number of tasks', fontsize=16)
plt.title("Distribution of tasks per node and team LOAD BALANCING")
plt.savefig("fig7_" + foldername+"_LB.png")
plt.show()











sys.exit()
#print ("\n\nmean uration: " + print(df['goal_duration']) + "\n")

####print ( df.groupby(['node','state', 'radio_silence', 'process_type']).size())

#print ( df.groupby(['goal','info_experiment_code','info_run_number']).size())

print ( df.groupby(['goal','info_experiment_code','info_run_number', 'duration']).size())

#print ( df.groupby(['node', 'process_type']).size())

sys.exit()

# #  3# 3 # # # df.plot(x="goal", y=["duration", "time_since_start"], kind='bar', stacked=True, legend=True)


#df.groupby([df.index.date, 'action']).count().plot(kind='bar')

nodes_names = ['Node 1', 'Node 2', 'Node 3', 'Node 4', 'Node 5', 'Node 6']

df[sorted(df)]




df2 = df[df.duplicated('goal', keep=False)].groupby('duration').apply(list).reset_index()

print(str(df2))

sys.exit()


df.drop_duplicates().plot.pie(y='duration',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
plt.legend(nodes_names, loc="center")
plt.savefig("global_tsk_t_pn_pie"+ ".png")
plt.show()	


all_goals = list(df['goal'].unique())
all_nodes = list(df['node'].unique())

goal_counter = 0
for goal in all_goals:
	goal_counter+=1
	print ("Goal: " + goal + "\n\n")		
	df_local = df.loc[df['goal'] == goal]
	df_local.drop_duplicates()
	df_local[sorted(df_local)]
	#print("\n" + str(df_local) + "\n\n")

	df_local.plot.pie(y='duration',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
	plt.legend(nodes_names, loc="center")
	plt.savefig("tsk_t_pn_pie_" + str(goal_counter)+ ".png")
	plt.show()	


	ax = df_local.plot(x='task', y=["duration", "state"], kind='bar', stacked=True, legend=True)
	#ax = df_local.groupby(['goal', 'fire_team']).plot(kind='bar', stacked=True, legend=True)
	plt.show()
	

	#local_df.groupby(['goal', 'duration']).size().unstack()
	ax.set_xlabel(goal)
	ax.set_ylabel("time in ms")
	
	#plt.savefig('tasks_per_node_.png')
	plt.show()
	
	#df_local.groupby('node')['fire_team'].apply(lambda x: x.value_counts().head(1))
	#ax2 = df_local['node'].value_counts().plot.bar()
	ax2 = pd.crosstab([ df_local['node'], df_local['state']],df_local['fire_team']).T.plot.bar()
	
	ax2.set_xlabel(all_nodes)
	ax2.set_ylabel("tasks completed")
	plt.xticks(rotation=360)
	plt.savefig("tasks_per_node_" + str(goal_counter)+ ".png")
	plt.show()
	#sys.exit()
print("total: \t" + str(len(all_goals)) + "\n\n")
sys.exit()







# all_goals = list(df['goal'].unique())
# all_nodes = list(df['node'].unique())


# # nrow=int(math.sqrt(len(all_goals))) + 1
# # ncol=int(math.sqrt(len(all_goals))) + 1


# nrow=2
# ncol=len(all_goals)



# fig, axes = plt.subplots(nrow, ncol)

# #nrow =  nrow - int(len(all_goals))/2 + 2
# #ncol= ncol - int(len(all_goals))/2 + 1
# print(str(len(all_goals)) + "  <= " + str(nrow) + " x " + str(ncol)  )

# ccounter = -1
# for goal in all_goals:
# 	ccounter += 1	
# 	print ("Goal: " + goal + "\n\n")	
# 	df_local = df.loc[df['goal'] == goal]
# 	df_local.drop_duplicates()
# 	df_local[sorted(df_local)]
# 	print("\n" + str(df_local) + "\n\n")
# 	ax = df_local.plot(x='task', y=["duration", "time_since_start"], kind='bar', stacked=True, legend=True, ax=axes[0, ccounter])	
# 	ax.set_xlabel(goal)
# 	ax.set_ylabel("time in ms " + str(ccounter))
# 	plt.show()
# 	ax2 = df_local['node'].value_counts().plot.bar(ax=axes[1, ccounter])
# 	ax2.set_xlabel(all_nodes)
# 	ax2.set_ylabel("tasks completed " + str(ccounter))
# 	plt.show()
# 	#plt.tight_layout()
# 	#sys.exit()
# print("total: \t" + str(len(all_goals)) + "\n\n")
# sys.exit()







##df = pd.read_csv("all_results.csv", sep="," usecold =[fire_team,state,radio_silence,node,ignored_node,process_type,resource_qty,duration,time_since_start,goal_duration,type_a_count,type_b_count,type_c_count] , nrows=20)


# all_goals = list(df['goal'].unique())

# for goal in all_goals:
# 	print ("Goal: " + goal + "\n\n")
# 	#df.loc[df['goal'] == 'foo']
# 	local_df = df.loc[df['goal'] == goal]
# 	local_df
# 	sys.exit()





sys.exit()

# fig, ax = plt.subplots(figsize=(10,7))  

# months = df['goal'].drop_duplicates()
# margin_bottom = np.zeros(len(df['goal'].drop_duplicates()))
# colors = ["#006D2C", "#31A354","#74C476"]

# for num, month in enumerate(months):
#     values = list(df[df['goal'] == month].loc[:, 'duration'])

#     df[df['goal'] == month].plot.bar(x='goal',y='duration', ax=ax, stacked=True, 
#                                     bottom = margin_bottom, color=colors[num], label=month)
#     margin_bottom += values

# plt.show()









sys.exit()



all_goals = list(df['goal'].unique())

for goal in all_goals:
	print ("Goal: " + goal + "\n\n")
	#df.loc[df['goal'] == 'foo']
	local_df = df.loc[df['goal'] == goal]
	print("\n\n" + str(local_df) + "\n\n")
	all_duration = list(local_df['duration'].unique())
	print("\n\n" + str(all_duration) + "\n\n")
	ind = [goal for goal in all_goals]
	print("\n\n\t" + str(len(ind)) + "\t\t" + str(len(all_duration)) + "\n\n\n"  )
	plt.bar(ind, ind, width=0.6, label='goal', color='gold')
	plt.show()
	sys.exit()
sys.exit()
bronzes = np.array([10,7,10,6,6])
silvers = np.array([14,10,8,8,6])
golds = np.array([14,14,11,9,8])
ind = [country for country in countries]
 



sys.exit()

plt.bar(ind, golds, width=0.6, label='golds', color='gold', bottom=silvers+bronzes)
plt.bar(ind, silvers, width=0.6, label='silvers', color='silver', bottom=bronzes)
plt.bar(ind, bronzes, width=0.6, label='bronzes', color='#CD7F32')
 
plt.xticks(ind, countries)
plt.ylabel("Medals")
plt.xlabel("Countries")
plt.legend(loc="upper right")
plt.title("2018 Winter Olympics Top Scorers")
plt.show()





sys.exit()

fig, axes = plt.subplots(nrows=1, ncols=3)

ax_position = 0
for concept in df.index.get_level_values('concept').unique():
    idx = pd.IndexSlice
    subset = df.loc[idx[[concept], :],
                    ['cmp_tr_neg_p_wrk', 'exp_tr_pos_p_wrk',
                     'cmp_p_spot', 'exp_p_spot']]     
    print(subset.info())
    subset = subset.groupby(
        subset.index.get_level_values('datetime').year).sum()
    subset = subset / 4  # quarter hours
    subset = subset / 100  # installed capacity
    ax = subset.plot(kind="bar", stacked=True, colormap="Blues",
                     ax=axes[ax_position])
    ax.set_title("Concept \"" + concept + "\"", fontsize=30, alpha=1.0)
    ax.set_ylabel("Hours", fontsize=30),
    ax.set_xlabel("Concept \"" + concept + "\"", fontsize=30, alpha=0.0),
    ax.set_ylim(0, 9000)
    ax.set_yticks(range(0, 9000, 1000))
    ax.set_yticklabels(labels=range(0, 9000, 1000), rotation=0,
                       minor=False, fontsize=28)
    ax.set_xticklabels(labels=['2012', '2013', '2014'], rotation=0,
                       minor=False, fontsize=28)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(['Market A', 'Market B',
               'Market C', 'Market D'],
              loc='upper right', fontsize=28)
    ax_position += 1

# look "three subplots"
#plt.tight_layout(pad=0.0, w_pad=-8.0, h_pad=0.0)

# look "one plot"
plt.tight_layout(pad=0., w_pad=-16.5, h_pad=0.0)
axes[1].set_ylabel("")
axes[2].set_ylabel("")


sys.exit()





#df = pd.read_csv('all_results.csv',sep=',')
#df.plot(x='time_since_start', y='type_a_count')
#plt.show()



#df = pd.read_csv("all_results.csv",sep=",").set_index('goal')

#df = pd.read_csv("all_results.csv",sep=",")

plt.style.use('seaborn-whitegrid')

df = pd.read_csv("all_results.csv", sep=",", usecols = ["goal", "duration"], nrows=20)










sys.exit()


all_goals = list(df['goal'].unique())



fig, ax = plt.subplots()

df.groupby(['goal', 'duration']).size().unstack().plot(kind='bar', stacked=True, legend=True)

tick_idx = plt.xticks()[0]

tick_idy = plt.yticks()[0]

print("\n\n" + str(tick_idy) + "\n\n" + str(df))
#sys.exit()

x_values = [0.1, 0.3, 0.4, 0.2]

for i in range(len(all_goals)): # your number of bars
	print("\n\n" + str(i) + "\n")
	plt.text(x = tick_idx[i]-0.25, #takes your x values as horizontal positioning argument 
	y = tick_idy[i]+1, #takes your y values as vertical positioning argument 
	#s = data_labels[i], # the labels you want to add to the data
	s = i, # the labels you want to add to the data
	size = 9) # font size of datalabels

plt.show()

print("\t\t\t DONE")

sys.exit()


for goal in all_goals:
	print ("Goal: " + goal + "\n\n")
	#df.loc[df['goal'] == 'foo']
	local_df = df.loc[df['goal'] == goal]
	#print( str(local_df) + "\n\n\n")
	fig, ax = plt.subplots()
	#ax = local_df.groupby(['goal', 'duration']).size().unstack().plot(kind='bar', stacked=False, legend=False, ax=ax)
	ax = local_df.groupby(['goal', 'duration']).plot(kind='bar', stacked=True, legend=True, ax=ax)
	plt.show()

	sys.exit()


# print("\n\nFirst 20 records are:\n")




# print("\n\n\n List of goals:\n", json.dumps( list(set(df.goal)), indent=4 ) + "\n\n\n\n")

# print("\n\nDF Info: \n")

# df.info()


print("\n\n")

#				fig, ax = plt.subplots()

#				ax = df.groupby(['goal', 'duration']).size().unstack().plot(kind='bar', stacked=False, legend=False, ax=ax)



#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))


#plt.tight_layout()


# for rowNum,row in df.iterrows():
#     xpos = 0
#     print("\n\trowNum:\t" + str(rowNum) + "\t\trow:\t" + str(row['duration']) + "\n\n\n")
#     for val in row:
#         xpos += int(row['duration'])
#         ax.text(xpos + 1, rowNum-0.05, str(val), color='black')
#     xpos = 0
#display(ax)





plt.show()

sys.exit()


print("\n\n\n List of goals:\n", json.dumps( list(set(df.goal)), indent=4 ) + "\n\n\n\n")

print(json.dumps( list(df['goal'].unique()), indent=4 ) )


#df.set_index('word').plot(kind='barh', stacked=True)


############df.set_index('goal').plot(kind='barh', stacked=True)


df2 = df[df.duplicated('goal', keep=False)].groupby('duration').apply(list).reset_index()

df2.info()

#df2.plot(kind='barh', stacked=True)

######df.set_index('goal').plot(kind='barh', stacked=True)


# # # pd.crosstab(df['goal'], df['type_a_count'])[['state','resource_qty']].plot()

###print(df['goal'].value_counts().head(40).index)

####d = dict(zip(df.index,df.values.tolist()))

####print(json.dumps(d, indent=4))

#df.set_index('Tour')[['Start', 'End']].plot.bar()
####df.set_index('goal')[['duration', 'type_a_count']].plot.bar()
plt.show()