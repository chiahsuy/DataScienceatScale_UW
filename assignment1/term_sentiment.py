import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def bdscoretb(score_tb,afinnfile):
		for line in afinnfile:
  			term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  		score_tb[term] = float(score)  # Convert the score to an integer.

def twtransfer(twtb, twfile):
		for line in twfile:
				tweet = json.loads(line)
				twtb.append(tweet)
				
def twscore(sctb,twtxt):
		value = 0
		text = twtxt.split()
		for tx in text:
				if tx in sctb.keys():
						value = value + sctb[tx] # text not in the dictonary will be counted as a zero
		return value
				
def deducescore(sctb,twtb,txtb):
		for twt in twtb:
				if 'text' in twt.keys(): # deleted tweet will be shown with a zero
						twtext = twt['text'].encode('utf-8')	
						text = twtext.split()
						for tx in text:
								if tx.isalnum(): # term cannot contain any special symbols
										if tx not in sctb.keys():
												if tx in txtb.keys():
														txtb[tx]=((txtb[tx]+twscore(sctb,twtext))/2)
												else:
														txtb[tx]=twscore(sctb,twtext)
										

def main():
		aff_file = open(sys.argv[1])
		tweet_file = open(sys.argv[2])
		#out_file = open('term_sentiment_output.txt','w')
		#build score table from aff_file
		scores = {} # initialize an empty dictionary
		bdscoretb(scores,aff_file)
		#print scores.items()
		#transfer tweet file
		tweets = []
		twtransfer(tweets,tweet_file)
		texts = {}
		deducescore(scores,tweets,texts)
		for tx in texts:
				print '%s %.2f' %(tx,texts[tx])
				#out_file.write('%s %.2f\n' %(tx,texts[tx]))
    #close files
		aff_file.close()
		tweet_file.close()
		#out_file.close()
   

if __name__ == '__main__':
    main()
