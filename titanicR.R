#Question6
data <- read.csv(file="titanic.csv", head=TRUE, sep=",")
print(data)
summary(data)

#Question7
data <- read.csv(file="titanic.csv", head=TRUE, sep=",")
names(data)
data$PassengerId
data$Survived
table(data$Sex)

#Question8
#The proportion of men and women who survived is man: 32%, woman: 68%
#The probability that if someone was a women, for about 74% they will survive the crash
#The probability that if someone was a man, for about 19% they will survive the crash
prop.table(table(data$Sex, data$Survived), 2)
prop.table(table(data$Sex, data$Survived), 1)

#Question9
#For total number of passengers: 12% male survived and 26% female survived
#For total number of survivors: 32% of survivors were male and 68% of survivors were female
#For total number of children: 54% of children survived
#For total number of adults: 34% of adults survived
#So we can see the old naval cliche of "women and children first" impacted survival.
table(data$Sex, data$Survived)
data$IsChild <- 0
data$IsChild[data$Age < 18] <- 1
data$IsChild
aggregate(Survived ~ Sex + IsChild, data=data, FUN=length)
aggregate(Survived ~ Sex + IsChild, data=data, FUN=sum)
table(data$Sex)
table(data$Sex, data$Survived)
