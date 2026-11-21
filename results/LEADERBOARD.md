# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 987 windows, 27428 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2800 | 51.0 | 50.4 | $-874.44 | -3.1% | $125.56 | -1.7 | done | can't tell from luck |
| value_ev10 | 1254 | 37.6 | 39.1 | $-877.53 | -7.0% | $122.47 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2355 | 50.0 | 49.7 | $-1014.04 | -4.3% | $-14.04 | -2.1 | done | losing for real |
| trend_filter | 1643 | 49.7 | 50.9 | $-1162.65 | -7.1% | $-162.65 | -2.9 | done | losing for real |
| value_ev5 | 1898 | 39.5 | 41.0 | $-1264.87 | -6.7% | $-264.87 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2355 | 50.0 | 50.9 | $-1608.78 | -6.8% | $-608.78 | -3.4 | done | losing for real |
| coinflip | 3940 | 50.3 | 50.3 | $-1734.31 | -4.4% | $-734.31 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2800 | 49.0 | 50.3 | $-1897.70 | -6.8% | $-897.70 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3940 | 50.9 | 51.5 | $-2027.12 | -5.1% | $-1027.12 | -3.3 | done | losing for real |
| always_up | 3940 | 46.7 | 49.6 | $-4051.91 | -10.3% | $-3051.91 | -6.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6255 | 48.2 | 49.1 | $-3567.80 |
| ETH | 6817 | 48.0 | 48.5 | $-4472.25 |
| SOL | 7163 | 48.1 | 48.6 | $-4244.53 |
| XRP | 7193 | 48.1 | 48.5 | $-4494.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
