# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path

#Code starts here 

data=pd.read_csv('/opt/greyatom/kernel-gateway/data/executor/attachments/account/b93/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b81/cf538c6b-cf03-44f6-8e6a-34ee54be92d2/file.csv')

data['Gender'].replace('-','Agender',inplace=True)

gender_count=data['Gender'].value_counts()

print(gender_count)

gender_count.plot(kind='bar')

#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()

plt.pie(alignment)

alignment.plot(label='Character Alignment')



# --------------
#Code starts here
sc_df=data[['Strength','Combat']]

sc_covariance=sc_df['Strength'].cov(sc_df['Combat'])

sc_strength=sc_df['Strength'].std()

sc_combat=sc_df['Combat'].std()

sc_pearson=sc_covariance/(sc_strength*sc_combat)

ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df['Intelligence'].cov(ic_df['Combat'])
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here•	total_high=data['Total'].quantile(0.99)

total_high=data['Total'].quantile(0.99)
	
super_best=data[data['Total']>total_high]
	
super_best_names=super_best['Name'].tolist()
	
super_best_names




# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3)=plt.subplots(nrows=3, ncols=1 ,figsize=(20,10))

data.boxplot(column='Intelligence', ax=ax_1)
ax_1.set_title('Intelligence')

data.boxplot(column='Speed', ax=ax_2)
ax_2.set_title('Speed')

data.boxplot(column='Power', ax=ax_3)
ax_3.set_title('Power')



