# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1380 windows, 35808 settled trades, 408 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 718 | 34.4 | 35.3 | $-534.88 | -7.4% | $465.12 | -1.5 | done | can't tell from luck |
| value_ev10 | 1739 | 38.8 | 39.2 | $-803.93 | -4.6% | $196.07 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3578 | 50.8 | 50.1 | $-1046.85 | -2.9% | $-46.85 | -1.7 | done | can't tell from luck |
| value_ev5 | 2617 | 40.4 | 41.1 | $-1316.02 | -5.0% | $-316.02 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 3001 | 49.2 | 49.3 | $-1504.34 | -5.0% | $-504.34 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3001 | 50.8 | 50.9 | $-1518.09 | -5.1% | $-518.09 | -2.8 | done | losing for real |
| trend_filter | 2126 | 48.4 | 50.4 | $-1907.96 | -9.0% | $-907.96 | -4.2 | done | losing for real |
| coinflip | 5150 | 50.1 | 50.0 | $-2188.66 | -4.2% | $-1188.66 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3578 | 49.2 | 50.2 | $-2190.42 | -6.1% | $-1190.42 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5150 | 50.1 | 51.3 | $-3229.00 | -6.3% | $-2229.00 | -4.6 | done | losing for real |
| always_up | 5150 | 47.9 | 49.3 | $-3672.70 | -7.1% | $-2672.70 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8907 | 47.9 | 48.8 | $-5108.29 |
| ETH | 9591 | 48.1 | 48.1 | $-5220.33 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
