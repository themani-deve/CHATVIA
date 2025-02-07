import joblib

model = joblib.load('Comprehenc.pkl')
vectorizer = joblib.load('vectorizer.pkl')


def process_pos_nev(text):
    vectorize = vectorizer.transform([text]).toarray()
    y_pred = model.predict(vectorize)
    if y_pred == 0:
        y_pred_to_str = 'Negative'
    else:
        y_pred_to_str = 'Positive'
    return y_pred_to_str
