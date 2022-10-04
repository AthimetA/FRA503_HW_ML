df['Attrition_Flag'].value_counts().plot.bar()

df.groupby('Attrition_Flag')['Gender'].value_counts().plot.bar()

gen_bar = pd.crosstab(df['Gender'], df['Attrition_Flag'])
gen_bar.div(gen_bar.sum(axis = 1).astype(float), axis = 0).plot(kind = 'bar', stacked = True, figsize = (7,7))
plt.xlabel('Gender')
plt.ylabel('Percentage')

df.plot.scatter('Total_Relationship_Count', 'Total_Trans_Amt')