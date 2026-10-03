def clean_words(sentence ):
    # Step 1: lowercase the whole sentence
    sentence = sentence.lower()

    # Step 2: remove punctuation, character by character
    punctuation = ".,!?;:'\"()"
    cleaned = ""
    for char in sentence:
        if char in punctuation:
            pass  # skip it — don't add it to cleaned
        else:
            cleaned += char  # keep it

    # Step 3: split the cleaned sentence into a list of words
    words = []
    current_word = ""
    for char in cleaned:
        if char == " ":
            if current_word != "":  # avoid adding empty words (e.g. double spaces)
                words.append(current_word)
            current_word = ""
        else:
            current_word += char

    # catch the last word, no trailing space to trigger the save
    if current_word != "":
        words.append(current_word)

    return words

#---The word_frequency method---#
def word_frequency(words):
    freq = {}   # empty dictionary to start
    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq

#--The unique_words method--#

#** OPTION-A with shortcut**#
def unique_words(words):
    return set(words)

#** Option-B with loop **#
#def unique_words(words):
    unique = set()
    for word in words:
        if word not in unique:
            unique.add(word)
    return unique


# --- outer step: split paragraph into sentences ---#
paragraph = "The quick brown fox jumps over the lazy dog. The dog barks loudly at the fox. A beautiful garden lies beyond the fence."
sentences = []
current_sentence = ""

for char in paragraph:
    if char == ".":
        sentences.append(current_sentence.strip())
        current_sentence = ""
    else:
        current_sentence += char

# remove trailing empty string
sentences = [s for s in sentences if s != ""]

# --- call clean_words on each sentence ---
all_cleaned = []
for s in sentences:
    all_cleaned.append(clean_words(s))

print("---The different words in the list are---\n")
print(all_cleaned)

test_words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog','the',
              'dog', 'barks', 'loudly', 'at', 'the', 'fox',
              'a', 'beautiful', 'garden', 'lies', 'beyond', 'the', 'fence']
result = word_frequency(test_words)
print("\n---The frequency of each word is\n")
print(result)

 # call the unique_words function
all_words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog','the',
              'dog', 'barks', 'loudly', 'at', 'the', 'fox',
              'a', 'beautiful', 'garden', 'lies', 'beyond', 'the', 'fence']
UniqueWords = unique_words(all_words)
print("\n---The unique words set---\n")
print(UniqueWords)
