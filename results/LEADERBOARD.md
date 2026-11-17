# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 642 windows, 17737 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1498 | 51.0 | 49.6 | $-223.57 | -1.5% | $776.43 | -0.6 | done | can't tell from luck |
| value_ev20 | 334 | 34.1 | 35.3 | $-256.80 | -7.7% | $743.20 | -1.1 | done | can't tell from luck |
| trend_filter | 1024 | 50.5 | 50.8 | $-508.76 | -5.0% | $491.24 | -1.6 | done | can't tell from luck |
| value_ev10 | 817 | 38.4 | 39.5 | $-557.13 | -6.8% | $442.87 | -1.6 | done | can't tell from luck |
| value_ev5 | 1238 | 40.9 | 41.4 | $-652.25 | -5.3% | $347.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1824 | 51.2 | 51.0 | $-690.06 | -3.8% | $309.94 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1824 | 48.8 | 50.0 | $-1120.30 | -6.1% | $-120.30 | -2.6 | done | losing for real |
| coinflip | 2560 | 50.2 | 50.5 | $-1161.77 | -4.5% | $-161.77 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1498 | 49.0 | 51.4 | $-1357.56 | -9.1% | $-357.56 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2560 | 50.7 | 51.7 | $-1358.94 | -5.3% | $-358.94 | -2.8 | done | losing for real |
| always_up | 2560 | 47.2 | 49.7 | $-2300.04 | -9.0% | $-1300.04 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4029 | 48.3 | 49.3 | $-2388.70 |
| ETH | 4437 | 48.3 | 48.7 | $-2633.74 |
| SOL | 4604 | 48.0 | 48.8 | $-2910.18 |
| XRP | 4667 | 48.5 | 48.5 | $-2254.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
