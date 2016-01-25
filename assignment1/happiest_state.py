import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def bdscoretb(score_tb,afinnfile):
		for line in afinnfile:
  			term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  		score_tb[term] = int(score)  # Convert the score to an integer.

def twtransfer(twtb, twfile):
		for line in twfile:
				tweet = json.loads(line)
				twtb.append(tweet)
				

def sthappy(sctb,twtb,stlist,sttb):
		for twt in twtb:
				value = 0
				if 'text' in twt.keys(): # deleted tweet will be shown with a zero
						twtext = twt['text'].encode('utf-8')	
						text = twtext.split()
						for tx in text:
								if tx in sctb.keys():
										value = value + sctb[tx] # text not in the dictonary will be counted as a zero
						loc=twt['user']['location']
						if (loc):
								loc_st=loc.split()
								if len(loc_st)>1:
										st=loc_st[len(loc_st)-1]
										st=st.encode('utf-8')
										if (st.isalnum() and len(st)==2):
												st=st.upper()
												if st in stlist.keys():
														if st in sttb.keys():
																sttb[st]+=value
														else:
																sttb[st]=value
		
		
def main():
    aff_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #out_file = open('tweet_sentiment_output.txt','w')
    states = {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut','DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MP': 'Northern Mariana Islands','MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina','ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}
    #print states.keys()
    #build score table from aff_file
    scores = {} # initialize an empty dictionary
    bdscoretb(scores,aff_file)
    #print scores.items()
    #transfer tweet file
    tweets = []
    twtransfer(tweets,tweet_file)
    #caculate score for each tweet and write into the output file
    #twscore(scores,tweets,out_file)
    st_happys = {}
    sthappy(scores,tweets,states,st_happys)
    #sort
    for key, value in sorted(st_happys.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:1]:
    		#print "%s %.0f" %(key,value)
    		print "%s" % (key)
    
    #print st_happys.items()
    #close files    
    aff_file.close()
    tweet_file.close()
    #out_file.close()
    

if __name__ == '__main__':
    main()
