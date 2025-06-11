from flask import Flask, request, render_template, jsonify
from pipeline import SummarizationPipeline
import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)
pipeline = SummarizationPipeline()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    file = request.files["document"]
    result = pipeline.run(file)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
