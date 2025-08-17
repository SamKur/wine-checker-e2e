import os

class S3Sync:
    '''
    Requires AWS CLI installed and credentials configured (aws configure).
    Uses aws s3 sync under the hood (good for big directories, handles diffs).
    '''
    def sync_folder_to_s3(self, folder: str, aws_bucket_url: str):
        """
        Upload local folder to S3 bucket path.
        """
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        exit_code = os.system(command)
        if exit_code != 0:
            raise Exception(f"Failed to sync {folder} to {aws_bucket_url}")

    def sync_folder_from_s3(self, aws_bucket_url: str, folder: str):
        """
        Download folder from S3 bucket path to local.
        """
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        exit_code = os.system(command)
        if exit_code != 0:
            raise Exception(f"Failed to sync {aws_bucket_url} to {folder}")
