# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 751 windows, 20728 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 392 | 33.7 | 34.9 | $-299.69 | -7.6% | $700.31 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2119 | 51.5 | 50.5 | $-478.13 | -2.3% | $521.87 | -1.0 | done | can't tell from luck |
| value_ev10 | 951 | 37.9 | 39.1 | $-636.68 | -6.7% | $363.32 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1752 | 50.0 | 49.6 | $-653.53 | -3.7% | $346.47 | -1.6 | done | can't tell from luck |
| value_ev5 | 1433 | 40.3 | 41.1 | $-808.06 | -5.6% | $191.94 | -1.8 | done | can't tell from luck |
| trend_filter | 1222 | 49.8 | 50.9 | $-821.04 | -6.7% | $178.96 | -2.4 | done | losing for real |
| coinflip | 2996 | 50.4 | 50.3 | $-1119.58 | -3.7% | $-119.58 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1752 | 50.0 | 51.2 | $-1213.91 | -6.9% | $-213.91 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2119 | 48.5 | 50.2 | $-1557.22 | -7.3% | $-557.22 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2996 | 50.7 | 51.8 | $-1706.34 | -5.7% | $-706.34 | -3.2 | done | losing for real |
| always_up | 2996 | 46.9 | 49.6 | $-2829.63 | -9.4% | $-1829.63 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4698 | 48.1 | 49.1 | $-2889.57 |
| ETH | 5163 | 48.1 | 48.5 | $-3357.90 |
| SOL | 5400 | 48.0 | 48.6 | $-3212.10 |
| XRP | 5467 | 48.5 | 48.5 | $-2664.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
