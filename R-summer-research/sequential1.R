##############Setup#######################
#clears all existing variables
rm(list=ls(all=TRUE))

#loads required libraries
library(lme4)
library(lattice)
library(boot)
library(stats)
library(MASS)

############Sequential 1 Wynne data file#####################
#read the file--select the correct file
#remember to move to the correct directory
mydata<-read.csv("sequential1-wynne.txt")
summary(mydata)

#mydata$Residuals<-log(mydata$Residuals+0.0000000001)

#plot residuals against obtained data using different transformation
xyplot(Residuals~Obtained|ID, data=mydata, type="a", auto.key=T)
xyplot(log(Residuals+0.00000000000001)~Obtained, data=mydata, type="a", auto.key=T)
xyplot(2*sinh(sqrt(mydata$Residuals))~Obtained|ID, data=mydata, type="a", auto.key=T)

#check residuals against end-anchor. EA1 is A (first end-anchor), EA is G
xyplot(Residuals~EndAnchor|ID, data=mydata, type="a", auto.key=T)

#############End-anchor residual comparison#######################
myr1<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(1|ID), data=mydata)
summary(myr1)
anova(myr1)
xyplot(fitted(myr1)~EndAnchor|ID, data=mydata, type="a", auto.key=T)

myr2<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(EndAnchor|ID), data=mydata)
summary(myr2)
anova(myr1,myr2)
xyplot(fitted(myr2)~EndAnchor, data=mydata, type="a", auto.key=T)

#Tasks for future.
#3) Directly compare successive 1 and 2 (can we pool 2 sets?) If yes, then
#dataset
#myr<-lmer(log(Residuals+0.00000000000001)~dataset+(dataset|ID), data=mydata)
#1) Re-run end anchor analysis on pooled data
#2) Run the same analysis on symbolic distance
#basically on the data where SD is non-existent
#mydata1<- mydata[mydata[, 'SD'] != NA,]
#mydata1<- mydata[mydata[, 'dataset'] == 1,]

#to add a column called "set" -- stores set #1 or #2
#sequential 1
wynneData<-read.csv("sequential1-wynne.txt")
wynneData<-transform(wynneData,Set = 1)
write.csv(wynneData,row.names=FALSE,file = "sequential1-wynne.txt")

#sequential 2
wynneData2<-read.csv("sequential2-wynne.txt")
wynneData2<-transform(wynneData2,Set = 2)
write.csv(wynneData2,row.names=FALSE,file = "sequential2-wynne.txt")

#combine files into one file
#states dimensions of the .csv files
dim(wynneData)
dim(wynneData2)
#creates a single file, combining these two
datafile<-rbind(wynneData,wynneData2)
#states dimensions of new file
dim(datafile)
#writes this new datafile out to a .txt file
write.csv(datafile,"combined-sequential-wynne.txt")

#############End-anchor residual comparison for Wynne#######################
#for the pooled dataset
myr1<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(1|ID), data=datafile)
summary(myr1)
anova(myr1)
xyplot(fitted(myr1)~EndAnchor|ID, data=datafile, type="a", auto.key=T)

myr2<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(EndAnchor|ID), data=datafile)
summary(myr2)
anova(myr1,myr2)
xyplot(fitted(myr2)~EndAnchor|ID, data=datafile, type="a", auto.key=T)

datafile$Set<-as.factor(datafile$Set)

myr3<-lmer(log(Residuals+0.00000000000001)~EndAnchor+Set+
             Set:EndAnchor+(EndAnchor|ID), data=datafile)
summary(myr3)
anova(myr2,myr3)
xyplot(fitted(myr3)~EndAnchor, group=Set, data=datafile, type="a", auto.key=T)

########Best model for end-anchor comparison for Wynne##############
myr2<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(EndAnchor|ID), data=datafile)
summary(myr2)
xyplot(fitted(myr2)~EndAnchor|ID, data=datafile, type="a", auto.key=T)

#########Symbolic distance ###############################
#delete any monkey with SD of NA in each set -- still pooled
datafile1<-datafile[!is.na(datafile$SD),]

#check for set (see if set makes any difference)
datafile1$Set<-as.factor(datafile1$Set)

myr3<-lmer(log(Residuals+0.00000000000001)~EndAnchor+Set+
             Set:EndAnchor+(EndAnchor|ID), data=datafile1)
summary(myr3)
anova(myr2,myr3)
xyplot(fitted(myr3)~EndAnchor, group=Set, data=datafile1, type="a", auto.key=T)
####### won't let me b/c only EndAnchor is I, no EA1 or EA2 ########
####### thus, wind up with 1 factor, not 2 or more ########



##################do the same as above for Seimann-Delius###########
#clears all existing variables
rm(list=ls(all=TRUE))

#to add a column called "set" -- stores set #1 or #2
#sequential 1
sdData<-read.csv("sequential1-siemannDelius.txt")
sdData<-transform(sdData,Set = 1)
write.csv(sdData,row.names=FALSE,file = "sequential1-siemannDelius.txt")

#sequential 2
sdData2<-read.csv("sequential2-siemannDelius.txt")
sdData2<-transform(sdData2,Set = 2)
write.csv(sdData2,row.names=FALSE,file = "sequential2-siemannDelius.txt")

#combine files into one file
#states dimensions of the .csv files
dim(sdData)
dim(sdData2)
#creates a single file, combining these two
datafile<-rbind(sdData,sdData2)
#states dimensions of new file
dim(datafile)
#writes this new datafile out to a .txt file
write.csv(datafile,"combined-sequential-sd.txt")

#############End-anchor residual comparison for SD#######################
#for the pooled dataset
myr1<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(1|ID), data=datafile)
summary(myr1)
anova(myr1)
xyplot(fitted(myr1)~EndAnchor|ID, data=datafile, type="a", auto.key=T)

myr2<-lmer(log(Residuals+0.00000000000001)~EndAnchor+(EndAnchor|ID), data=datafile)
summary(myr2)
anova(myr1,myr2)
xyplot(fitted(myr2)~EndAnchor|ID, data=datafile, type="a", auto.key=T)

datafile$Set<-as.factor(datafile$Set)

myr3<-lmer(log(Residuals+0.00000000000001)~EndAnchor+Set+
             Set:EndAnchor+(EndAnchor|ID), data=datafile)
summary(myr3)
anova(myr2,myr3)
xyplot(fitted(myr3)~EndAnchor|ID, group=Set, data=datafile, type="a", auto.key=T)

#exploring random factor structure
#fixed factors are outside of parentheses -- if 1,
#then no fixed factors
#random factors are inside parentheses -- 1|ID means no random
#factor
myrA <-lmer(log(Residuals+0.00000000000001)~1+
              (EndAnchor|ID), data=datafile)
myrB <-lmer(log(Residuals+0.00000000000001)~1+
              (Set|ID), data=datafile)
myrC <-lmer(log(Residuals+0.00000000000001)~1+
              (EndAnchor+Set|ID), data=datafile)
myrD <-lmer(log(Residuals+0.00000000000001)~1+
              (EndAnchor*Set|ID), data=datafile)
anova(myrA,myrB,myrC,myrD)

########Does Symbolic Distance factor in S-D?? ########
datafile1<-datafile[!is.na(datafile$SD),]
#same as Wynne -- only Inner pairs have SD
