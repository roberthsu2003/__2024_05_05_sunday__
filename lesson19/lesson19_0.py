# 台積電,聯電,聯發科,鴻海,2024年,(平均,中位數,最高價,最低價,最高價日期,最低價的日期)
import os
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
from datetime import date

#----------------------------------------------------------
# For store result to HTML file
#----------------------------------------------------------
def _float_format(v):
	return "{:.2f}".format(v)

# _export_to_html_part
# 把部分 Pandas DataFrame 資料寫入 HTML file
def _export_to_html_part(data:pd.DataFrame, title:str=None, first:int=5, last:int=5, append:bool=True):
	mode = 'a' if append else 'w'
	fpath = os.path.basename(__file__).replace('py', 'html')
	with open(fpath, mode) as f:
		# Check for add title
		if title:
			f.write(title)
		# Check for add head data
		if first > 0:
			f.write(data.iloc[:first,:].to_html(float_format=_float_format))
			f.write(".....")
		f.write(data.iloc[-last:,:].to_html(float_format=_float_format))
		f.write("<br>")

# _export_to_html_all
# 把所有 Pandas DataFrame 資料寫入 HTML file
def _export_to_html_all(data:pd.DataFrame, title:str=None, append:bool=True):
	_export_to_html_part(data, title=title, first=0, last=0, append=append)
#----------------------------------------------------------


# 給擷取最高最低價資料時，維持 column 順序用
ticker_name:list = []

# _index_date_list
# 1. 從 DataFrame index 取得日期
# 2. 調整日期格式為 ISO format(%Y-%m-%d)
# Input:
#   1. df: Pandas DataFrame
# Return: date list
def _index_date_list(df:pd.DataFrame) -> list:
	lst:list = []
	for d in df.index:
		lst.append(d.date().isoformat())
	return lst

# _parse_data
# 1. 解析出平均價, 中位數, 最高價, 最低價, 最高價日期和最低價日期資訊
# 2. 列出所有的最高價日期和最低價日期，用逗號區隔
# Input:
#   1. data: Pandas DataFrame
# Return: Pandas series data
def _parse_data(data:pd.DataFrame) -> pd.Series:
	max_price = data.max()
	max_date = ",".join(_index_date_list(data[data == max_price]))
	min_price = data.min()
	min_date = ",".join(_index_date_list(data[data == min_price]))
	mean = data.mean()
	median = data.median()
	return pd.Series(
		[mean, median, max_price, min_price, max_date, min_date],
		index=['平均', '中位數', '最高價', '最低價', '最高價日期', '最低價日期'])

# _get_for_date
# 依據指定的 date 來擷取 dataFrame
# Input
#   1. data: Pandas DataFrame
#   2. date_lst: expected date list
# Return: pd.DataFrame
def _get_for_date(data:pd.DataFrame, date_lst:list) -> pd.DataFrame:
	global ticker_name
	# add DataFrame 後會有 column 順序改變情形
	# 為維持 column 順序，create DataFrame 時指定 column 順序
	df_nu = pd.DataFrame(columns=ticker_name, copy=False)
	for idx in data.index.tolist():
		if idx.date().isoformat() in date_lst:
			df = data[data.index == idx]
			df_nu = df_nu.add(df, fill_value=0)
	return df_nu

def _main():
	global ticker_name
	# Set mapping table of ticker and ticker name
	ticker_map:dict = {'2330.TW':'臺積電', '2303.TW':'聯電', '2454.TW':'聯發科', '2317.TW':'鴻海'}
	# Generate ticker list from ticker name mapping table
	ticker_lst:list = ticker_map.keys()
	ticker_name = ticker_map.values()
	# 直接指定要擷取的資料年份，以減少資料大小和處理程序
	# Set the start and end date
	get_year = 2024
	start = date(get_year, 1, 1)
	end = date(get_year, 12, 31)
	# Get stock data from Yahoo
	# 注意: yfinance 和 pandas_datareader 的說明文件不甚詳盡，使用時要特別小心
	# NOTE: Don't forget call yf.pdr_override() first
	yf.pdr_override()
	all_data:dict = {ticker:pdr.get_data_yahoo(ticker, start=start, end=end) for ticker in ticker_lst}

	# Convert stock data (dict) to Pandas DataFrame, change the column name and drop null data
	df_year:pd.DataFrame = pd.DataFrame({k:v['Adj Close'] for k,v in all_data.items()}).rename(columns=ticker_map).dropna()
	_export_to_html_part(df_year, title="2024 全年股票資料(共 {} 筆，僅顯示部分)".format(len(df_year)), append=False)
	df_parsed = df_year.apply(_parse_data)
	_export_to_html_all(df_parsed, title="分析後的 2024 全年股票資訊")

	# 列出最高價和最低價的資料
	chk_lst:list = ['最高價', '最低價']
	for chk in chk_lst:
		# Generate date list
		date_lst:list = []
		chk_col:str = chk+'日期'
		for v in df_parsed.loc[chk_col].values:
			date_lst += v.split(',')
		df_chk = _get_for_date(df_year, date_lst)
		_export_to_html_all(df_chk, title="{}資料有 {} 筆".format(chk, len(df_chk)))
	#df_max = df_parsed.apply()


if __name__ == "__main__":
	_main()