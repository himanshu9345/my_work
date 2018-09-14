Required libraries

- Tweepy (pip install tweepy)
- NLTK (pip install nltk)
- NLTK Downloader (pip install nltk downloader)
- NLTK Stopwords
	Open python cmd and enter following cmds:
	1) import nltk
	2) nltk.download('stopwords')
-Leaflet (pip install leaflet)


To run successfully:
Open console in Code and run SentimentAnalyzer.py

python SentimentAnalyzer.py

Output will be two lists, first list contains words associated with positive sentiment and second list contains words with negative sentiment.


To change the topic, edit last two lines in Streaming.py, enter your topic on which you want to do sentiment analysis replacing 'demonetisation'.

After adding topic, run Streaming.py

Let it run for some time to collect data, it is possible that the file may not stop running on its own so manually exit from it by pressing Ctrl+C.

Then open file TermFrequencies.py
and instead of stream_deminetisation write - stream_[your topic]

Finally run SentimentAnalyzer.py

(This is just the experimental version, in future updates, this will be improved to provide the topic from console itself to save from this hassle.)