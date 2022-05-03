#Python code for finding the Cosine similarity using sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
doc1="Deep Learning Can be Hard"
doc2="Deep Learning Can be simple"
documents=[doc1,doc2]
#convert given documents into vectoried form
count_vectorizer=CountVectorizer()
res=count_vectorizer.fit_transform(documents)
#it returns matrix and stored in rs
rs=res.todense()
df=pd.DataFrame(rs,columns=count_vectorizer.get_feature_names(),index=['doc1','doc2'])
print(df)
print("Cosine Similarity:",cosine_similarity(df))
