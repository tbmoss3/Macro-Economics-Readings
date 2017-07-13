"""

This is a simple project using the FRED API that reads in a list of data points that can be fully customized


"""
from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

fred = Fred(api_key = """key here""")

"""These are the keys that correspond to certain macro economic indicators and data points from the FRED Database"""

series = ['SP500','GDP', 'A067RL1A156NBEA', 'CPIAUCSL', 'A191RL1Q225SBEA', 'DGS10', 'IC4WSA',
          'UNRATE', 'DEXUSEU', 'BAMLH0A0HYM2', 'MEHOINUSA672N', 'M2V', 'GFDEGDQ188S',
          'FEDFUNDS', 'NAPM', 'DCOILWTICO', 'M2', 'CIVPART', 'PSAVERT', 'USD3MTD156N',
          'T10Y2Y', 'HOUST', 'DGS30', 'MORTG', 'DEXCHUS', 'BUSLOANS', 'UEMPMEAN',
          'EXPGSCA', 'NETEXP', 'A067RP1A027NBEA', 'FYFSD']

#strips the data down to the title, frequency of reporting, units,  and the latest values

for t in series:
  data = fred.get_series(t)
  info = fred.get_series_info(t)
  print info['title']
  print info['frequency']
  print info['units']
  print " " 
  print "LATEST VALUES:"
  print data.tail()
  print " "


#saves a PDF graph in the folder where code is stored

for i in series:
    info=fred.get_series_info(i)
    title=info['title']
    
    df={}
    df[title]=fred.get_series(i)
    df=pd.DataFrame(df)

    df.plot()
    base_filename=title
    suffix = '.pdf'
    plt.savefig(title+suffix)




