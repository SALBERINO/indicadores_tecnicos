def devolver_con_percentil(df):
  data = df . copy()
  data["variacion"]  = data["Close"].pct_change() * 100 
  data.dropna(inplace=True)
  data["rank_variacion"] = data["variacion"].rank()
  data["rank_variacion_pct"] = data["variacion"].rank(pct= True)
  return data
