import string
from collections import Counter

def remove_stop_words(text):
    stop_words = ["the", "and", "is", "in", "to", "of", "a", "it"]
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_words(text):
    words = remove_stop_words(text)
    word_counts = Counter(words)
    return word_counts

# Example usage
paragraph = "Bali is predominantly a Hindu country. Bali is known for its elaborate, traditional dancing. The dancing is inspired by its Hindi beliefs. Most of the dancing portrays tales of good versus evil. To watch the dancing is a breathtaking experience. Lombok has some impressive points of interest – the majestic Gunung Rinjani is an active volcano. It is the second highest peak in Indonesia. Art is a Balinese passion. Batik paintings and carved statues make popular souvenirs. Artists can be seen whittling and painting on the streets, particularly in Ubud. It is easy to appreciate each island as an attractive tourist destination. Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year. Snorkelling and diving around the nearby Gili Islands is magnificent. Marine fish, starfish, turtles and coral reef are present in abundance. Bali and Lombok are part of the Indonesian archipelago. Bali has some spectacular temples. The most significant is the Mother Temple, Besakih. The inhabitants of Lombok are mostly Muslim with a Hindu minority. Lombok remains the most understated of the two islands. Lombok has several temples worthy of a visit, though they are less prolific. Bali and Lombok are neighbouring islands."
counts = count_words(paragraph)
print(counts)
