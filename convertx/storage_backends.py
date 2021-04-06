from storages.backends.s3boto3 import S3Boto3Storage
from dotenv import load_dotenv
from convertx.constants import DOTENV_PATH
import os

load_dotenv(dotenv_path=DOTENV_PATH)


class MediaStorage(S3Boto3Storage):
	bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
