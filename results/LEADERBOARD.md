# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 324 windows, 8662 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 700 | 53.3 | 51.7 | $-84.58 | -1.2% | $915.42 | -0.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 862 | 52.9 | 51.9 | $-203.41 | -2.4% | $796.59 | -0.7 | done | can't tell from luck |
| value_ev20 | 163 | 33.7 | 36.8 | $-212.09 | -13.0% | $787.91 | -1.3 | Sun 12:15 AM | too few trades (163/200) |
| value_ev10 | 414 | 37.7 | 40.5 | $-459.41 | -11.1% | $540.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 621 | 39.6 | 42.2 | $-645.19 | -10.4% | $354.81 | -2.3 | done | losing for real |
| trend_filter | 476 | 45.0 | 50.4 | $-718.15 | -15.1% | $281.85 | -3.4 | done | losing for real |
| coinflip | 1288 | 50.1 | 51.0 | $-766.55 | -6.0% | $233.45 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 700 | 46.7 | 49.9 | $-776.76 | -11.1% | $223.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 862 | 47.1 | 49.8 | $-826.98 | -9.6% | $173.02 | -2.9 | done | losing for real |
| always_up | 1288 | 47.9 | 50.5 | $-1194.00 | -9.3% | $-194.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1288 | 48.2 | 51.4 | $-1324.74 | -10.3% | $-324.74 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1941 | 46.3 | 49.4 | $-2006.46 |
| ETH | 2175 | 46.8 | 48.8 | $-2149.60 |
| SOL | 2255 | 48.1 | 49.4 | $-1787.29 |
| XRP | 2291 | 48.7 | 49.2 | $-1268.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
