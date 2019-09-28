
import sys
import os.path
import boto3

def main():

    if(len(sys.argv) != 2):
        print ("Sorry run script as follow:")
        print ("python %s <file path to upload s3 bucket>" % sys.argv[0])
        sys.exit()

    # Create an S3 client
    s3 = boto3.client('s3')

    filename = sys.argv[1]
    if os.path.exists(filename) == False:
        print ("%s not exist." % sys.argv[1])
        sys.exit()

    bucket_name = 's3-file-handler-bucket'
    upload_name = "Incoming/" + filename

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, upload_name)
  
if __name__== "__main__":
  main()