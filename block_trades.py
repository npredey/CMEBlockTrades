import datetime
import requests
import pandas as pd

current_date = f"{datetime.datetime.now():%m%d%Y}"
cme_url = "https://www.cmegroup.com/CmeWS/mvc/xsltTransformer.do?xlstDoc=/XSLT/md/blocks-records.xsl&url=/da/BlockTradeQuotes/V1/Block/BlockTrades?exchange=XCBT,XCME,XCEC,DUMX,XNYM&foi=FUT,OPT,SPD&assetClassId=1,6&tradeDate={}&sortCol=time&sortBy=desc"
cme_url = cme_url.format(current_date)
# print(cme_url)

html_data = requests.get(cme_url)._content
tables = pd.read_html(html_data)
block_trades_table = tables[0]
# print(type(block_trades_table))

print(block_trades_table.to_string(index=False))
