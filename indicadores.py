def devolver_con_percentil(data):
  """ 
    Esta funcion recibe una matriz de datos, que posee la serie historica con los valores encolumnados por
    Open, High, Low, Close
  """
  df = data . copy()
  df["variacion"]  = df["Close"].pct_change() * 100 
  df.dropna(inplace=True)
  df["rank_variacion"] = df["variacion"].rank()
  df["rank_variacion_pct"] = df["variacion"].rank(pct= True)
  return df

def indicador_gap_basico(data):
  """ 
    Esta funcion recibe una matriz de datos, que posee la serie historica con los valores encolumnados por
    Open, High, Low, Close
  """
  import numpy as np
  df = data.copy()
  df_menosuno = data.copy().shift(1)
  df_menosdos = data.copy().shift(2)
  df_menosuno['tendencia'] = np.where(df_menosuno['Close'] > df_menosdos['Close'],'alsista','bajista')
  df['gap'] = np.where((df_menosuno['tendencia'] == 'alsista') & (df['Open'] > df_menosuno['High']) & (df['Close'] > df['Open']), 'gap alsista', np.where((df_menosuno['tendencia'] == 'bajista)') & (df['Open'] < df_menosuno['Low']) & (df['Close'] < df['Open']),'gap bajista', 'sin gap'))
  return df
