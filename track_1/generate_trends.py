import random
import lorem

# Function to generate random text with a random number of sentences per paragraph
def generate_random_text(num_paragraphs, min_sentences, max_sentences):
    random_text = ""
    for _ in range(num_paragraphs):
        sentences_per_paragraph = random.randint(min_sentences, max_sentences)
        for _ in range(sentences_per_paragraph):
            sentence = lorem.sentence()
            random_text += sentence + ' '
        random_text += '\n'
    return random_text

# Set the number of paragraphs and the range for the number of sentences per paragraph
num_paragraphs = 1000
min_sentences_per_paragraph = 10
max_sentences_per_paragraph = 100

# Create 10 text files with generated paragraphs
for file_num in range(1, 11):
    file_name = f"{file_num}_customer_trends.txt"
    random_text = generate_random_text(num_paragraphs, min_sentences_per_paragraph, max_sentences_per_paragraph)
    
    with open(file_name, "w") as file:
        file.write(random_text)

    print(f"File '{file_name}' created.")