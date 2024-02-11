import numpy as np
from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

def load_reviews(text):
    with open(text, 'r') as file:
        return file.read()

def get_previous_weekday(date):
    while date.weekday() > 4:  # Monday to Friday are considered weekdays (0 to 4)
        date -= timedelta(days=1)
    return date

def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = []
    in_text = seed_text
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        yhat = model.predict_classes(encoded, verbose=0)
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)

def ask_user():
    ratings = ['One', 'Two', 'Three', 'Four', 'Five']
    
    while True:
        rating = input("What rating do you want to generate a review for? \nPlease enter 'One', 'Two', 'Three', 'Four', 'Five'\n\n").title()
        
        if rating not in ratings:
            print("Invalid rating. Please enter a valid rating.")
            continue

        doc = load_reviews(f'../NLP/{rating}_Star.txt')
        lines = doc.split('\n')
        seq_length = len(lines[0].split()) - 1
        model = load_model(f'Models/model_{rating.lower()}_star.h5')
        tokenizer = load(open(f'Models/tokenizer_{rating.lower()}_star.pkl', 'rb'))
        
        words = int(input(f'\nHow many words would you like your {rating} star review to be?\n\n'))
        seed_text = lines[randint(0, len(lines))]
        generated = generate_seq(model, tokenizer, seq_length, seed_text, words)
        
        print(f'Seed text to generate {rating} star review: {seed_text}')
        print(generated)
        break

if __name__ == "__main__":
    ask_user()
