# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 727 windows, 20023 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2052 | 51.8 | 50.7 | $-412.79 | -2.0% | $587.21 | -0.9 | done | can't tell from luck |
| value_ev10 | 917 | 38.1 | 39.1 | $-585.38 | -6.4% | $414.62 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1678 | 50.0 | 49.5 | $-593.09 | -3.5% | $406.91 | -1.4 | done | can't tell from luck |
| value_ev5 | 1385 | 40.6 | 41.1 | $-680.43 | -4.9% | $319.57 | -1.5 | done | can't tell from luck |
| trend_filter | 1171 | 49.9 | 50.9 | $-748.12 | -6.4% | $251.88 | -2.2 | done | losing for real |
| coinflip | 2903 | 50.3 | 50.3 | $-1175.39 | -4.0% | $-175.39 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1678 | 50.0 | 51.3 | $-1175.84 | -7.0% | $-175.84 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2052 | 48.2 | 50.1 | $-1515.32 | -7.4% | $-515.32 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2903 | 50.7 | 51.8 | $-1637.08 | -5.6% | $-637.08 | -3.1 | done | losing for real |
| always_up | 2903 | 47.1 | 49.6 | $-2630.28 | -9.1% | $-1630.28 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4527 | 48.1 | 49.1 | $-2865.71 |
| ETH | 4991 | 48.1 | 48.5 | $-3033.73 |
| SOL | 5219 | 48.1 | 48.7 | $-3062.58 |
| XRP | 5286 | 48.5 | 48.5 | $-2525.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
