# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 820 windows, 22519 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 416 | 33.7 | 35.0 | $-330.80 | -8.0% | $669.20 | -1.2 | done | can't tell from luck |
| value_ev10 | 1029 | 37.8 | 39.2 | $-716.63 | -7.0% | $283.37 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1884 | 49.9 | 49.6 | $-784.97 | -4.2% | $215.03 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2299 | 50.8 | 50.6 | $-863.42 | -3.8% | $136.58 | -1.8 | done | can't tell from luck |
| trend_filter | 1323 | 49.9 | 50.8 | $-882.36 | -6.7% | $117.64 | -2.5 | done | losing for real |
| value_ev5 | 1557 | 40.1 | 41.1 | $-940.83 | -6.0% | $59.17 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1884 | 50.1 | 51.2 | $-1311.60 | -7.0% | $-311.60 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2299 | 49.2 | 50.2 | $-1372.67 | -6.0% | $-372.67 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3276 | 51.3 | 51.6 | $-1466.05 | -4.5% | $-466.05 | -2.6 | done | losing for real |
| coinflip | 3276 | 50.1 | 50.3 | $-1485.00 | -4.5% | $-485.00 | -2.6 | done | losing for real |
| always_up | 3276 | 47.4 | 49.6 | $-2871.91 | -8.8% | $-1871.91 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5109 | 48.2 | 49.1 | $-3099.63 |
| ETH | 5604 | 48.1 | 48.5 | $-3686.23 |
| SOL | 5876 | 48.3 | 48.6 | $-3217.35 |
| XRP | 5930 | 48.5 | 48.5 | $-3023.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
