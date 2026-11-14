# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 358 windows, 9661 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 8:45 PM | too few trades (186/200) |
| value_ev10 | 465 | 40.0 | 40.3 | $-211.42 | -4.5% | $788.58 | -0.8 | done | can't tell from luck |
| value_ev5 | 690 | 41.6 | 42.0 | $-340.39 | -4.9% | $659.61 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 959 | 52.0 | 52.0 | $-403.34 | -4.2% | $596.66 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 796 | 49.0 | 49.7 | $-465.99 | -5.9% | $534.01 | -1.7 | done | can't tell from luck |
| trend_filter | 535 | 48.2 | 50.5 | $-473.12 | -8.8% | $526.88 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 796 | 51.0 | 52.0 | $-473.21 | -5.9% | $526.79 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 959 | 48.0 | 49.7 | $-728.88 | -7.6% | $271.12 | -2.4 | done | losing for real |
| coinflip | 1425 | 50.0 | 50.8 | $-789.76 | -5.5% | $210.24 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1425 | 49.4 | 51.5 | $-1114.15 | -7.8% | $-114.15 | -3.1 | done | losing for real |
| always_up | 1425 | 46.2 | 50.6 | $-1768.68 | -12.4% | $-768.68 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2171 | 47.3 | 49.3 | $-1804.48 |
| ETH | 2431 | 47.6 | 48.8 | $-1764.71 |
| SOL | 2504 | 48.0 | 49.4 | $-1905.76 |
| XRP | 2555 | 48.7 | 49.1 | $-1352.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
