# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 312 windows, 8335 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 825 | 53.0 | 51.8 | $-164.75 | -2.0% | $835.25 | -0.6 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 1:45 AM | too few trades (155/200) |
| reversal_60m_0.30pct | 679 | 52.4 | 51.7 | $-191.55 | -2.8% | $808.45 | -0.8 | done | can't tell from luck |
| value_ev10 | 399 | 38.1 | 40.5 | $-402.57 | -10.1% | $597.43 | -1.7 | done | can't tell from luck |
| value_ev5 | 595 | 39.7 | 42.2 | $-606.70 | -10.2% | $393.30 | -2.2 | done | losing for real |
| trend_filter | 458 | 45.9 | 50.4 | $-608.46 | -13.3% | $391.54 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 679 | 47.6 | 49.9 | $-634.76 | -9.3% | $365.24 | -2.5 | done | losing for real |
| coinflip | 1240 | 49.9 | 50.9 | $-754.74 | -6.1% | $245.26 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 825 | 47.0 | 49.9 | $-807.10 | -9.8% | $192.90 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1240 | 48.8 | 51.4 | $-1120.16 | -9.0% | $-120.16 | -3.3 | done | losing for real |
| always_up | 1240 | 47.1 | 50.4 | $-1320.35 | -10.6% | $-320.35 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1870 | 46.4 | 49.3 | $-1877.41 |
| ETH | 2088 | 47.0 | 48.8 | $-1948.39 |
| SOL | 2169 | 47.9 | 49.4 | $-1745.06 |
| XRP | 2208 | 48.6 | 49.1 | $-1220.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
