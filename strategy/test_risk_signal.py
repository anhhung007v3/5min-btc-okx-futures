import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from strategy.risk_manager import calculate_risk


print("===== RISK SIGNAL TEST =====")


entry_price = 62800
atr = 120


short_risk = calculate_risk(
    "SHORT",
    entry_price,
    atr
)


long_risk = calculate_risk(
    "LONG",
    entry_price,
    atr
)


print("SHORT:")
print(short_risk)


print("LONG:")
print(long_risk)