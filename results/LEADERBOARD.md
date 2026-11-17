# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 637 windows, 17608 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1489 | 51.2 | 49.6 | $-178.24 | -1.2% | $821.76 | -0.5 | done | can't tell from luck |
| value_ev20 | 331 | 33.8 | 35.3 | $-284.70 | -8.6% | $715.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1019 | 50.4 | 50.8 | $-518.85 | -5.1% | $481.15 | -1.7 | done | can't tell from luck |
| value_ev10 | 810 | 38.3 | 39.5 | $-589.42 | -7.3% | $410.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1228 | 40.6 | 41.4 | $-728.92 | -5.9% | $271.08 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1811 | 50.9 | 51.1 | $-814.53 | -4.5% | $185.47 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1811 | 49.1 | 50.0 | $-1030.98 | -5.7% | $-30.98 | -2.4 | done | losing for real |
| coinflip | 2540 | 50.1 | 50.5 | $-1186.65 | -4.7% | $-186.65 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1489 | 48.8 | 51.4 | $-1427.85 | -9.6% | $-427.85 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2540 | 50.6 | 51.7 | $-1429.46 | -5.6% | $-429.46 | -2.9 | done | losing for real |
| always_up | 2540 | 47.2 | 49.7 | $-2275.20 | -9.0% | $-1275.20 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4000 | 48.3 | 49.3 | $-2418.89 |
| ETH | 4407 | 48.2 | 48.6 | $-2639.97 |
| SOL | 4569 | 48.0 | 48.8 | $-3026.73 |
| XRP | 4632 | 48.4 | 48.6 | $-2379.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
