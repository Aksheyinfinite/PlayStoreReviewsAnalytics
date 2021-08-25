import pandas as pd
from bertopic import BERTopic
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import os

# -------------------------- Preprocessing ----------------------------------
os.mkdir("Visual_Outputs")
reviewsDataFrame=pd.read_csv("reviews.csv")  # Reading the Scrapped Reviews File
reviewsDataFrame=reviewsDataFrame[reviewsDataFrame.score<=3] #Segregation of reviews by rating
content=reviewsDataFrame.content.values  # Extracting Text Reviews After Rating Filteration
def deEmojify(inputString):   # Help Us Filtering Hindi Text, Emoji, Icons
    return inputString.encode('ascii', 'ignore').decode('ascii')
content=[deEmojify(i) for i in content]


# ---------------------------Model Initialisation & Fiting -----------------------------
topic_model = BERTopic(n_gram_range=(2,4),top_n_words=20) #Defining Object of a Deeplearning Based Transformer Model 
topics, probs = topic_model.fit_transform(content) # Fiting Cleaned Text Reviews Into Our NLP Model


#-------------------------Topic Exploration------------------------------------------
print(topic_model.get_topic_info()) # Will List Number Of Reviews 
print(topic_model.get_topic(7)) # 7 Is a parameter which we used to dig deeper into topic number 7


#--------------------------Visual Exploration & Saving to ./Visual_Outputs/*.html  ------------------------------------------
topicDistance=topic_model.visualize_topics() 
timestamps = reviewsDataFrame.timestamp.to_list()
topics_over_time = topic_model.topics_over_time(content, topics, timestamps, nr_bins=20)
topicOverTime=topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=8)
topicBarChart=topic_model.visualize_barchart(top_n_topics=8,n_words=15,width=1400,height=1000)
hirarchicalSegmentation=topic_model.visualize_hierarchy()
topicsHeatmap=topic_model.visualize_heatmap()
topicRank=topic_model.visualize_term_rank()



#Saving Interactive Findings As Graph
topicDistance.write_html("Visual_Outputs/InterTopicsDistance.html") 
topicOverTime.write_html("Visual_Outputs/TopicsTrendOverTime.html")
topicBarChart.write_html("Visual_Outputs/TopicsBarChart.html")
hirarchicalSegmentation.write_html("Visual_Outputs/hirarchicalSegmentation.html")
topicsHeatmap.write_html("Visual_Outputs/topicsHeatmap.html")
topicRank.write_html("Visual_Outputs/topicRank.html")