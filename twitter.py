import twint
import asyncio
import sys
import pandas as pd
import time
#pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
# ^ proper twint install
#config = twint.Config()
#config.Since="2019-11-01"
#config.Hide_outpt = True
#config.Store_object= True
#config.Limit = sys.maxsize
#config.Search = "covid"
#config.Store_csv = True
#config.Output = "covid1.csv"
#twint.run.Search(config)
Still_Going = True
BIGFNAME = "covidAll1.csv"
def getAllCovid():
    config = twint.Config()
    config.Hide_output = True
    config.Since = "2019-11-01"
    config.Store_object = True
    config.Limit = 10000000
    config.Search = "covid"
    config.Store_csv = True
    config.Output = BIGFNAME
    asyncio.new_event_loop(twint.run.Search(config))
    Still_Going = False


def sampler(fname):
    LastInt = -1
    while(Still_Going):
        f = pd.read_csv(fname)
        if(LastInt == len(f)):
            break
        print(str(len(f)) + f['tweet'].get(len(f)-1))
        LastInt = len(f)
        time.sleep(3)


def getTweets(topic=None, limit=100, fname=None, verbose=False):
    topic = topic
    limit = limit
    fname = fname
    if(topic == None):
        raise Exception("No Topic Provided")
    if(fname == None):
        raise Exception("No Filename Provided")
    c = twint.Config()
    c.since = "2019-1-1"
    c.Search = [topic]
    c.Limit = limit
    if verbose == False:
        c.Hide_output = True
    else:
        c.Hide_output = False
#maybe change later to allow for different output formats
    c.Store_csv = True


    c.Output = fname
    twint.run.Search(c)

def tweetsByDate(since="2019-12-20", until="2019-12-20", topic=None, limit = None, fname = None):
    if(topic == None):
        raise Exception("No Topic Provided")
    if(fname == None):
        raise Exception("No Filename Provided")
    c = twint.Config()
    c.Since = since
    c.Until = until
    c.Limit = limit
    c.Search = [topic]
    c.Hide_output = False
    c.Store_csv = True
    c.Output = fname
    twint.run.Search(c)
#getAllCovid()

#twint.run.Search(c)
#prints all in english
def printTweets(fname):

    df = pd.read_csv(fname)

    for i in range(0, int(len(df))):
        if(df['language'].get(i).__eq__("en")):
            print(str(i) + " " + df['date'].get(i) + " "+  df['tweet'].get(i) + "\n")

#printTweets("covidAll.csv")
