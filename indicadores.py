def devolver_con_percentil(df):
  data = df . copy()
  data["variacion"]  = data["Close"].pct_change() * 100 
  data.dropna(inplace=True)
  data["rank_variacion"] = data["variacion"].rank()
  data["rank_variacion_pct"] = data["variacion"].rank(pct= True)
  return data

def indicador_gap_basico(data):
  import numpy as np
  df = data.copy()
  df_menosuno = data.copy().shift(1)
  df_menosdos = data.copy().shift(2)
  df_menosuno['tendencia'] = np.where(df_menosuno['Close'] > df_menosdos['Close'],'alsista','bajista')
  df['gap'] = np.where((df_menosuno['tendencia'] == 'alsista') & (df['Open'] > df_menosuno['High']) & (df['Close'] > df['Open']), 'gap alsista', np.where((df_menosuno['tendencia'] == 'bajista)') & (df['Open'] < df_menosuno['Low']) & (df['Close'] < df['Open']),'gap bajista', 'sin gap'))
  return df
