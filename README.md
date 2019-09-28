# How to...

I will suppose you already setup serverless environment on your local.

## Clone project from Github repository

git clone https://github.com/mbpup/s3-file-handler.git

## Replace S3 bucket name as you want.
- custom:
-     bucket: <your bucket name here>

## Deploy project
- cd s3-file-handler/
- serverless deploy

## Test prject

### Create virtualenv for running script.
 - python3 -m venv env

### Install boto3 package
 - pip install boto3

### Run test script
 - python file-uploader.py [file path to upload s3 bucket]