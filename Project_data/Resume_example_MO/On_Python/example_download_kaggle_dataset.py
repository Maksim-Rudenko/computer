import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# if stand-alone dataset
#api.dataset_download_files('hmavrodiev/london-bike-sharing-dataset',
   #        file_name = 'london_merged.csv')
# example : https://www.kaggle.com/datasets/kazanova/sentiment140
api.dataset_download_files(dataset='london_merged.csv', path='hmavrodiev/london-bike-sharing-dataset')
#kaggle.api.authenticate()

#kaggle.api.dataset_download_files('london_merged.csv',
#                                  path='/kaggle/input/london-bike-sharing-dataset/london_merged.csv', unzip=True)