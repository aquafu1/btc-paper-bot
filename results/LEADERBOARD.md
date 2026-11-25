# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1367 windows, 35603 settled trades, 421 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 707 | 34.2 | 35.4 | $-549.64 | -7.8% | $450.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1724 | 38.7 | 39.2 | $-826.30 | -4.8% | $173.70 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3558 | 50.9 | 50.1 | $-976.27 | -2.7% | $23.73 | -1.6 | done | can't tell from luck |
| value_ev5 | 2600 | 40.4 | 41.1 | $-1318.39 | -5.1% | $-318.39 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2984 | 49.3 | 49.4 | $-1462.31 | -4.9% | $-462.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2984 | 50.7 | 50.9 | $-1549.88 | -5.2% | $-549.88 | -2.9 | done | losing for real |
| trend_filter | 2116 | 48.6 | 50.4 | $-1860.35 | -8.8% | $-860.35 | -4.1 | done | losing for real |
| coinflip | 5124 | 50.0 | 50.0 | $-2219.62 | -4.3% | $-1219.62 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3558 | 49.1 | 50.2 | $-2247.90 | -6.3% | $-1247.90 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5124 | 50.1 | 51.3 | $-3218.34 | -6.3% | $-2218.34 | -4.6 | done | losing for real |
| always_up | 5124 | 47.8 | 49.3 | $-3716.90 | -7.3% | $-2716.90 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8805 | 47.8 | 48.8 | $-5242.32 |
| ETH | 9488 | 48.1 | 48.1 | $-5119.34 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
