# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 685 windows, 18950 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 358 | 34.6 | 35.0 | $-193.12 | -5.4% | $806.88 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1600 | 50.3 | 49.5 | $-448.83 | -2.8% | $551.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 874 | 38.6 | 39.2 | $-475.12 | -5.4% | $524.88 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1949 | 51.6 | 50.9 | $-538.51 | -2.8% | $461.49 | -1.2 | done | can't tell from luck |
| value_ev5 | 1315 | 40.8 | 41.1 | $-601.41 | -4.6% | $398.59 | -1.4 | done | can't tell from luck |
| trend_filter | 1103 | 50.1 | 50.9 | $-621.27 | -5.6% | $378.73 | -1.9 | done | can't tell from luck |
| coinflip | 2734 | 50.2 | 50.3 | $-1164.78 | -4.3% | $-164.78 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1600 | 49.7 | 51.3 | $-1223.87 | -7.6% | $-223.87 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1949 | 48.4 | 49.9 | $-1334.86 | -6.8% | $-334.86 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2734 | 50.7 | 51.8 | $-1536.84 | -5.6% | $-536.84 | -3.0 | done | losing for real |
| always_up | 2734 | 47.4 | 49.6 | $-2317.85 | -8.5% | $-1317.85 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4309 | 48.3 | 49.1 | $-2434.49 |
| ETH | 4718 | 48.2 | 48.6 | $-2830.74 |
| SOL | 4945 | 48.1 | 48.6 | $-2865.82 |
| XRP | 4978 | 48.5 | 48.4 | $-2325.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
