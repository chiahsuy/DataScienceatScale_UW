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

def countterms(twtb,txctb,all):
		for twt in twtb:
				if 'text' in twt.keys(): # deleted tweet will be shown with a zero
						twtext = twt['text'].encode('utf-8')	
						text = twtext.split()
						for tx in text:
								if tx.isalnum(): # term cannot contain any special symbols
										all += 1
										if tx in txctb.keys():
												txctb[tx]+=1
										else:
												txctb[tx]=1
		return all
					
def freq(txctb,total,txftb):
		for tx in txctb.keys():
				txftb[tx] = float(txctb[tx])/float(total)


def main():
		tweet_file = open(sys.argv[1])
		#out_file = open('freq_output.txt','w')
		#transfer tweet file
		tweets = []
		twtransfer(tweets,tweet_file)
		total = 0
		counts = {}
		total= countterms(tweets,counts,total)
		freqs = {}
		freq(counts,total,freqs)
		for tx in freqs:
				print '%s %.6f' %(tx,freqs[tx])
				#out_file.write('%s %.6f\n' %(tx,freqs[tx]))
    #close files
		tweet_file.close()
		#out_file.close()

if __name__ == '__main__':
    main()
