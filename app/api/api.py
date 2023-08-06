import tornado.ioloop
import tornado.web
from transformers_model import TransformersModel
from mongodb_storage import get_data, create_data, update_data, delete_data
import json

model = TransformersModel('t5-base')

class GenerateHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)

        if 'text' not in data:
            self.set_status(400)  
            self.write({'error': 'Nenhum texto fornecido'})
            return

        generated_text = model.generate_text(data['text'])

        self.write({'generated_text': generated_text})

class DataHandler(tornado.web.RequestHandler):
    def get(self, data_id):
        data = get_data(data_id)
        self.write(data)

    def post(self, data_id):
        data = json.loads(self.request.body)
        create_data(data_id, data)
        self.set_status(201)  
        self.write(data)

    def put(self, data_id):
        data = json.loads(self.request.body)
        update_data(data_id, data)
        self.write(data)

    def delete(self, data_id):
        delete_data(data_id)
        self.set_status(204)  

def make_app():
    return tornado.web.Application([
        (r"/generate", GenerateHandler),
        (r"/data/(.*)", DataHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()
