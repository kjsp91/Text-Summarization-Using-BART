from flask import Flask, render_template, request
#from summarizer.py import summarize_text
# app.py
from summarizer import summarize_text



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        #summarized_text1,summarized_text2,hallucination1,hallucination2 = summarize_text(text)
        #return render_template('index.html', text=text, summarized_text1=summarized_text1 ,summarized_text2=summarized_text2 , hallucination1=hallucination1 ,hallucination2=hallucination2 )
        summarized_text1,hallucination1 = summarize_text(text)
        return render_template('index.html', text=text, summarized_text1=summarized_text1 , hallucination1=hallucination1  )

if __name__ == '__main__':
    app.run(debug=True)

