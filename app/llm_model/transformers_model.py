from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TransformersModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_text(self, input_text):
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=5)

        generated_text = [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        return generated_text
