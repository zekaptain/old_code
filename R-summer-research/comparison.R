########## combine SD and Wynne testing pairs only into one file ##########
#clears all existing variables
rm(list=ls(all=TRUE))

#to add a column called "set" -- stores set #1 or #2
#loads required libraries
library(lme4)
library(lattice)
library(boot)
library(stats)
library(MASS)

#train pairs of all SD types

seqTrain<-read.csv("combined-train-sequential.txt")
simTrain<-read.csv("combined-train-simultaneous.txt")
seqTrain<-transform(seqTrain,TrainType = 0)
simTrain<-transform(simTrain,TrainType = 1)
write.csv(seqTrain,row.names=FALSE,file = "combined-train-sequential.txt")
write.csv(simTrain,row.names=FALSE,file = "combined-train-simultaneous.txt")

#set Set variable to NULL -- don't need it
seqTrain$Set<-NULL
simTrain$Set<-NULL

#combine files into one file
#states dimensions of the .csv files
dim(seqTrain)
dim(simTrain)
#creates a single file, combining these two
datafile<-rbind(seqTrain,simTrain)
#states dimensions of new file
dim(datafile)
#writes this new datafile out to a .txt file
write.csv(datafile,"combined-train.txt")

#############Training pair fit comparison###################
#fixed factors are outside of parentheses -- if 1,
#then no fixed factors
#random factors are inside parentheses -- 1|ID means no random
#factor
datafile<-read.csv("combined-train.txt")
datafile$TrainType<-as.factor(datafile$TrainType)
summary(datafile)

#these below say no fixed factor -- only look at random factors
myrA <-lmer(log(Residuals+0.00000000000001)~1+
              (1|ID), data=datafile)
myrB <-lmer(log(Residuals+0.00000000000001)~1+
              (TrainType|ID), data=datafile)
myrC <-lmer(log(Residuals+0.00000000000001)~1+
              (Pair|ID), data=datafile)
myrD <-lmer(log(Residuals+0.00000000000001)~1+
              (TrainType+Pair|ID), data=datafile)
myrE <-lmer(log(Residuals+0.00000000000001)~1+
              (TrainType*Pair|ID), data=datafile)
anova(myrA,myrB,myrC,myrD,myrE)
#I think myrB 

myr1 <-lmer(log(Residuals+0.00000000000001)~TrainType+Pair+
              TrainType:Pair+(TrainType|ID), data=datafile)
summary(myr1)
myr2 <-lmer(log(Residuals+0.00000000000001)~TrainType+Pair+
              (TrainType|ID), data=datafile)
summary(myr2)
myr3 <-lmer(log(Residuals+0.00000000000001)~TrainType+
              (TrainType|ID), data=datafile)
summary(myr3)
myr4 <-lmer(log(Residuals+0.00000000000001)~Pair+
              (TrainType|ID), data=datafile)
summary(myr4)
anova(myrB,myr1,myr2,myr3,myr4)

###Best model for training ##################
myr1 <-lmer(log(Residuals+0.00000000000001)~TrainType+Pair+
              TrainType:Pair+(TrainType|ID), data=datafile)
summary(myr1)

attach(datafile)
datafile$legend[TrainType==0]<-"Sequential"
datafile$legend[TrainType==1]<-"Simultaneous"
detach(datafile)

xyplot(fitted(myr1)~Pair|ID, group = legend, auto.key = TRUE,
       data=datafile)

#group effect of pair
#group effect of training: Simultaneous is fit better than 
#sequential which is the opposite of what we expect
#also interaction: some types of pairs are fit equivalently
#in both, some are different
#random interaction means that this is a bit different across 
#individuals


##########TESTING pair comparison##################
#test pairs of all SD types
#combines sequential 1 SD and simultaneous 1 SD TRAIN sets into one file
seqTest<-read.csv("combined-test-sequential.txt")
simTest<-read.csv("combined-test-simultaneous.txt")
seqTest<-transform(seqTest,TrainType = 0)
simTest<-transform(simTest,TrainType = 1)
write.csv(seqTest,row.names=FALSE,file = "combined-test-sequential.txt")
write.csv(simTest,row.names=FALSE,file = "combined-test-simultaneous.txt")

#set Set variable to NULL -- don't need it
seqTest$Set<-NULL
simTest$Set<-NULL

#combine files into one file
#states dimensions of the .csv files
dim(seqTest)
dim(simTest)
#creates a single file, combining these two
datafile2<-rbind(seqTest,simTest)
#states dimensions of new file
dim(datafile2)
#writes this new datafile out to a .txt file
write.csv(datafile2,"combined-test.txt")

datafile2<-read.csv("combined-test.txt")
summary(datafile2)
datafile2$TrainType<-as.factor(datafile2$TrainType)
datafile2$EACode<-as.factor(datafile2$EACode)
#these below say no fixed factor -- only look at random factors
myrA <-lmer(log(Residuals+0.00000000000001)~1+
              (EACode|ID), data=datafile2)
myrB <-lmer(log(Residuals+0.00000000000001)~1+
              (TrainType|ID), data=datafile2)
myrC <-lmer(log(Residuals+0.00000000000001)~1+
              (EACode+TrainType|ID), data=datafile2)
myrD <-lmer(log(Residuals+0.00000000000001)~1+
              (EACode*TrainType|ID), data=datafile2)
anova(myrA,myrB,myrC,myrD)
#I think myrD 

myr1 <-lmer(log(Residuals+0.00000000000001)~EACode+TrainType+
              EACode:TrainType+(EACode*TrainType|ID), data=datafile2)
summary(myr1)

myr2 <-lmer(log(Residuals+0.00000000000001)~EACode+(EACode*TrainType|ID), 
            data=datafile2)
summary(myr2)
myr3 <-lmer(log(Residuals+0.00000000000001)~EACode+TrainType+
              (EACode*TrainType|ID), 
            data=datafile2)
summary(myr3)
myr4 <-lmer(log(Residuals+0.00000000000001)~TrainType+
              (EACode*TrainType|ID), data=datafile2)
summary(myr4)
anova(myr1, myr2,myr3,myr4)
####Best model for testing data######
myr4 <-lmer(log(Residuals+0.00000000000001)~TrainType+
              (EACode*TrainType|ID), data=datafile2)
summary(myr4)

attach(datafile2)
datafile2$legend[TrainType==0]<-"Sequential"
datafile2$legend[TrainType==1]<-"Simultaneous"
detach(datafile2)

attach(datafile2)
datafile2$EndAnchor<-as.character(datafile2$EndAnchor)
datafile2$EA[EndAnchor=="EA1"]<-"G"
datafile2$EA[EndAnchor=="EA2"]<-"A"
datafile2$EA[EndAnchor=="I"]<-"Inner"
detach(datafile2)
datafile2$EndAnchor<-as.factor(datafile2$EndAnchor)

xyplot(fitted(myr1)~EACode|ID, group = legend, auto.key = TRUE,
       data=datafile2)
#the only group effect is train type: simultaneous is predicted 
#less reliably than sequential. as we would expect
#no reliable diff for EACode