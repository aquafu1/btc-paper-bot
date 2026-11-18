# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 686 windows, 18966 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 358 | 34.6 | 35.0 | $-193.12 | -5.4% | $806.88 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1601 | 50.3 | 49.5 | $-437.83 | -2.7% | $562.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 875 | 38.6 | 39.2 | $-459.28 | -5.2% | $540.72 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1951 | 51.6 | 50.9 | $-558.51 | -2.9% | $441.49 | -1.3 | done | can't tell from luck |
| value_ev5 | 1317 | 40.9 | 41.1 | $-574.58 | -4.4% | $425.42 | -1.3 | done | can't tell from luck |
| trend_filter | 1104 | 50.2 | 50.9 | $-610.27 | -5.5% | $389.73 | -1.9 | done | can't tell from luck |
| coinflip | 2736 | 50.2 | 50.3 | $-1158.94 | -4.2% | $-158.94 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1601 | 49.7 | 51.4 | $-1233.87 | -7.7% | $-233.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1951 | 48.4 | 49.9 | $-1308.02 | -6.7% | $-308.02 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2736 | 50.7 | 51.8 | $-1535.84 | -5.6% | $-535.84 | -3.0 | done | losing for real |
| always_up | 2736 | 47.4 | 49.6 | $-2291.01 | -8.4% | $-1291.01 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4309 | 48.3 | 49.1 | $-2434.49 |
| ETH | 4725 | 48.3 | 48.6 | $-2771.57 |
| SOL | 4945 | 48.1 | 48.6 | $-2865.82 |
| XRP | 4987 | 48.6 | 48.4 | $-2289.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
