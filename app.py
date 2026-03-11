from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Le-Nair Koffa! This is my first HTML page.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()

# Route for favorite course — accepts GET query parameters
# subject and course_number passed via URL
@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject', '')
    course_number = request.args.get('course_number', '')
    return render_template('favorite-course.html',
                           subject=subject,
                           course_number=course_number)

# Route for contact form — handles GET and POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
