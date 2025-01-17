from flask import Flask, request, json
from model import MLModelHandler, DLModelHandler
from train_ml import *

app = Flask(__name__)

# assign model handler as global variable [2 LINES]

ml_handler = MLModelHandler()
#dl_handler = DLModelHandler()


@app.route("/predict", methods=["POST"])
def predict():
    # handle request and body
    body = request.get_json()
    text = body.get('text', '')
    text = [text] if isinstance(text, str) else text
    do_fast = body.get('do_fast', True)

    # model inference [2 LINES]
    if do_fast:
        predictions = ml_handler.handle(text)
    else:
        predictions = ml_handler.handle(text)

    # response
    result = json.dumps({str(i): {'text': t, 'label': l, 'confidence': c}
                         for i, (t, l, c) in enumerate(zip(text, predictions[0], predictions[1]))})
    return result



@app.route("/train")
def train():
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    start_time = datetime.now()
    # Download train and test data from github
    for mode in ['train', 'test']:
        download_data(mode)

    # train and evaluate model
    model, vectorizer = train_and_evaluate()

    # Serialization
    serialization(model, vectorizer)
    return f"Elapsed time : {datetime.now() - start_time}"





if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
