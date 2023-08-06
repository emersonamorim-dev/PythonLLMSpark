from transformers_model import TransformersModel

def main():
    model = TransformersModel('t5-base')

    input_text = "Translate this text to Portuguese: "
    generated_text = model.generate_text(input_text)

    print(generated_text)

if __name__ == "__main__":
    main()
