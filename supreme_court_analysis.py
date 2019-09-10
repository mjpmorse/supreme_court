import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Supreme court data from 1946-2017, Legacy data could be loaded
# to go back further
data = pd.read_csv('SCDB_2018_02_caseCentered_Citation.csv',
encoding = "ISO-8859-1")

#split the data by the term pre1980 and post1980
pre1980 = data[ data['term'] < 1980 ]
post1980 = data[data['term'] >= 1980]

#make some plots to visual data first

#Pre  1980 majority distribution plot
plt.title('1946 - 1979 Majority distribution')
plt.xlabel('Justices')
plt.ylabel('Fractional number of case')
pre1980_sums = pre1980['majVotes'].value_counts().sort_index()
pre1980_normal = pre1980_sums/sum(pre1980_sums)
pre1980_normal.plot(kind='bar')
plt.show()

#Post 1980 majority distribution plot

plt.title('1980 - 2017 Majority distribution')
plt.xlabel('Justices')
plt.ylabel('Fractional number of case')
post1980_sums = post1980['majVotes'].value_counts().sort_index()
post1980_normal = post1980_sums/sum(post1980_sums)
post1980_normal.plot(kind='bar')

plt.show()
#Average number of Justices in the majority and minority pre and post pre1980
pre1980_major = pre1980['majVotes']
pre1980_minor = pre1980['minVotes']
pre1980_maj_avg = np.average(pre1980_major)
pre1980_min_avg =np.average(pre1980_minor)

post1980_major = post1980['majVotes']
post1980_minor = post1980['minVotes']
post1980_maj_avg = np.average(post1980_major)
post1980_min_avg =np.average(post1980_minor)

print('The avg number of Justices in majority pre1980 was: '
+ str(round(pre1980_maj_avg,2) ) )

print('The avg number of Justices in majority post1980 was: '
+ str( round(post1980_maj_avg,2) ) )



print('The avg number of Justices in minority pre1980 was: '
+ str( round(pre1980_min_avg,2) ) )

print('The avg number of Justices in minority post1980 was: '
+ str( round (post1980_min_avg,2) ) )
