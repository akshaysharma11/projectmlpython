import pandas as pd
import matplotlib.pyplot as plt
df=""



def strtofloat(str):
    newstr=[]
    for i in df[str]:
        i=i.strip("*")
        if(i=="-"):
            newstr.append(0)
        else:
            newstr.append(float(i))
    return newstr

def playedMatches(x):
    player=df['Player'].values
    century=strtofloat("Inns")
    fig=plt.figure(figsize=(10,8))
    plt.bar(player[0:x],century[0:x])
    plt.xlabel("player's name")
    plt.ylabel("Inns Count ")
    fig.autofmt_xdate()
    plt.show()

def goldenduck(x):
    player=df['Player'].values
    century=strtofloat("0")
    fig=plt.figure(figsize=(10,8))
    plt.bar(player[0:x],century[0:x])
    plt.xlabel("player's name")
    plt.ylabel("GoldenDuck Count ")
    fig.autofmt_xdate()
    plt.show()

def HS(x):
    player=df['Player'].values
    century=strtofloat("HS")
    fig=plt.figure(figsize=(10,8))
    plt.bar(player[0:x],century[0:x])
    plt.xlabel("player's name")
    plt.ylabel("Highest Score ")
    fig.autofmt_xdate()
    plt.show()

def fifty(x):
    player=df['Player'].values
    century=strtofloat("50")
    fig=plt.figure(figsize=(10,8))
    plt.bar(player[0:x],century[0:x])
    plt.xlabel("player's name")
    plt.ylabel("Fifties ")
    fig.autofmt_xdate()
    plt.show()

# no players data in histogram
def hundreds(x):
    player=df['Player'].values
    century=strtofloat("100")
    fig=plt.figure(figsize=(10,8))
    plt.bar(player[0:x],century[0:x])
    plt.xlabel("player's name")
    plt.ylabel("Hundreds")
    fig.autofmt_xdate()
    plt.show()

#no player's average
def average(x):
    player=df['Player']
    fig=plt.figure(figsize=(10,8))
    avg=strtofloat("Ave")
    plt.bar(player[0:x],avg[0:x],width=0.3)
    plt.xlabel("player's name")
    plt.ylabel("Average Runs")
    fig.autofmt_xdate()
    plt.show()

def strikeRate(x):
    player=df['Player']
    fig=plt.figure(figsize=(10,8))
    avg=strtofloat("SR")
    plt.bar(player[0:x],avg[0:x],width=0.3)
    plt.xlabel("player's name")
    plt.ylabel("Strike Rate")
    fig.autofmt_xdate()
    plt.show()

def choices():
    print("1 for hundred")
    print("2 for average")
    print("3 for fifty")
    print("4 for Strike rate")
    print("5 for Highest Score")
    print("6 for Golden duck count")
    print("7 for Innings count")
    i=int(input())
    x=int(input("enter the no of players"))
    if(i==1):
        hundreds(x)
    elif(i==2):
        average(x)
    elif(i==3):
        fifty(x)
    elif(i==4):
        strikeRate(x)
    elif(i==5):
        HS(x)
    elif(i==6):
        goldenduck(x)
    elif(i==7):
        playedMatches(x)
    else:
        print("correct the option")


while(True):
    print("1 for test format\n2 for t20 format\n3 for ODI format")
    i=int(input())
    if(i==1):
        df=pd.read_csv("test.csv")
        choices()
    elif(i==2):
        df=pd.read_csv("t20.csv")
        choices()
    elif(i==3):
        df=pd.read_csv("ODI.csv")
        choices()
    else:
        print("choose something correct")
    
    
