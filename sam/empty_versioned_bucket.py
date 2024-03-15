import boto3
import sys 

if len(sys.argv) < 2 : 
    print('Please provide your account ID as an argument!')
    sys.exit()

#Edit the bucket name with your account ID
BUCKET = 'uploads-tasks-app-us-east-1-'+sys.argv[1]

print('Emptying versioned bucket: ' + BUCKET)

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()
