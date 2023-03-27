import pandas as pd
import fastparquet as fp
import requests
import datetime as dt

path = "C://Users//Dejene//OneDrive//Documents//GitHub//yellow_tripdata_2022-01.parquet"
# path = "https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
start = dt.datetime.now()
try:
    ytripDF = pd.read_parquet(path)
    print(f"success Dejene")
except Exception as e:
    print(f"find other way to get the data: {e}")
print(ytripDF)
end = dt.datetime.now()
diff_time = end - start
print(diff_time)