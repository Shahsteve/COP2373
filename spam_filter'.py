# Created keywords to look for for spam
keywords = ["billion", "miracle", "prize", "satisfaction", "promotion", "lifetime", "money",
            "highest", "lowest", "exclusive", "instant", "limited", "urgent", "winner", "winning", "selected",
            "unbelievable", "only", "action", "member", "emergency", "apply", "promise", "earnings", "income",
            "pennies", "risk", "profit", "traffic", "trial", "miracle"]

# Asks user for entry
text = input('Enter message here: ')


# Function counts, scores, and prints the output for spam
def spam_score(text):
    wordcount = 0
    found_keywords = []
    words = text.strip().lower().split(" ")
    for word in words:
        if word in keywords:
            wordcount += 1
            found_keywords.append(word)

    # This is formula I used to create the rate of likelihood for spam message
    rate = wordcount / 30 * 100

    if rate > 9:

        print(f"We found, {wordcount} words flagged as spam keywords. {rate}% chance of being spam. "
              f"{found_keywords} found")
    else:

        print(f"We did not find enough to label as spam")


# call function
spam_score(text)
