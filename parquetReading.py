import pandas as pd


'''with open('/home/imran/Desktop/kaggle/bengaliai-cv19/train_image_data_0_csv.csv','w') as csv_file:
    print('Reading par_file1.parquet')
    df = pd.read_parquet('/home/imran/Desktop/kaggle/bengaliai-cv19/train_image_data_0.parquet')
    df.to_csv(csv_file, index=False)
    print('par_file1.parquet appended to csv_file.csv\n')
    csv_file.close()'''

df = pd.read_parquet('/home/imran/Desktop/kaggle/bengaliai-cv19/train_image_data_0.parquet')
df.tail()