from botocore.exceptions import ClientError

from backend.core.config import settings


def upload_file_to_bucket(s3_client, file_obj, bucket, folder, object_name=None):
    """Upload a file to an S3 bucket
    :param s3_client: s3
    :param file_obj: File to upload
    :param bucket: Bucket to upload to
    :param folder: Folder to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_obj

    # Upload the file
    try:
        response = s3_client.upload_fileobj(file_obj, bucket, f"{folder}/{object_name}")
        print(response)
    except ClientError:
        return False
    return True


def get_s3_image_url(property_title: str):
    s3_url = settings.S3_FILE_PATH + "property-" + property_title.replace(" ", "-") + ".png"
    print(s3_url)
    return s3_url
