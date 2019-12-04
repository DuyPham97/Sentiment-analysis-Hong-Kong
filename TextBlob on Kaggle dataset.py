#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
fields = ['target', 'text']

#Read dataset
Kaggle = pd.read_csv ('Kaggle dataset.csv', encoding = 'ISO-8859-1', names=DATASET_COLUMNS, usecols = fields)
Kaggle.head(5)

def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

# Remove URLs
Kaggle.text = [remove_url(text) for text in Kaggle.text]

# Processing textual data using textblob
sentiment_objects = [TextBlob(text) for text in Kaggle.text]

# Create list of polarity valuesx and tweet text
sentiment_values = [[text.sentiment.polarity, str(text)] for text in sentiment_objects]

# Create dataframe containing the polarity value and tweet text
Kaggle_sentiment['target'] = Kaggle['target'].copy()
Kaggle_sentiment['polarity_rounding'] = 4
Kaggle_sentiment['polarity_rounding'][Kaggle_sentiment['polarity'] < 0] = 0

print (classification_report(Kaggle_sentiment['target'], Kaggle_sentiment['polarity_rounding']))
print ('Accuracy:', accuracy_score (Kaggle_sentiment['target'], Kaggle_sentiment['polarity_rounding']))

