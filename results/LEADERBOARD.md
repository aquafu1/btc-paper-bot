# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1372 windows, 35701 settled trades, 414 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 712 | 34.3 | 35.3 | $-547.28 | -7.7% | $452.72 | -1.6 | done | can't tell from luck |
| value_ev10 | 1731 | 38.8 | 39.2 | $-796.33 | -4.6% | $203.67 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3568 | 50.8 | 50.1 | $-1043.45 | -2.9% | $-43.45 | -1.7 | done | can't tell from luck |
| value_ev5 | 2607 | 40.5 | 41.1 | $-1288.42 | -4.9% | $-288.42 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2993 | 49.3 | 49.4 | $-1473.06 | -4.9% | $-473.06 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2993 | 50.7 | 50.9 | $-1534.00 | -5.1% | $-534.00 | -2.9 | done | losing for real |
| trend_filter | 2121 | 48.6 | 50.4 | $-1857.96 | -8.8% | $-857.96 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3568 | 49.2 | 50.2 | $-2181.30 | -6.1% | $-1181.30 | -3.7 | done | losing for real |
| coinflip | 5136 | 50.1 | 50.0 | $-2189.75 | -4.3% | $-1189.75 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5136 | 50.1 | 51.3 | $-3200.60 | -6.2% | $-2200.60 | -4.6 | done | losing for real |
| always_up | 5136 | 47.9 | 49.3 | $-3667.24 | -7.1% | $-2667.24 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8854 | 47.9 | 48.8 | $-5099.99 |
| ETH | 9537 | 48.1 | 48.1 | $-5095.16 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
