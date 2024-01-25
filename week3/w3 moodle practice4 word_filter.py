import re
from collections import Counter

def word_filter_counter(text, filter_words):
    # Convert filter words to lowercase for case-insensitive comparison
    filter_words_lower = [word.lower() for word in filter_words]

    # Use regular expression to find all words in the text
    words = re.findall(r'\b\w+\b', text.lower())

    # Filter out words present in filter_words list
    filtered_words = [word for word in words if word in filter_words_lower]

    # Count occurrences of each filtered word
    word_counts = Counter(filtered_words)

    return dict(word_counts)

# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
print(
    word_filter_counter("I want money.",["money"]))
    
