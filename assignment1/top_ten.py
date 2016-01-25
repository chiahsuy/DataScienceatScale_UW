import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def twtransfer(twtb, twfile):
		for line in twfile:
				tweet = json.loads(line)
				twtb.append(tweet)
				
def htscore(hstb,twtb):
		for twt in twtb:
				value = 0
				if 'entities' in twt.keys(): # deleted tweet will be shown with a zero
						twhash = twt['entities']['hashtags']
						if len(twhash)>=1:
								i=0
								while (i < len(twhash)):
										hstx = twhash[i]['text'].encode('utf-8')	
										if hstx in hstb.keys():
												hstb[hstx]+=1
										else:
												hstb[hstx]=1
										i+=1
			
		
def main():
    tweet_file = open(sys.argv[1])
    #out_file = open('top_ten_output.txt','w')
    #transfer tweet file
    tweets = []
    twtransfer(tweets,tweet_file)
    #count for each hashtag
    hashtags = {}
    htscore(hashtags,tweets)
    #print hashtags.items()
    #sort
    for key, value in sorted(hashtags.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:10]:
    		print "%s %.0f" %(key,value)
    		#out_file.write("%s %.0f" %(key,value))
    #close files    
    tweet_file.close()
    #out_file.close()
    

if __name__ == '__main__':
    main()
