# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 382 windows, 10425 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 9:45 PM | too few trades (196/200) |
| value_ev10 | 505 | 39.8 | 40.5 | $-237.29 | -4.7% | $762.71 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 872 | 50.0 | 49.8 | $-341.41 | -3.9% | $658.59 | -1.2 | done | can't tell from luck |
| value_ev5 | 745 | 41.5 | 42.1 | $-366.06 | -4.9% | $633.94 | -1.2 | done | can't tell from luck |
| trend_filter | 580 | 48.4 | 50.5 | $-487.94 | -8.4% | $512.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1043 | 51.5 | 52.1 | $-541.05 | -5.2% | $458.95 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1043 | 48.5 | 49.7 | $-619.76 | -5.9% | $380.24 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 872 | 50.0 | 52.1 | $-683.13 | -7.8% | $316.87 | -2.4 | done | losing for real |
| coinflip | 1523 | 50.0 | 50.8 | $-789.31 | -5.2% | $210.69 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1523 | 49.2 | 51.5 | $-1208.11 | -7.9% | $-208.11 | -3.2 | done | losing for real |
| always_up | 1523 | 45.6 | 50.7 | $-2070.88 | -13.6% | $-1070.88 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2351 | 47.3 | 49.4 | $-1881.26 |
| ETH | 2621 | 47.5 | 48.9 | $-1916.20 |
| SOL | 2696 | 47.8 | 49.4 | $-2046.75 |
| XRP | 2757 | 48.5 | 49.1 | $-1527.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
