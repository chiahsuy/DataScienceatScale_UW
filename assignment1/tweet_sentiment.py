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
				
#def twscore(sctb,twtb,outfile):
		#for twt in twtb:
				#value = 0
				#if 'text' in twt.keys():
						#twtext = twt['text'].encode('utf-8')	
						#text = twtext.split()
						#for tx in text:
								#if tx in sctb.keys():
										#value = value + sctb[tx]
				#outfile.write('%d\n' % value)
def twscore(sctb,twtb):
		for twt in twtb:
				value = 0
				if 'text' in twt.keys(): # deleted tweet will be shown with a zero
						twtext = twt['text'].encode('utf-8')	
						text = twtext.split()
						for tx in text:
								if tx in sctb.keys():
										value = value + sctb[tx] # text not in the dictonary will be counted as a zero
				print('%d' % value)				
		
def main():
    aff_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #out_file = open('tweet_sentiment_output.txt','w')
    #build score table from aff_file
    scores = {} # initialize an empty dictionary
    bdscoretb(scores,aff_file)
    #print scores.items()
    #transfer tweet file
    tweets = []
    twtransfer(tweets,tweet_file)
    #caculate score for each tweet and write into the output file
    #twscore(scores,tweets,out_file)
    twscore(scores,tweets)
    #close files    
    aff_file.close()
    tweet_file.close()
    #out_file.close()
    

if __name__ == '__main__':
    main()
