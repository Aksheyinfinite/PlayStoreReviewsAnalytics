from google_play_scraper import Sort, reviews,reviews_all
from google_play_scraper import app
import pandas as pd

def review_scrapper(app="com.tatasky.binge",destinationReviewFile="reviews.csv"):
	result=reviews_all(app)
	reviewId,userName,userImage,content,score,thumbsUpCount,reviewCreatedVersion,timestamp=[],[],[],[],[],[],[],[]
	reviewsDataFrame=pd.DataFrame()
	for i in result:
    		reviewId.append(i["reviewId"])
    		userName.append(i["userName"])
    		userImage.append(i["userImage"])
    		content.append(i["content"])
    		score.append(i["score"])
    		thumbsUpCount.append(i["thumbsUpCount"])
    		reviewCreatedVersion.append(i["reviewCreatedVersion"])
    		timestamp.append(i["at"])
	reviewsDataFrame["reviewID"]=reviewId
	reviewsDataFrame["userName"]=userName
	reviewsDataFrame["userImage"]=userImage
	reviewsDataFrame["content"]=content
	reviewsDataFrame["score"]=score
	reviewsDataFrame["thumbsUpCount"]=thumbsUpCount
	reviewsDataFrame["reviewCreatedVersion"]=reviewCreatedVersion
	reviewsDataFrame["timestamp"]=timestamp
	reviewsDataFrame.to_csv(destinationReviewFile,index=False)
review_scrapper("com.tatasky.binge",destinationReviewFile="test.csv")

