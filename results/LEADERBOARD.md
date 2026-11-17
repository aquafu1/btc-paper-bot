# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 629 windows, 17383 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1467 | 51.2 | 49.5 | $-166.03 | -1.1% | $833.97 | -0.4 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1006 | 50.1 | 50.8 | $-573.57 | -5.7% | $426.43 | -1.8 | done | can't tell from luck |
| value_ev10 | 803 | 38.2 | 39.5 | $-590.20 | -7.3% | $409.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 1217 | 40.6 | 41.4 | $-728.64 | -6.0% | $271.36 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1783 | 50.9 | 51.0 | $-823.01 | -4.6% | $176.99 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1783 | 49.1 | 49.9 | $-995.89 | -5.6% | $4.11 | -2.4 | done | losing for real |
| coinflip | 2509 | 50.1 | 50.5 | $-1163.90 | -4.6% | $-163.90 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1467 | 48.8 | 51.4 | $-1409.32 | -9.6% | $-409.32 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2509 | 50.3 | 51.7 | $-1571.26 | -6.3% | $-571.26 | -3.2 | done | losing for real |
| always_up | 2509 | 47.3 | 49.7 | $-2184.60 | -8.7% | $-1184.60 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3944 | 48.2 | 49.2 | $-2452.15 |
| ETH | 4353 | 48.2 | 48.6 | $-2662.10 |
| SOL | 4514 | 47.9 | 48.8 | $-3031.97 |
| XRP | 4572 | 48.4 | 48.5 | $-2334.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
