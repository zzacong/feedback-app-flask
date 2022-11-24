import os
from flask import Flask, render_template, request, logging
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

# ! Init App
app = Flask(__name__)

# ! App Configs
if app.env == 'development':
  import dotenv
  dotenv.load_dotenv(override=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ! Init db
db = SQLAlchemy(app)


# ! Model
class Feedback(db.Model):
  __tablename__ = 'feedback'
  id = db.Column(db.Integer, primary_key=True)
  customer = db.Column(db.String(200), unique=True)
  dealer = db.Column(db.String(200))
  rating = db.Column(db.Integer)
  comments = db.Column(db.Text())

  def __init__(self, customer, dealer, rating, comments):
    self.customer = customer
    self.dealer = dealer
    self.rating = rating
    self.comments = comments


# ! Index
@app.route('/')
def index():
  return render_template('index.html')


# ! Submit
@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    customer = request.form['customer']
    dealer = request.form['dealer']
    rating = request.form['rating']
    comments = request.form['comments']
    # app.logger.info(f'{customer}, {dealer}, {rating}, {comments}')
    if customer == '' or dealer == '':
      return render_template('index.html', msg='Please enter required fields.')
    if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
      data = Feedback(customer, dealer, rating, comments)
      db.session.add(data)
      db.session.commit()
      send_mail(customer, dealer, rating, comments)
      return render_template('success.html')
    return render_template('index.html', msg='You can only submit one feedback.')


if __name__ == '__main__':
  app.run()
