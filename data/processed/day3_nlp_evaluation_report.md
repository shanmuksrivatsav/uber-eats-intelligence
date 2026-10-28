# Day 3 — NLP Sentiment Analysis Report

- Reviews analyzed: 7000
- Review text column: `review_text`
- Rating column: `review_rating`
- Existing label column: `sentiment_label`
- NLTK lemmatization available: False
- VADER available: True

## Sentiment label distribution
sentiment_label
negative    2373
positive    2353
neutral     2274

## Naive Bayes evaluation
- Accuracy: 1.0000
- Macro precision: 1.0000
- Macro recall: 1.0000
- Macro F1-score: 1.0000

```text
              precision    recall  f1-score   support

    negative       1.00      1.00      1.00       593
     neutral       1.00      1.00      1.00       569
    positive       1.00      1.00      1.00       588

    accuracy                           1.00      1750
   macro avg       1.00      1.00      1.00      1750
weighted avg       1.00      1.00      1.00      1750

```

## VADER sentiment distribution
vader_sentiment
positive    3846
negative    2377
neutral      777

## Interpretation notes
- Sentiment labels derived from ratings are proxy labels, not human-annotated sentiment.
- TF-IDF terms and complaint keywords require manual contextual review.
- The data is synthetic and does not establish real-world Uber Eats customer behavior.
