# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 163 windows, 4160 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 306 | 59.8 | 53.1 | $+313.55 | +10.2% | $1313.55 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 401 | 57.4 | 52.5 | $+265.32 | +6.6% | $1265.32 | +1.4 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 5:00 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 644 | 51.7 | 51.1 | $-192.53 | -3.0% | $807.47 | -0.8 | done | can't tell from luck |
| value_ev10 | 211 | 38.4 | 40.9 | $-232.16 | -11.0% | $767.84 | -1.4 | done | can't tell from luck |
| coinflip | 644 | 50.3 | 50.9 | $-353.85 | -5.5% | $646.15 | -1.4 | done | can't tell from luck |
| value_ev5 | 310 | 39.4 | 42.6 | $-365.80 | -11.8% | $634.20 | -1.9 | done | can't tell from luck |
| trend_filter | 215 | 40.5 | 48.9 | $-433.00 | -20.1% | $567.00 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 306 | 40.2 | 49.1 | $-635.52 | -20.8% | $364.48 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 401 | 42.6 | 49.7 | $-691.88 | -17.3% | $308.12 | -3.5 | done | losing for real |
| always_up | 644 | 46.1 | 50.2 | $-797.89 | -12.4% | $202.11 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 903 | 46.2 | 49.5 | $-803.97 |
| ETH | 1038 | 45.7 | 48.9 | $-1164.48 |
| SOL | 1090 | 47.8 | 49.0 | $-910.42 |
| XRP | 1129 | 50.2 | 49.1 | $-326.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
