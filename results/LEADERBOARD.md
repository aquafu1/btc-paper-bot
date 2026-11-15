# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 423 windows, 11626 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 996 | 50.5 | 50.0 | $-324.34 | -3.3% | $675.66 | -1.0 | done | can't tell from luck |
| value_ev10 | 541 | 39.4 | 40.4 | $-331.49 | -6.1% | $668.51 | -1.2 | done | can't tell from luck |
| value_ev5 | 814 | 41.4 | 42.1 | $-448.73 | -5.5% | $551.27 | -1.4 | done | can't tell from luck |
| trend_filter | 665 | 49.3 | 50.7 | $-452.59 | -6.8% | $547.41 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1176 | 49.0 | 50.0 | $-656.62 | -5.6% | $343.38 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1176 | 51.0 | 51.8 | $-666.13 | -5.7% | $333.87 | -2.0 | done | losing for real |
| coinflip | 1684 | 50.5 | 51.0 | $-762.62 | -4.5% | $237.38 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 996 | 49.5 | 51.9 | $-857.56 | -8.6% | $142.44 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1684 | 49.4 | 51.6 | $-1301.08 | -7.7% | $-301.08 | -3.3 | done | losing for real |
| always_up | 1684 | 46.0 | 50.7 | $-2142.76 | -12.7% | $-1142.76 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2635 | 47.7 | 49.4 | $-1928.96 |
| ETH | 2921 | 47.9 | 49.0 | $-1868.03 |
| SOL | 3011 | 47.6 | 49.5 | $-2564.40 |
| XRP | 3059 | 48.7 | 49.3 | $-1749.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
