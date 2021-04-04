# Twitter_Chatbot
Chat bot that answers simple questions trained with a database of tweets

The used data has been obtained from The Customer Support on Twitter database.
https://www.kaggle.com/thoughtvector/customer-support-on-twitter

**Features:**

**tweet_id :** A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.
**author_id :** A unique, anonymized user ID. @s in the dataset have been replaced with their associated anonymized user ID.
**inbound :** Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing data for training conversational models.
**created_at :** Date and time when the tweet was sent.
**text :** Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like __email__.
**response_tweet_id :** IDs of tweets that are responses to this tweet, comma-separated.
**in_response_to_tweet_id :** ID of the tweet this tweet is in response to, if any.
