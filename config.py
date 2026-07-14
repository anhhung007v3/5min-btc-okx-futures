# ==========================================
# ACCOUNT
# ==========================================

# Tổng vốn của dự án (để thống kê)
TOTAL_CAPITAL = 100

# Số tiền thực sự có trong Futures Wallet
FUTURES_BALANCE = 20

# Giới hạn Margin tối đa cho mỗi lệnh
MAX_MARGIN_PER_TRADE = 5

# Đòn bẩy
LEVERAGE = 20

# ==========================================
# RISK
# ==========================================

# Rủi ro mỗi lệnh (%)
RISK_PERCENT = 1

# ==========================================
# TRADING
# ==========================================

SYMBOL = "BTC-USDT-SWAP"

TIMEFRAME = "5m"

PAPER_MODE = True

DRY_RUN = True


# ==========================================
# BACKWARD COMPATIBILITY
# ==========================================

# Tạm thời giữ để code cũ vẫn chạy
ACCOUNT_SIZE = FUTURES_BALANCE