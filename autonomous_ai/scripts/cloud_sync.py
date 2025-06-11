import boto3
import subprocess
import os

def upload_to_s3(file_path, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, object_name)

def upload_to_gdrive(file_path):
    subprocess.run(["gdown", "https://drive.google.com/drive/folders/YOUR_FOLDER_ID", "--folder", "--upload", file_path])

# Example usage
# upload_to_s3("results/analysis.json", "your-bucket-name")
# upload_to_gdrive("results/analysis.json")
