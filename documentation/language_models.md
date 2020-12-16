# Language Models

The data is provided with word level suprisal values from three language models.

- `SURP-GPT2`: word surprisal according to the GPT2 language model trained on the WebText corpus (off-the-shelf). Radford et al. 2019 "Language Models are Unsupervised Multitask Learners".
When the GPT tokenizer splits the word, the suprtisal value is the sum of the subword surprisals.

- `SURP-LSTM`: word surprisal according to an LSTM RNN language model trained on BLLIP.
We use the PyTorch implementation of a word-level LSTM RNN (https://github.com/pytorch/examples/tree/master/word_language_model), with the standard parameters:
2 layers, 200 hidden units, size of word embeddings 200. The model is trained for 10 epochs (initial learning rate 20, gradient clipping 0.25, batch size 20, dropout 0.2).

- `SURP-KENLM`: word suprisal according to an ngram language model trained on BLLIP.
We train a 5-gram language model using KenLM (https://kheafield.com/code/kenlm/)

## Notes on LSTM and Ngram model training:

- Training data: The LSTM and ngram models are trained on the BLLIP corpus, excluding sentences which were used in CELER (14,274 sentences from BLLIP, and 313 sentences from WSJ PTB which have identical sentences in BLLIP). The remaining 1,781,792 sentences are dividided into 1,681,792 sentences (35,085,708 words) for training and 100,000 sentences (2,088,980 words) for validation (used for LSTM training). 
- Preprocessing: 
   - Sentences were whitespace tokenized
   - Words were lowercased, punctuation was removed, numbers were converted to NUM (the same normalization is performed in the `WORD_NORM` field).
   - The order of the sentences was shuffled prior to language model training.
- The LSTM model expects <eos> as the first token of the sentence.