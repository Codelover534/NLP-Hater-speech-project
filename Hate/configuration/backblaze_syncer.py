# Import necessary classes from Backblaze B2 SDK
# InMemoryAccountInfo -> stores login info temporarily in memory
# B2Api -> main API object to interact with B2 (upload, download, list files, etc.)
from b2sdk.v2 import InMemoryAccountInfo, B2Api

# Define a class to handle uploading and downloading files from Backblaze B2
class B2Sync:

    # Constructor: runs when you create a new object of B2Sync
    # key_id and app_key are your Backblaze credentials
    def __init__(self, key_id, app_key):
        # Create a temporary container in memory to store login/session info
        info = InMemoryAccountInfo()

        # Initialize the Backblaze API client using the memory container
        self.b2_api = B2Api(info)

        # Login/authorize to Backblaze using your credentials
        # "production" means we are connecting to the real cloud, not test mode
        self.b2_api.authorize_account("production", key_id, app_key)


    # Method to upload a single file to a specific bucket
    def sync_folder_to_b2(self, bucket_name, filepath, filename):
        # Get the bucket object by name (must already exist in Backblaze)
        bucket = self.b2_api.get_bucket_by_name(bucket_name)

        # Upload the file from local path to the bucket
        # local_file -> path on your computer
        # file_name -> name to store the file as in Backblaze
        bucket.upload_local_file(local_file=f"{filepath}/{filename}", file_name=filename)


    # Method to download a single file from a bucket to a local destination
    def sync_folder_from_b2(self, bucket_name, filename, destination):
        # Get the bucket object by name
        bucket = self.b2_api.get_bucket_by_name(bucket_name)

        # Download the file by its name in the bucket
        # save_to -> save the file to your local path
        bucket.download_file_by_name(filename).save_to(f"{destination}/{filename}")
