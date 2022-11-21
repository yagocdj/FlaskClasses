from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_51M6ZRvJm4oPq6G8oZ6AlNla3DuNzEgp7AUNbzTVg1e6GDsd2NSGBYfQebjgiWXseuZyBtU7JPXjowhPCXShCPw8n00fQqgIwMg"

stripe.api_key = "sk_test_51M6ZRvJm4oPq6G8oW5psaQ0k1DgMTz3urSh7YS4ZG4G9ySBVtsJCFqzHQd1EzK71yitbIgsA5Yp6vX3DTZaKDEXX00eeM787xq"

@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment', methods=['POST'])
def payment():
    
    # CUSTOMER INFO
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    # PAYMENT INFO
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description='Donation'
    )

    return redirect(url_for('thankyou'))

if __name__ == "__main__":
    app.run(debug=True)