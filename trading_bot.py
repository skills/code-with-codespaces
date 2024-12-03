import ccxt
import pandas as pd
import time

# إعداد منصة التداول
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# دالة لجلب بيانات السوق
def fetch_data(symbol, timeframe='1m', limit=100):
    bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# دالة لاتخاذ قرار التداول
def trading_decision(df):
    # استراتيجية بسيطة تعتمد على المتوسط المتحرك
    df['SMA'] = df['close'].rolling(window=20).mean()
    if df['close'].iloc[-1] > df['SMA'].iloc[-1]:
        return 'buy'
    elif df['close'].iloc[-1] < df['SMA'].iloc[-1]:
        return 'sell'
    else:
        return 'hold'

# دالة لتنفيذ التداول
def execute_trade(symbol, decision):
    if decision == 'buy':
        order = exchange.create_market_buy_order(symbol, 0.001)  # شراء 0.001 بيتكوين
    elif decision == 'sell':
        order = exchange.create_market_sell_order(symbol, 0.001)  # بيع 0.001 بيتكوين
    print(order)

# تشغيل الروبوت
symbol = 'BTC/USDT'
while True:
    df = fetch_data(symbol)
    decision = trading_decision(df)
    execute_trade(symbol, decision)
    time.sleep(60)  # الانتظار لمدة دقيقة قبل التحقق مرة أخرى
