
# Import necessary modules
from flask import Flask, request, render_template
from flask_babel import Babel, lazy_gettext as _l

# Create a Flask application
app = Flask(__name__)

# Configure Babel for internationalization
babel = Babel(app)

# Define the supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Load the Dutch translation
babel.locale_selector_func = lambda: 'nl'

# Define the flashcard data (sample data)
flashcards = [
    {'source': 'Fair dinkum', 'translation': 'Echt waar'},
    {'source': 'She'll be right, mate', 'translation': 'Het komt wel goed, maat'},
    {'source': 'Chuck a shrimp on the barbie', 'translation': 'Gooi een garnaal op de barbecue'}
]

# Define the routes
@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)

@app.route('/translate', methods=['POST'])
def translate():
    # Get the user input
    source_text = request.form['source_text']

    # Translate the text
    translated_text = _l(source_text)

    # Render the results page
    return render_template('results.html', source_text=source_text, translated_text=translated_text)

# Run the application
if __name__ == '__main__':
    app.run()
