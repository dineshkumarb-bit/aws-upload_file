# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import os
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
app.secret_key = 'secret123'  # Needed for flash messages

# Replace with your bucket name
S3_BUCKET = 'chandana-bucket-demo'

# Create S3 client
s3 = boto3.client('s3')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            try:
                s3.upload_fileobj(file, S3_BUCKET, file.filename)
                flash('✅ File uploaded to S3 successfully!')
            except NoCredentialsError:
                flash('❌ AWS credentials not found!')
            except Exception as e:
                flash(f'❌ Upload failed: {e}')
            return redirect(url_for('upload_file'))
        else:
            flash('❌ No file selected')
            return redirect(url_for('upload_file'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
