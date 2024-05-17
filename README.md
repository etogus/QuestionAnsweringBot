<p>A bot that can answer questions in different fields of knowledge, using the Jeopardy! question-answering database. </p><br/>

The program does the following:<br/>
> 1. Preprocess the user's input and train the Doc2Vec model on JSON Jeopardy corpus.<br/>
> 2. Using the number of the closest topic, find the answer in the training data.<br/>
> 3. Return the answer to the user.<br/>
> 4. Ask the user if he wants to play again.<br/>
> 5. If the response is yes, the program repeats the algorithm. If the response is no, the program terminates.<br/>

Example<br/>
> Hello! I'm Jane, a question answering bot who knows answers to all the questions from the 'Jeopardy!' game.<br/>
> Ask me something!<br/>
> Spanish for "mask", this cosmetic is used to color the eyelashes.<br/>
> Let's play!<br/>
> I know this question: its number is 10569. I'm 78% sure of this.<br/>
> The answer is mascara.<br/>
> Do you want to ask me again? (yes/no)<br/>
> no<br/>
> It was nice to play with you! Goodbye!<br/>
