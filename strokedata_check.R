df = read.csv('/home/brugha/Documents/Project/strokedataset.csv')
head(df)
attach(df)
colnames(df)
target = df["stroke"]
df = df[c("gender","age","hypertension","heart_disease","ever_married","work_type","Residence_type","avg_glucose_level","bmi","smoking_status" )]
pos_stroke = subset(target, target$stroke >0)
length(rownames(pos_stroke))
df[df$gender=='Male']
