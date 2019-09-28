import boto3


# Create an S3 client
s3 = boto3.client('s3')

filename = 'handler.py'
bucket_name = 's3-file-handler-bucket'
upload_name = "Incoming/" + filename

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, upload_name)