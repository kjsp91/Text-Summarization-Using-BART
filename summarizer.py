from transformers import BartForConditionalGeneration, BartTokenizer
from nltk.tokenize import word_tokenize
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# Load BART model and tokenizer for summarization
model_name = 'facebook/bart-large'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
model_name = "google/pegasus-large"  # Replace with the desired PEGASUS variant
model1 = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer1 = PegasusTokenizer.from_pretrained(model_name)
print("Success") 
def summarize_text(text):
    # Tokenize input text
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, num_beams=22, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    #input_ids1 = tokenizer1.encode(text, return_tensors='pt', max_length=512, truncation=True)
    #summary_ids1 = model1.generate(input_ids1, num_beams=22, max_length=150, early_stopping=True)
    #summary1 = tokenizer1.decode(summary_ids1[0], skip_special_tokens=True)
    hallucinated_words = identify_hallucinated_words(text, summary)
    #hallucinated_words1 = identify_hallucinated_words(text, summary1)
    #return summary,summary1,hallucinated_words,hallucinated_words1
    return summary,hallucinated_words
def identify_hallucinated_words(original_text, summary):
    # Tokenize the words in the original text and summary
    original_words = set(word_tokenize(original_text.lower()))
    summary_words = set(word_tokenize(summary.lower()))

    # Identify words present in the summary but not in the original text
    hallucinated_words = summary_words - original_words

    return list(hallucinated_words)
