from flask import Flask, render_template, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Example pandas usage
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    # Convert dataframe to HTML table for demonstration
    table_html = df.to_html(classes='data')
    return render_template('firstpage.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)