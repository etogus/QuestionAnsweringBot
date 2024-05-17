import json
import re

from nltk import word_tokenize
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from scipy.spatial.distance import cosine
import pandas as pd


def is_punctuation(word):
    return bool(re.match(r'^[\W_]+$', word))


# remove punctuation and tokenize
def preprocess_sentence(sentence):
    tokenized_sentence = word_tokenize(sentence.lower())
    for token in tokenized_sentence:
        if is_punctuation(token):
            tokenized_sentence.remove(token)
    return tokenized_sentence


# Search for the most similar question to the user input
def find_similar_question(q_corpus, u_input, d2v):
    user_vector = d2v.infer_vector(preprocess_sentence(u_input))
    most_sim = -1
    most_sim_question = ""
    most_sim_index = -1
    for index, question in enumerate(q_corpus):
        question_vector = model.infer_vector(question)
        cosine_similarity = 1 - cosine(user_vector, question_vector)
        if cosine_similarity > most_sim:
            most_sim = cosine_similarity
            most_sim_question = question
            most_sim_index = index
    return most_sim, most_sim_question, most_sim_index


json_file = open("C:\\Users\\gusey\\Downloads\\jeopardy.json", "r", encoding="utf-8")
json_corpus = json.load(json_file)

# DataFrame object from JSON
df = pd.DataFrame(json_corpus)

bot_name = "Gus_GPT"
print(f"Hello! I'm {bot_name}, a question answering bot who knows answers to all questions from the "
      "'Jeopardy!' game.")
print("Ask me something!")

user_input = input()

# Collect only questions
questions_corpus = []
for entry in json_corpus:
    questions_corpus.append(preprocess_sentence(entry['question']))

# Doc2Vec model training
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(questions_corpus)]
model = Doc2Vec(documents, vector_size=200, window=3, min_count=4, workers=4, epochs=10)
model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)

print("Let's play!")

most_similar, most_similar_question, most_similar_index = find_similar_question(questions_corpus, user_input, model)

print(f"I know this question: its number is: {most_similar_index}. I'm {int(round(most_similar * 100, 0))}% sure of "
      f"this.")
print(f"The answer is {df.loc[most_similar_index, 'answer']}.")

# Ask user in a loop until he decides it's enough
while True:
    print("Do you want to ask me again? (yes/no)")
    user_input = input()
    if user_input.lower() == 'no':
        print("It was nice to play with you! Goodbye!")
        break
    else:
        print("Ask me something!")
        user_input = input()
        print("Let's play!")
        most_similar, most_similar_question, most_similar_index = find_similar_question(questions_corpus, user_input,
                                                                                        model)
        print(
            f"I know this question: its number is: {most_similar_index}. I'm {int(round(most_similar * 100, 0))}% "
            f"sure of"
            f"this.")
        print(f"The answer is {df.loc[most_similar_index, 'answer']}.")
