from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import LinearSVC

from extractors.LexiconExtractor import LexiconExtractor
from extractors.PartsOfSpeechExtractor import PartsOfSpeechExtractor
from extractors.SentimentSymbolExtractor import SentimentSymbolExtractor
from util.Preprocessor import Preprocessor
from extractors.TwitterExtractor import TwitterExtractor
from baseline_model import read_corpus

message_train, label_train = read_corpus("datasets/train_dataset_30.csv")
message_test, label_test = read_corpus("datasets/test_dataset_30.csv")

preprocessor = Preprocessor(tweet_elements='normalize', stemming=False).preprocess

pipeline = Pipeline([
    ('feats', FeatureUnion([
        ('vect', TfidfVectorizer(use_idf=False,
                                 preprocessor=preprocessor)),
        #('sentiment_symbol', SentimentSymbolExtractor()),
        #('parts_of_speech', PartsOfSpeechExtractor()),
        #('lexicon', LexiconExtractor()),
        #('twitter', TwitterExtractor())
    ])),
    ('clf', LinearSVC())
])


l = 1000

pipeline.fit(message_train[:l], label_train[:l])

y_prediction = pipeline.predict( message_test[:l] )

report = classification_report( label_test[:l], y_prediction )

print(report)
print(accuracy_score(label_test[:l], y_prediction))