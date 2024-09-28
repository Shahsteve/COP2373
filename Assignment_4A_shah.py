import time

def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Function took {end_time - start_time:.5f} seconds to execute")

        return result

    return wrapper
# Created keywords to look for for spam
keywords = ["billion", "miracle", "prize", "satisfaction", "promotion", "lifetime", "money",
            "highest", "lowest", "exclusive", "instant", "limited", "urgent", "winner", "winning", "selected",
            "unbelievable", "only", "action", "member", "emergency", "apply", "promise", "earnings", "income",
            "pennies", "risk", "profit", "traffic", "trial", "miracle"]

# Asks user for entry
text = input('Enter message here: ')

@measure_time

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

    time.sleep(5)
    if rate > 9:

        print(f"We found, {wordcount} words flagged as spam keywords. {rate}% chance of being spam. "
              f"{found_keywords} found")
    else:

        print(f"We did not find enough to label as spam")


# call function
spam_score(text)
