




from transformers import AutoModelForSeq2SeqLM, AutoTokenizer



def get_niraj_corpus_summary(
        model_name = "tsmatz/mt5_summarize_japanese", 
        corpus_file_path = "./Data/corpus.txt", 
        summary_file_path = './Data/summary_corpus.txt', 
        verbose = False, 
        ):
    if verbose: print("Model Name:", model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(corpus_file_path, "r", encoding="utf-8") as file:
        paragraph = file.read()
    # Tokenize and summarize
    inputs = tokenizer.encode("summarize: " + paragraph, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=700, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True) 

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    with open(summary_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)
    return summary