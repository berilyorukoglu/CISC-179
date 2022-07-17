from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()

    text = "You p1ec3 of sHit."
    censored_text = profanity.censor(text)
    print(censored_text)
    # You **** of **