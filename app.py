


# from flask import Flask, request, jsonify, render_template
# import yfinance as yf
# import pandas as pd
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/companies")
# def get_companies():
#     companies = [
#         {"symbol": "INFY.NS", "name": "Infosys"},
#         {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
#         {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
#         {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
#         {"symbol": "ITC.NS", "name": "ITC"},
#         {"symbol": "WIPRO.NS", "name": "Wipro"},
#         {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
#         {"symbol": "LT.NS", "name": "Larsen & Toubro"},
#         {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
#         {"symbol": "AXISBANK.NS", "name": "Axis Bank"},
#         {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"},
#         {"symbol": "SBIN.NS", "name": "State Bank of India"},
#         {"symbol": "ASIANPAINT.NS", "name": "Asian Paints"},
#         {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance"},
#         {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement"},
#         {"symbol": "MARUTI.NS", "name": "Maruti Suzuki"},
#         {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma"},
#         {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever"},
#         {"symbol": "TITAN.NS", "name": "Titan Company"},
#         {"symbol": "HCLTECH.NS", "name": "HCL Technologies"},
#         {"symbol": "ADANIENT.NS", "name": "Adani Enterprises"},
#         {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy"},
#         {"symbol": "ADANIPORTS.NS", "name": "Adani Ports"},
#         {"symbol": "JSWSTEEL.NS", "name": "JSW Steel"},
#         {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
#         {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation"},
#         {"symbol": "NTPC.NS", "name": "NTPC"},
#         {"symbol": "ONGC.NS", "name": "ONGC"},
#         {"symbol": "COALINDIA.NS", "name": "Coal India"},
#         {"symbol": "BPCL.NS", "name": "Bharat Petroleum"},
#     ]
#     return jsonify(companies)

# # Helper Functions
# def calculate_rsi(data, window=14):
#     delta = data.diff()
#     gain = delta.where(delta > 0, 0)
#     loss = -delta.where(delta < 0, 0)
#     avg_gain = gain.rolling(window=window).mean()
#     avg_loss = loss.rolling(window=window).mean()
#     rs = avg_gain / avg_loss
#     rsi = 100 - (100 / (1 + rs))
#     return rsi

# def calculate_macd(data, fast=12, slow=26, signal=9):
#     ema_fast = data.ewm(span=fast, adjust=False).mean()
#     ema_slow = data.ewm(span=slow, adjust=False).mean()
#     macd = ema_fast - ema_slow
#     signal_line = macd.ewm(span=signal, adjust=False).mean()
#     return macd, signal_line

# def calculate_ma(data, window):
#     return data.rolling(window=window).mean()

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/data", methods=["POST"])
# def get_data():
#     data = request.json
#     symbol = data.get("symbol")
#     range_map = {
#         "1d": "1d",
#         "1w": "5d",
#         "1m": "1mo",
#         "3m": "3mo",
#         "1y": "1y",
#         "2y": "2y"
#     }
#     period = range_map.get(data.get("range", "1m"), "1mo")

#     if not symbol:
#         return jsonify({"error": "Symbol is required"}), 400

#     ticker = yf.Ticker(symbol)
#     df = ticker.history(period=period)

#     if df.empty:
#         return jsonify({"error": "No data found"}), 404

#     df["RSI"] = calculate_rsi(df["Close"])
#     df["MACD"], df["Signal"] = calculate_macd(df["Close"])
#     df["MA20"] = calculate_ma(df["Close"], 20)
#     df["MA30"] = calculate_ma(df["Close"], 30)

#     graph_data = {
#         "dates": df.index.strftime("%Y-%m-%d").tolist(),
#         "close": df["Close"].round(2).tolist(),
#         "rsi": df["RSI"].round(2).fillna(0).tolist(),
#         "macd": df["MACD"].round(2).fillna(0).tolist(),
#         "signal": df["Signal"].round(2).fillna(0).tolist(),
#         "ma20": df["MA20"].round(2).fillna(0).tolist(),
#         "ma30": df["MA30"].round(2).fillna(0).tolist()
#     }

#     info = ticker.info
#     financial_data = {
#         "Name": info.get("longName"),
#         "Sector": info.get("sector"),
#         "Industry": info.get("industry"),
#         "Market Cap": info.get("marketCap"),
#         "P/E Ratio": info.get("trailingPE"),
#         "EPS": info.get("trailingEps"),
#         "Dividend Yield": info.get("dividendYield")
#     }

#     return jsonify({
#         "graph": graph_data,
#         "financials": financial_data
#     })

# if __name__ == "__main__":
#     app.run(debug=True)
















#code with not good ma graph

# from flask import Flask, request, jsonify, render_template
# import yfinance as yf
# import pandas as pd
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/companies")
# def get_companies():
#     companies = [
#         {"symbol": "INFY.NS", "name": "Infosys"},
#         {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
#         {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
#         {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
#         {"symbol": "ITC.NS", "name": "ITC"},
#         {"symbol": "WIPRO.NS", "name": "Wipro"},
#         {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
#         {"symbol": "LT.NS", "name": "Larsen & Toubro"},
#         {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
#         {"symbol": "AXISBANK.NS", "name": "Axis Bank"},
#         {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"},
#         {"symbol": "SBIN.NS", "name": "State Bank of India"},
#         {"symbol": "ASIANPAINT.NS", "name": "Asian Paints"},
#         {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance"},
#         {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement"},
#         {"symbol": "MARUTI.NS", "name": "Maruti Suzuki"},
#         {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma"},
#         {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever"},
#         {"symbol": "TITAN.NS", "name": "Titan Company"},
#         {"symbol": "HCLTECH.NS", "name": "HCL Technologies"},
#         {"symbol": "ADANIENT.NS", "name": "Adani Enterprises"},
#         {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy"},
#         {"symbol": "ADANIPORTS.NS", "name": "Adani Ports"},
#         {"symbol": "JSWSTEEL.NS", "name": "JSW Steel"},
#         {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
#         {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation"},
#         {"symbol": "NTPC.NS", "name": "NTPC"},
#         {"symbol": "ONGC.NS", "name": "ONGC"},
#         {"symbol": "COALINDIA.NS", "name": "Coal India"},
#         {"symbol": "BPCL.NS", "name": "Bharat Petroleum"},
#     ]
#     return jsonify(companies)

# # Helper Functions
# def calculate_rsi(data, window=14):
#     delta = data.diff()
#     gain = delta.where(delta > 0, 0)
#     loss = -delta.where(delta < 0, 0)
#     avg_gain = gain.rolling(window=window).mean()
#     avg_loss = loss.rolling(window=window).mean()
#     rs = avg_gain / avg_loss
#     rsi = 100 - (100 / (1 + rs))
#     return rsi

# def calculate_macd(data, fast=12, slow=26, signal=9):
#     ema_fast = data.ewm(span=fast, adjust=False).mean()
#     ema_slow = data.ewm(span=slow, adjust=False).mean()
#     macd = ema_fast - ema_slow
#     signal_line = macd.ewm(span=signal, adjust=False).mean()
#     return macd, signal_line

# def calculate_ma(data, window):
#     return data.rolling(window=window).mean()

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/data", methods=["POST"])
# def get_data():
#     data = request.json
#     symbol = data.get("symbol")
#     ma_range = data.get("maRange", [20, 30])

#     range_map = {
#         "1d": "1d",
#         "1w": "5d",
#         "1m": "1mo",
#         "3m": "3mo",
#         "1y": "1y",
#         "2y": "2y"
#     }
#     period = range_map.get(data.get("range", "1mo"), "1mo")

#     if not symbol:
#         return jsonify({"error": "Symbol is required"}), 400

#     ticker = yf.Ticker(symbol)
#     df = ticker.history(period=period)

#     if df.empty:
#         return jsonify({"error": "No data found"}), 404

#     df["RSI"] = calculate_rsi(df["Close"])
#     df["MACD"], df["Signal"] = calculate_macd(df["Close"])
#     df[f"MA{ma_range[0]}"] = calculate_ma(df["Close"], ma_range[0])
#     df[f"MA{ma_range[1]}"] = calculate_ma(df["Close"], ma_range[1])

#     graph_data = {
#         "dates": df.index.strftime("%Y-%m-%d").tolist(),
#         "close": df["Close"].round(2).tolist(),
#         "rsi": df["RSI"].round(2).fillna(0).tolist(),
#         "macd": df["MACD"].round(2).fillna(0).tolist(),
#         "signal": df["Signal"].round(2).fillna(0).tolist(),
#         f"ma{ma_range[0]}": df[f"MA{ma_range[0]}"] .round(2).fillna(0).tolist(),
#         f"ma{ma_range[1]}": df[f"MA{ma_range[1]}"] .round(2).fillna(0).tolist(),
#     }

#     info = ticker.info
#     financial_data = {
#         "Name": info.get("longName"),
#         "Sector": info.get("sector"),
#         "Industry": info.get("industry"),
#         "Market Cap": info.get("marketCap"),
#         "P/E Ratio": info.get("trailingPE"),
#         "EPS": info.get("trailingEps"),
#         "Dividend Yield": info.get("dividendYield")
#     }

#     return jsonify({
#         "graph": graph_data,
#         "financials": financial_data,
#         "maLabels": [f"MA{ma_range[0]}", f"MA{ma_range[1]}"]
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify, render_template
# import yfinance as yf
# import pandas as pd
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/companies")
# def get_companies():
#     companies = [
#         {"symbol": "INFY.NS", "name": "Infosys"},
#         {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
#         {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
#         {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
#         {"symbol": "ITC.NS", "name": "ITC"},
#         {"symbol": "WIPRO.NS", "name": "Wipro"},
#         {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
#         {"symbol": "LT.NS", "name": "Larsen & Toubro"},
#         {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
#         {"symbol": "AXISBANK.NS", "name": "Axis Bank"},
#         {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"},
#         {"symbol": "SBIN.NS", "name": "State Bank of India"},
#         {"symbol": "ASIANPAINT.NS", "name": "Asian Paints"},
#         {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance"},
#         {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement"},
#         {"symbol": "MARUTI.NS", "name": "Maruti Suzuki"},
#         {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma"},
#         {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever"},
#         {"symbol": "TITAN.NS", "name": "Titan Company"},
#         {"symbol": "HCLTECH.NS", "name": "HCL Technologies"},
#         {"symbol": "ADANIENT.NS", "name": "Adani Enterprises"},
#         {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy"},
#         {"symbol": "ADANIPORTS.NS", "name": "Adani Ports"},
#         {"symbol": "JSWSTEEL.NS", "name": "JSW Steel"},
#         {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
#         {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation"},
#         {"symbol": "NTPC.NS", "name": "NTPC"},
#         {"symbol": "ONGC.NS", "name": "ONGC"},
#         {"symbol": "COALINDIA.NS", "name": "Coal India"},
#         {"symbol": "BPCL.NS", "name": "Bharat Petroleum"},
#     ]
#     return jsonify(companies)

# # Helper Functions
# def calculate_rsi(data, window=14):
#     delta = data.diff()
#     gain = delta.where(delta > 0, 0)
#     loss = -delta.where(delta < 0, 0)
#     avg_gain = gain.rolling(window=window).mean()
#     avg_loss = loss.rolling(window=window).mean()
#     rs = avg_gain / avg_loss
#     rsi = 100 - (100 / (1 + rs))
#     return rsi

# def calculate_macd(data, fast=12, slow=26, signal=9):
#     ema_fast = data.ewm(span=fast, adjust=False).mean()
#     ema_slow = data.ewm(span=slow, adjust=False).mean()
#     macd = ema_fast - ema_slow
#     signal_line = macd.ewm(span=signal, adjust=False).mean()
#     return macd, signal_line

# def calculate_ma(data, window):
#     return data.rolling(window=window).mean()

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/data", methods=["POST"])
# def get_data():
#     data = request.json
#     symbol = data.get("symbol")
#     ma_range = data.get("maRange", [20, 30])

#     range_map = {
#         "1d": "1d",
#         "1w": "5d",
#         "1m": "1mo",
#         "3m": "3mo",
#         "1y": "1y",
#         "2y": "2y"
#     }
#     period = range_map.get(data.get("range", "1mo"), "1mo")

#     if not symbol:
#         return jsonify({"error": "Symbol is required"}), 400

#     ticker = yf.Ticker(symbol)
#     df = ticker.history(period=period)

#     if df.empty:
#         return jsonify({"error": "No data found"}), 404

#     df["RSI"] = calculate_rsi(df["Close"])
#     df["MACD"], df["Signal"] = calculate_macd(df["Close"])
#     df[f"MA{ma_range[0]}"] = calculate_ma(df["Close"], ma_range[0])
#     df[f"MA{ma_range[1]}"] = calculate_ma(df["Close"], ma_range[1])

#     graph_data = {
#         "dates": df.index.strftime("%Y-%m-%d").tolist(),
#         "close": df["Close"].round(2).tolist(),
#         "rsi": df["RSI"].round(2).fillna(0).tolist(),
#         "macd": df["MACD"].round(2).fillna(0).tolist(),
#         "signal": df["Signal"].round(2).fillna(0).tolist(),
#         f"ma{ma_range[0]}": df[f"MA{ma_range[0]}"] .round(2).fillna(0).tolist(),
#         f"ma{ma_range[1]}": df[f"MA{ma_range[1]}"] .round(2).fillna(0).tolist(),
#     }

#     info = ticker.info
#     financial_data = {
#         "Name": info.get("longName"),
#         "Sector": info.get("sector"),
#         "Industry": info.get("industry"),
#         "Market Cap": info.get("marketCap"),
#         "P/E Ratio": info.get("trailingPE"),
#         "EPS": info.get("trailingEps"),
#         "Dividend Yield": info.get("dividendYield")
#     }

#     return jsonify({
#         "graph": graph_data,
#         "financials": financial_data,
#         "maLabels": [f"MA{ma_range[0]}", f"MA{ma_range[1]}"]
#     })

# if __name__ == "__main__":
#     app.run(debug=True)
















# from flask import Flask, request, jsonify, render_template
# import yfinance as yf
# import pandas as pd
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route("/api/companies")
# def get_companies():
#     companies = [
#         {"symbol": "INFY.NS", "name": "Infosys"},
#         {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
#         {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
#         {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
#         {"symbol": "ITC.NS", "name": "ITC"},
#         {"symbol": "WIPRO.NS", "name": "Wipro"},
#         {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
#         {"symbol": "LT.NS", "name": "Larsen & Toubro"},
#         {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
#         {"symbol": "AXISBANK.NS", "name": "Axis Bank"},
#         {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"},
#         {"symbol": "SBIN.NS", "name": "State Bank of India"},
#         {"symbol": "ASIANPAINT.NS", "name": "Asian Paints"},
#         {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance"},
#         {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement"},
#         {"symbol": "MARUTI.NS", "name": "Maruti Suzuki"},
#         {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma"},
#         {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever"},
#         {"symbol": "TITAN.NS", "name": "Titan Company"},
#         {"symbol": "HCLTECH.NS", "name": "HCL Technologies"},
#         {"symbol": "ADANIENT.NS", "name": "Adani Enterprises"},
#         {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy"},
#         {"symbol": "ADANIPORTS.NS", "name": "Adani Ports"},
#         {"symbol": "JSWSTEEL.NS", "name": "JSW Steel"},
#         {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
#         {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation"},
#         {"symbol": "NTPC.NS", "name": "NTPC"},
#         {"symbol": "ONGC.NS", "name": "ONGC"},
#         {"symbol": "COALINDIA.NS", "name": "Coal India"},
#         {"symbol": "BPCL.NS", "name": "Bharat Petroleum"},
#     ]
#     return jsonify(companies)

# # Helper Functions
# def calculate_rsi(data, window=14):
#     delta = data.diff()
#     gain = delta.where(delta > 0, 0)
#     loss = -delta.where(delta < 0, 0)
#     avg_gain = gain.rolling(window=window).mean()
#     avg_loss = loss.rolling(window=window).mean()
#     rs = avg_gain / avg_loss
#     rsi = 100 - (100 / (1 + rs))
#     return rsi

# def calculate_macd(data, fast=12, slow=26, signal=9):
#     ema_fast = data.ewm(span=fast, adjust=False).mean()
#     ema_slow = data.ewm(span=slow, adjust=False).mean()
#     macd = ema_fast - ema_slow
#     signal_line = macd.ewm(span=signal, adjust=False).mean()
#     return macd, signal_line

# def calculate_ma(data, window):
#     return data.rolling(window=window).mean()

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/data", methods=["POST"])
# def get_data():
#     data = request.json
#     symbol = data.get("symbol")
#     ma_range = data.get("maRange", [20, 30])

#     range_map = {
#         "1d": "1d",
#         "1w": "5d",
#         "1m": "1mo",
#         "3m": "3mo",
#         "1y": "1y",
#         "2y": "2y"
#     }
#     period = range_map.get(data.get("range", "1mo"), "1mo")

#     if not symbol:
#         return jsonify({"error": "Symbol is required"}), 400

#     ticker = yf.Ticker(symbol)
#     df = ticker.history(period=period)

#     if df.empty:
#         return jsonify({"error": "No data found"}), 404

#     df["RSI"] = calculate_rsi(df["Close"])
#     df["MACD"], df["Signal"] = calculate_macd(df["Close"])
#     df[f"MA{ma_range[0]}"] = calculate_ma(df["Close"], ma_range[0])
#     df[f"MA{ma_range[1]}"] = calculate_ma(df["Close"], ma_range[1])

#     graph_data = {
#         "dates": df.index.strftime("%Y-%m-%d").tolist(),
#         "close": df["Close"].round(2).tolist(),
#         "rsi": df["RSI"].round(2).fillna(0).tolist(),
#         "macd": df["MACD"].round(2).fillna(0).tolist(),
#         "signal": df["Signal"].round(2).fillna(0).tolist(),
#         f"ma{ma_range[0]}": df[f"MA{ma_range[0]}"] .round(2).fillna(0).tolist(),
#         f"ma{ma_range[1]}": df[f"MA{ma_range[1]}"] .round(2).fillna(0).tolist(),
#     }

#     info = ticker.info
#     financial_data = {
#         "Name": info.get("longName"),
#         "Sector": info.get("sector"),
#         "Industry": info.get("industry"),
#         "Market Cap": info.get("marketCap"),
#         "P/E Ratio": info.get("trailingPE"),
#         "EPS": info.get("trailingEps"),
#         "Dividend Yield": info.get("dividendYield")
#     }

#     return jsonify({
#         "graph": graph_data,
#         "financials": financial_data,
#         "maLabels": [f"MA{ma_range[0]}", f"MA{ma_range[1]}"]
#     })

# if __name__ == "__main__":
#     app.run(debug=True)















from flask import Flask, request, jsonify, render_template
import yfinance as yf
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/companies")
def get_companies():
    companies = [
        {"symbol": "INFY.NS", "name": "Infosys"},
        {"symbol": "TCS.NS", "name": "Tata Consultancy Services"},
        {"symbol": "RELIANCE.NS", "name": "Reliance Industries"},
        {"symbol": "HDFCBANK.NS", "name": "HDFC Bank"},
        {"symbol": "ITC.NS", "name": "ITC"},
        {"symbol": "WIPRO.NS", "name": "Wipro"},
        {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel"},
        {"symbol": "LT.NS", "name": "Larsen & Toubro"},
        {"symbol": "ICICIBANK.NS", "name": "ICICI Bank"},
        {"symbol": "AXISBANK.NS", "name": "Axis Bank"},
        {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank"},
        {"symbol": "SBIN.NS", "name": "State Bank of India"},
        {"symbol": "ASIANPAINT.NS", "name": "Asian Paints"},
        {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance"},
        {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement"},
        {"symbol": "MARUTI.NS", "name": "Maruti Suzuki"},
        {"symbol": "SUNPHARMA.NS", "name": "Sun Pharma"},
        {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever"},
        {"symbol": "TITAN.NS", "name": "Titan Company"},
        {"symbol": "HCLTECH.NS", "name": "HCL Technologies"},
        {"symbol": "ADANIENT.NS", "name": "Adani Enterprises"},
        {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy"},
        {"symbol": "ADANIPORTS.NS", "name": "Adani Ports"},
        {"symbol": "JSWSTEEL.NS", "name": "JSW Steel"},
        {"symbol": "TATAMOTORS.NS", "name": "Tata Motors"},
        {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation"},
        {"symbol": "NTPC.NS", "name": "NTPC"},
        {"symbol": "ONGC.NS", "name": "ONGC"},
        {"symbol": "COALINDIA.NS", "name": "Coal India"},
        {"symbol": "BPCL.NS", "name": "Bharat Petroleum"},
    ]
    return jsonify(companies)

# Helper Functions
def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data, fast=12, slow=26, signal=9):
    ema_fast = data.ewm(span=fast, adjust=False).mean()
    ema_slow = data.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def calculate_ma(data, window):
    return data.rolling(window=window).mean()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data", methods=["POST"])
def get_data():
    data = request.json
    symbol = data.get("symbol")
    ma_range = data.get("maRange", [20, 30])
    custom_months = data.get("customMonths", [])
    custom_years = data.get("customYears", [])

    range_map = {
        "1d": "1d",
        "1w": "5d",
        "1m": "1mo",
        "3m": "3mo",
        "1y": "1y",
        "2y": "2y"
    }
    period = range_map.get(data.get("range", "1mo"), "1mo")

    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400

    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)

    if df.empty:
        return jsonify({"error": "No data found"}), 404

    df["RSI"] = calculate_rsi(df["Close"])
    df["MACD"], df["Signal"] = calculate_macd(df["Close"])
    df[f"MA{ma_range[0]}"] = calculate_ma(df["Close"], ma_range[0])
    df[f"MA{ma_range[1]}"] = calculate_ma(df["Close"], ma_range[1])

    graph_data = {
        "dates": df.index.strftime("%Y-%m-%d").tolist(),
        "close": df["Close"].round(2).tolist(),
        "rsi": df["RSI"].round(2).fillna(0).tolist(),
        "macd": df["MACD"].round(2).fillna(0).tolist(),
        "signal": df["Signal"].round(2).fillna(0).tolist(),
        f"ma{ma_range[0]}": df[f"MA{ma_range[0]}"].round(2).fillna(0).tolist(),
        f"ma{ma_range[1]}": df[f"MA{ma_range[1]}"].round(2).fillna(0).tolist(),
    }

    info = ticker.info
    financial_data = {
        "Name": info.get("longName"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry"),
        "Market Cap": info.get("marketCap"),
        "P/E Ratio": info.get("trailingPE"),
        "EPS": info.get("trailingEps"),
        "Dividend Yield": info.get("dividendYield")
    }

    return jsonify({
        "graph": graph_data,
        "financials": financial_data,
        "maLabels": [f"MA{ma_range[0]}", f"MA{ma_range[1]}"]
    })

if __name__ == "__main__":
    app.run(debug=True)
