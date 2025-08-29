#from Hate import logger    # this runs __init__.py and configures logging
#from Hate.exception import CustomException
from Hate.configuration.backblaze_syncer import B2Sync
import logging
import sys

# logging.info("Logging has started")

#Checking the exception package
# try:
#   a = 1 / 0
# except Exception as e:
#   raise CustomException(e, sys) from e


B2Sync_cloud = B2Sync(key_id='00557c4c37bcc5e0000000001', app_key='K005vnRppeGChXJ6QTlv0x4K30pJtCg')
B2Sync_cloud.sync_folder_from_b2(bucket_name='hate-speech2025', filename='domain.csv', destination='.')