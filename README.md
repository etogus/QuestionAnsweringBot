# Question-Answering Bot

<p>A bot that can answer questions in different fields of knowledge, using the Jeopardy! question-answering database.</p>

## Functionality
1. Preprocess the user's input and train the Doc2Vec model on JSON Jeopardy corpus.<br/>
2. Using the number of the closest topic, find the answer in the training data.<br/>
3. Return the answer to the user.<br/>
4. Ask the user if he wants to play again.<br/>
5. If the response is yes, the program repeats the algorithm. If the response is no, the program terminates.<br/>

## Example
```
Hello! I'm Jane, a question answering bot who knows answers to all the questions from the 'Jeopardy!' game.
Ask me something!
Spanish for "mask", this cosmetic is used to color the eyelashes.
Let's play!
I know this question: its number is 10569. I'm 78% sure of this.
The answer is mascara.
Do you want to ask me again? (yes/no)
no
It was nice to play with you! Goodbye!
```
