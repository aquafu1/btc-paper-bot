# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 673 windows, 18652 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 348 | 34.5 | 35.2 | $-217.83 | -6.3% | $782.17 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1588 | 50.6 | 49.6 | $-344.53 | -2.2% | $655.47 | -0.9 | done | can't tell from luck |
| value_ev10 | 858 | 38.5 | 39.4 | $-525.66 | -6.1% | $474.34 | -1.5 | done | can't tell from luck |
| trend_filter | 1089 | 50.5 | 50.9 | $-532.53 | -4.9% | $467.47 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1912 | 51.4 | 50.9 | $-615.93 | -3.2% | $384.07 | -1.4 | done | can't tell from luck |
| value_ev5 | 1293 | 40.7 | 41.3 | $-671.02 | -5.2% | $328.98 | -1.6 | done | can't tell from luck |
| coinflip | 2688 | 50.2 | 50.4 | $-1138.47 | -4.2% | $-138.47 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1912 | 48.6 | 50.0 | $-1250.71 | -6.5% | $-250.71 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1588 | 49.4 | 51.3 | $-1310.14 | -8.3% | $-310.14 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2688 | 50.7 | 51.8 | $-1470.40 | -5.5% | $-470.40 | -2.9 | done | losing for real |
| always_up | 2688 | 47.3 | 49.7 | $-2397.65 | -8.9% | $-1397.65 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4241 | 48.3 | 49.2 | $-2507.24 |
| ETH | 4652 | 48.3 | 48.6 | $-2749.46 |
| SOL | 4855 | 48.2 | 48.7 | $-2826.19 |
| XRP | 4904 | 48.5 | 48.5 | $-2391.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
