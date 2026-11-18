# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 675 windows, 18712 settled trades, 25 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 350 | 34.9 | 35.1 | $-174.96 | -5.0% | $825.04 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1591 | 50.5 | 49.6 | $-374.53 | -2.4% | $625.47 | -0.9 | done | can't tell from luck |
| value_ev10 | 862 | 38.7 | 39.3 | $-445.56 | -5.2% | $554.44 | -1.2 | done | can't tell from luck |
| trend_filter | 1091 | 50.4 | 50.9 | $-552.53 | -5.1% | $447.47 | -1.7 | done | can't tell from luck |
| value_ev5 | 1299 | 40.8 | 41.2 | $-610.92 | -4.7% | $389.08 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1920 | 51.4 | 50.9 | $-631.11 | -3.3% | $368.89 | -1.5 | done | can't tell from luck |
| coinflip | 2696 | 50.2 | 50.4 | $-1155.63 | -4.3% | $-155.63 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1920 | 48.6 | 49.9 | $-1210.61 | -6.3% | $-210.61 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1591 | 49.5 | 51.3 | $-1266.70 | -8.0% | $-266.70 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2696 | 50.7 | 51.7 | $-1461.00 | -5.4% | $-461.00 | -2.9 | done | losing for real |
| always_up | 2696 | 47.3 | 49.7 | $-2357.55 | -8.7% | $-1357.55 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4257 | 48.3 | 49.2 | $-2451.15 |
| ETH | 4666 | 48.3 | 48.6 | $-2714.32 |
| SOL | 4872 | 48.2 | 48.7 | $-2748.95 |
| XRP | 4917 | 48.5 | 48.5 | $-2326.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
