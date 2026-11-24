# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1325 windows, 35060 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 690 | 34.3 | 35.3 | $-507.07 | -7.3% | $492.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1690 | 38.8 | 39.2 | $-779.05 | -4.6% | $220.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3514 | 50.9 | 50.2 | $-1036.91 | -3.0% | $-36.91 | -1.7 | done | can't tell from luck |
| value_ev5 | 2550 | 40.5 | 41.1 | $-1242.07 | -4.9% | $-242.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2946 | 49.4 | 49.4 | $-1428.70 | -4.8% | $-428.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2946 | 50.6 | 50.9 | $-1553.47 | -5.3% | $-553.47 | -2.9 | done | losing for real |
| trend_filter | 2087 | 48.7 | 50.5 | $-1793.38 | -8.6% | $-793.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3514 | 49.1 | 50.2 | $-2198.36 | -6.3% | $-1198.36 | -3.7 | done | losing for real |
| coinflip | 5041 | 49.9 | 50.0 | $-2329.71 | -4.6% | $-1329.71 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5041 | 50.3 | 51.4 | $-3013.25 | -6.0% | $-2013.25 | -4.4 | done | losing for real |
| always_up | 5041 | 47.8 | 49.3 | $-3699.70 | -7.3% | $-2699.70 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8546 | 47.9 | 48.8 | $-5115.23 |
| ETH | 9204 | 48.2 | 48.2 | $-4882.21 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
