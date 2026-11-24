# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1284 windows, 34413 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 678 | 33.8 | 35.3 | $-590.36 | -8.7% | $409.64 | -1.7 | done | can't tell from luck |
| value_ev10 | 1655 | 38.5 | 39.2 | $-887.41 | -5.4% | $112.59 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3451 | 50.7 | 50.2 | $-1161.43 | -3.4% | $-161.43 | -2.0 | done | can't tell from luck |
| value_ev5 | 2499 | 40.3 | 41.1 | $-1348.77 | -5.4% | $-348.77 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2884 | 49.4 | 49.4 | $-1379.08 | -4.8% | $-379.08 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2884 | 50.6 | 51.0 | $-1630.40 | -5.7% | $-630.40 | -3.1 | done | losing for real |
| trend_filter | 2034 | 49.0 | 50.5 | $-1633.73 | -8.0% | $-633.73 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 3451 | 49.3 | 50.2 | $-2104.31 | -6.1% | $-1104.31 | -3.6 | done | losing for real |
| coinflip | 4959 | 49.9 | 50.1 | $-2309.16 | -4.7% | $-1309.16 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4959 | 50.5 | 51.4 | $-2756.72 | -5.6% | $-1756.72 | -4.0 | done | losing for real |
| always_up | 4959 | 47.8 | 49.3 | $-3676.61 | -7.4% | $-2676.61 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8220 | 48.0 | 48.8 | $-5000.80 |
| ETH | 8883 | 48.2 | 48.2 | $-4892.96 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
