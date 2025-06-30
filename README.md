# aws-upload_file

# 📁 Flask S3 File Upload App on AWS EC2

This project is a simple web-based file uploader built using **Flask**, which allows users to upload files via a browser interface and stores them **directly into an AWS S3 bucket**.

---

## 🚀 Features

- Upload files via web browser
- Store files directly in AWS S3
- Simple and lightweight UI
- Built with Flask and Boto3
- Deployable on AWS EC2

---

## 📦 Prerequisites

- AWS account with an existing **S3 bucket**
- IAM user with `s3:PutObject` permission on the bucket
- Running EC2 instance (Ubuntu)
- SSH access to the EC2 instance

---

## 🔧 Setup Instructions

### 1. SSH into your EC2 instance

```bash
ssh -i path/to/your-key.pem ubuntu@<EC2-PUBLIC-IP>


**Update packages and install Python tools**

sudo apt update
sudo apt install -y python3-pip python3-venv git


**📁 Project Setup
Clone your repo or set up manually**

git clone https://github.com/dineshkumarb-bit/code.git aws-upload_file
cd aws-upload_file


** Create and activate a virtual environment **

python3 -m venv venv
source venv/bin/activate
pip install flask boto3

**Configure AWS Credentials**

sudo apt install awscli
aws configure

S3_BUCKET = 'your-actual-bucket-name'

python3 app.py

http://<EC2-PUBLIC-IP>:5000

**🌐 Allow Port 5000 in Security Group
Go to EC2 Console → Instances → Security Groups**

Select your instance’s Security Group

Edit Inbound rules

Add:

Type: Custom TCP

Port: 5000

Source: 0.0.0.0/0


✅ Project Structure
aws-upload_file/
├── upload_s3_app/
│   ├── app.py
│   ├── templates/
│   │   └── upload.html
│   └── venv/
├── README.md
