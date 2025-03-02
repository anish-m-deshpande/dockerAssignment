import os
import re
import socket

# Function to count words in file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # Handle contractions and split words
        text = re.sub(r"\'", "", text)
        words = re.findall(r'\w+', text.lower())
        return words

# File paths
data_path = "/home/data"
if_file1 = os.path.join(data_path, "IF-1.txt")
always_file = os.path.join(data_path, "AlwaysRememberUsThisWay-1.txt")

# Counting words in both files
if_words = count_words(if_file1)
always_words = count_words(always_file)

# Total number of words in each text file
if_word_count = len(if_words)
always_word_count = len(always_words)

# Grand total of words across both files
grand_total = if_word_count + always_word_count

# Top 3 most frequent words in IF-1.txt
if_word_freq = {word: if_words.count(word) for word in set(if_words)}
if_top_3 = sorted(if_word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

# Handling contractions and finding top 3 most frequent words in AlwaysRememberUsThisWay-1.txt
always_word_freq = {word: always_words.count(word) for word in set(always_words)}
always_top_3 = sorted(always_word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

# Getting the IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Ensuring the output directory exists
output_dir = os.path.join(data_path, "output")
os.makedirs(output_dir, exist_ok=True)

# Writing results to result.txt
output_path = os.path.join(output_dir, "result.txt")
with open(output_path, 'w') as result_file:
    result_file.write(f"Word count in IF-1.txt: {if_word_count}\n")
    result_file.write(f"Word count in AlwaysRememberUsThisWay-1.txt: {always_word_count}\n")
    result_file.write(f"Grand total word count: {grand_total}\n")
    result_file.write(f"Top 3 words in IF-1.txt: {if_top_3}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {always_top_3}\n")
    result_file.write(f"IP Address: {ip_address}\n")

# Print the result file content to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())