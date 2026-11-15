# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 412 windows, 11297 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 204 | 35.8 | 36.5 | $-106.95 | -5.2% | $893.05 | -0.6 | done | can't tell from luck |
| value_ev10 | 530 | 40.2 | 40.5 | $-221.49 | -4.2% | $778.51 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 964 | 50.8 | 50.0 | $-234.67 | -2.4% | $765.33 | -0.8 | done | can't tell from luck |
| value_ev5 | 798 | 42.1 | 42.2 | $-310.32 | -3.9% | $689.68 | -1.0 | done | can't tell from luck |
| trend_filter | 641 | 49.9 | 50.7 | $-339.37 | -5.3% | $660.63 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1138 | 49.2 | 49.9 | $-550.00 | -4.8% | $450.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1138 | 50.8 | 51.9 | $-695.88 | -6.1% | $304.12 | -2.2 | done | losing for real |
| coinflip | 1640 | 50.2 | 50.9 | $-801.35 | -4.9% | $198.65 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 964 | 49.2 | 51.9 | $-868.50 | -9.0% | $131.50 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1640 | 49.7 | 51.6 | $-1147.99 | -7.0% | $-147.99 | -2.9 | done | losing for real |
| always_up | 1640 | 45.8 | 50.6 | $-2124.85 | -13.0% | $-1124.85 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2553 | 47.7 | 49.5 | $-1784.44 |
| ETH | 2839 | 48.0 | 49.0 | $-1717.01 |
| SOL | 2925 | 47.8 | 49.5 | $-2306.13 |
| XRP | 2980 | 48.8 | 49.3 | $-1593.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
