# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 563 windows, 15630 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1329 | 51.3 | 49.7 | $-244.55 | -1.8% | $755.45 | -0.7 | done | can't tell from luck |
| value_ev20 | 307 | 32.9 | 35.2 | $-365.92 | -11.9% | $634.08 | -1.6 | done | can't tell from luck |
| trend_filter | 905 | 50.6 | 51.1 | $-497.42 | -5.5% | $502.58 | -1.7 | done | can't tell from luck |
| value_ev10 | 744 | 37.4 | 39.4 | $-736.41 | -9.9% | $263.59 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1585 | 49.3 | 49.8 | $-849.74 | -5.4% | $150.26 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1585 | 50.7 | 51.1 | $-923.43 | -5.8% | $76.57 | -2.4 | done | losing for real |
| value_ev5 | 1105 | 39.5 | 41.3 | $-931.53 | -8.4% | $68.47 | -2.4 | done | losing for real |
| coinflip | 2247 | 49.8 | 50.5 | $-1274.85 | -5.7% | $-274.85 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1329 | 48.7 | 51.2 | $-1313.90 | -9.9% | $-313.90 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2247 | 50.3 | 51.9 | $-1553.70 | -6.9% | $-553.70 | -3.4 | done | losing for real |
| always_up | 2247 | 47.3 | 49.9 | $-2215.90 | -9.9% | $-1215.90 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3528 | 47.6 | 49.2 | $-2716.15 |
| ETH | 3897 | 47.9 | 48.6 | $-2793.31 |
| SOL | 4081 | 47.8 | 48.7 | $-3057.61 |
| XRP | 4124 | 48.5 | 48.6 | $-2340.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
