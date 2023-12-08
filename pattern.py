from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
db = SQLAlchemy(app)

# Generate a key for encryption (change this key in a production environment)
key = Fernet.generate_key()
cipher_suite = Fernet(key)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f"Entry(id={self.id}, service={self.service}, username={self.username})"


def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())


def decrypt_data(data):
    return cipher_suite.decrypt(data).decode()


@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)


@app.route('/add_entry', methods=['POST'])
def add_entry():
    service = request.form.get('service')
    username = request.form.get('username')
    password = request.form.get('password')

    encrypted_password = encrypt_data(password)

    new_entry = Entry(service=service, username=username, password=encrypted_password)
    db.session.add(new_entry)
    db.session.commit()

    flash(f'Entry for {service} added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/decrypt_password/<int:entry_id>')
def decrypt_password(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    decrypted_password = decrypt_data(entry.password)
    return render_template('decrypt_password.html', entry=entry, decrypted_password=decrypted_password)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
