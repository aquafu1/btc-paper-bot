# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1390 windows, 35943 settled trades, 381 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 722 | 34.6 | 35.3 | $-497.54 | -6.9% | $502.46 | -1.4 | done | can't tell from luck |
| value_ev10 | 1745 | 38.9 | 39.2 | $-764.97 | -4.4% | $235.03 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3589 | 50.8 | 50.1 | $-1048.23 | -2.9% | $-48.23 | -1.7 | done | can't tell from luck |
| value_ev5 | 2628 | 40.5 | 41.1 | $-1269.38 | -4.8% | $-269.38 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3012 | 49.3 | 49.3 | $-1478.05 | -4.9% | $-478.05 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3012 | 50.7 | 50.9 | $-1553.13 | -5.2% | $-553.13 | -2.9 | done | losing for real |
| trend_filter | 2133 | 48.6 | 50.4 | $-1863.77 | -8.7% | $-863.77 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3589 | 49.2 | 50.2 | $-2193.25 | -6.1% | $-1193.25 | -3.7 | done | losing for real |
| coinflip | 5171 | 50.0 | 50.0 | $-2227.59 | -4.3% | $-1227.59 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5171 | 50.2 | 51.3 | $-3182.85 | -6.2% | $-2182.85 | -4.6 | done | losing for real |
| always_up | 5171 | 47.9 | 49.3 | $-3664.15 | -7.1% | $-2664.15 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8971 | 48.0 | 48.8 | $-5008.64 |
| ETH | 9662 | 48.1 | 48.1 | $-5150.04 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
