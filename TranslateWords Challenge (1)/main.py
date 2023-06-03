import csv
import time

def load_dictionary(filename):
    dictionary = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                english_word = row[0]
                french_word = row[1]
                dictionary[english_word] = french_word
    return dictionary

def load_find_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        find_words = file.read().splitlines()
    return find_words

def replace_words(text, find_words, dictionary):
    replaced_words = set()
    word_count = {}
    replaced_text = text
    for word in find_words:
        if word in dictionary:
            replaced_text = replaced_text.replace(word, dictionary[word])
            replaced_words.add(dictionary[word])
            if dictionary[word] in word_count:
                word_count[dictionary[word]] += 1
            else:
                word_count[dictionary[word]] = 1
    return replaced_text, replaced_words, word_count

def process_file(input_file, find_words_file, dictionary_file, output_file):
    start_time = time.time()
    
    # Load dictionary and find words list
    dictionary = load_dictionary(dictionary_file)
    find_words = load_find_words(find_words_file)
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Replace words
    replaced_text, replaced_words, word_count = replace_words(text, find_words, dictionary)
    
    # Write output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(replaced_text)
    
    # Calculate performance metrics
    end_time = time.time()
    elapsed_time = end_time - start_time
    memory_usage = 0  # TODO: Calculate memory usage
    
    # Write performance.txt
    with open('performance.txt', 'w') as file:
        file.write(f'Time taken: {elapsed_time} seconds\n')
        file.write(f'Memory taken: {memory_usage} bytes\n')
    
    # Write frequency.csv
    with open('frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English word', 'French word', 'Frequency'])
        for word, count in word_count.items():
            french_word = dictionary.get(word, '')
            writer.writerow([word, french_word, count])

if __name__ == '__main__':
    input_file = 't8.shakespeare.txt'
    find_words_file = 'find_words.txt'
    dictionary_file = 'french_dictionary.csv'
    output_file = 't8.shakespeare.translated.txt'
    process_file(input_file, find_words_file, dictionary_file, output_file)
