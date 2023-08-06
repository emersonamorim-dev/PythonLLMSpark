import unittest
from transformers_model import TransformersModel

class TestTransformersModel(unittest.TestCase):
    def test_generate_text(self):
        model = TransformersModel('t5-base')

        input_text = "Translate this text to Portuguese: "
        generated_text = model.generate_text(input_text)

        # Verifique se o texto é uma string
        self.assertIsInstance(generated_text, str)

        # Verifique se o texto gerado contém algum texto
        self.assertGreater(len(generated_text), 0)

if __name__ == '__main__':
    unittest.main()
