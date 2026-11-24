# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1327 windows, 35077 settled trades, 414 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 692 | 34.4 | 35.4 | $-508.07 | -7.3% | $491.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1692 | 38.8 | 39.2 | $-780.05 | -4.6% | $219.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3515 | 50.9 | 50.2 | $-1027.91 | -2.9% | $-27.91 | -1.7 | done | can't tell from luck |
| value_ev5 | 2552 | 40.6 | 41.1 | $-1243.07 | -4.9% | $-243.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2946 | 49.4 | 49.4 | $-1428.70 | -4.8% | $-428.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2946 | 50.6 | 50.9 | $-1553.47 | -5.3% | $-553.47 | -2.9 | done | losing for real |
| trend_filter | 2087 | 48.7 | 50.5 | $-1793.38 | -8.6% | $-793.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3515 | 49.1 | 50.2 | $-2208.36 | -6.3% | $-1208.36 | -3.8 | done | losing for real |
| coinflip | 5044 | 49.9 | 50.1 | $-2324.98 | -4.6% | $-1324.98 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5044 | 50.3 | 51.4 | $-3008.52 | -6.0% | $-2008.52 | -4.4 | done | losing for real |
| always_up | 5044 | 47.8 | 49.3 | $-3697.10 | -7.3% | $-2697.10 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8549 | 47.9 | 48.8 | $-5128.36 |
| ETH | 9218 | 48.2 | 48.2 | $-4861.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
