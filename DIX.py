import pandas as pd
import numpy as np
from tqdm import tqdm

def darkPoolBuying():
    df1 = pd.read_pickle('total_shorts.pkl')
    
    last_idx = df1.index[-1]

    df_NDAQ = pd.DataFrame(columns=['ShortVolume', 'TotalVolume'])
    df_NYSE = pd.DataFrame(columns=['ShortVolume', 'TotalVolume'])
    df_ORF = pd.DataFrame(columns=['ShortVolume', 'TotalVolume'])

    for x in tqdm(pd.date_range(start=last_idx, end=pd.Timestamp.today(), freq='D')):
        year = str(x.date().year)
        month = str(x.date().month).zfill(2)
        day = str(x.date().day).zfill(2)
        try:
            url = 'http://regsho.finra.org/FNSQshvol'+year+month+day+'.txt'
            df = pd.read_csv(url, sep='|', dtype={'ShortVolume': np.float64,
                                                  'ShortExemptVolume': np.float64,
                                                  'TotalVolume': np.float64})

            df_NDAQ.loc[year+'/'+month+'/'+day, 'ShortVolume'] = df['ShortVolume'].sum(axis=0)
            df_NDAQ.loc[year+'/'+month+'/'+day, 'TotalVolume'] = df['TotalVolume'].sum(axis=0)
        except:
            pass

        try:
            url = 'http://regsho.finra.org/FNYXshvol'+year+month+day+'.txt'
            df = pd.read_csv(url, sep='|', dtype={'ShortVolume': np.float64,
                                                  'ShortExemptVolume': np.float64,
                                                  'TotalVolume': np.float64})

            df_NYSE.loc[year+'/'+month+'/'+day, 'ShortVolume'] = df['ShortVolume'].sum(axis=0)
            df_NYSE.loc[year+'/'+month+'/'+day, 'TotalVolume'] = df['TotalVolume'].sum(axis=0)
        except:
            pass

        try:
            url = 'http://regsho.finra.org/FNYXshvol'+year+month+day+'.txt'
            df = pd.read_csv(url, sep='|', dtype={'ShortVolume': np.float64,
                                                  'ShortExemptVolume': np.float64,
                                                  'TotalVolume': np.float64})

            df_ORF.loc[year+'/'+month+'/'+day, 'ShortVolume'] = df['ShortVolume'].sum(axis=0)
            df_ORF.loc[year+'/'+month+'/'+day, 'TotalVolume'] = df['TotalVolume'].sum(axis=0)
        except:
            pass

    df_NDAQ.index = pd.to_datetime(df_NDAQ.index, infer_datetime_format=True)
    df_NYSE.index = pd.to_datetime(df_NYSE.index, infer_datetime_format=True)
    df_ORF.index = pd.to_datetime(df_ORF.index, infer_datetime_format=True)

    df2 = df_NDAQ + df_NYSE + df_ORF
    df2['ShortPct'] = df2['ShortVolume']/df2['TotalVolume']
    df3 = df1.iloc[:-1, :].append(df2, sort=True)
    df3.to_pickle('total_shorts.pkl')
    return df3
