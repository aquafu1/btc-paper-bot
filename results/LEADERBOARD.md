# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 725 windows, 19967 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2045 | 51.9 | 50.7 | $-368.62 | -1.8% | $631.38 | -0.8 | done | can't tell from luck |
| value_ev10 | 917 | 38.1 | 39.1 | $-585.38 | -6.4% | $414.62 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1671 | 49.9 | 49.5 | $-633.85 | -3.8% | $366.15 | -1.5 | done | can't tell from luck |
| value_ev5 | 1384 | 40.7 | 41.1 | $-670.43 | -4.8% | $329.57 | -1.5 | done | can't tell from luck |
| trend_filter | 1171 | 49.9 | 50.9 | $-748.12 | -6.4% | $251.88 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1671 | 50.1 | 51.3 | $-1120.85 | -6.7% | $-120.85 | -2.8 | done | losing for real |
| coinflip | 2894 | 50.3 | 50.3 | $-1173.78 | -4.1% | $-173.78 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2045 | 48.1 | 50.0 | $-1553.92 | -7.6% | $-553.92 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2894 | 50.9 | 51.8 | $-1562.09 | -5.4% | $-562.09 | -3.0 | done | losing for real |
| always_up | 2894 | 47.2 | 49.6 | $-2555.29 | -8.8% | $-1555.29 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4514 | 48.1 | 49.1 | $-2827.44 |
| ETH | 4979 | 48.2 | 48.5 | $-3006.67 |
| SOL | 5207 | 48.1 | 48.7 | $-3019.92 |
| XRP | 5267 | 48.6 | 48.4 | $-2452.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
