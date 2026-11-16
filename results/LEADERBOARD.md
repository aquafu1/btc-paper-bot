# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 507 windows, 13968 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1183 | 51.1 | 49.8 | $-201.40 | -1.7% | $798.60 | -0.6 | done | can't tell from luck |
| value_ev10 | 658 | 38.1 | 39.7 | $-490.51 | -7.5% | $509.49 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1414 | 49.9 | 49.6 | $-528.24 | -3.7% | $471.76 | -1.4 | done | can't tell from luck |
| trend_filter | 817 | 49.6 | 50.7 | $-538.44 | -6.6% | $461.56 | -1.9 | done | can't tell from luck |
| value_ev5 | 975 | 40.0 | 41.5 | $-703.88 | -7.2% | $296.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1414 | 50.1 | 51.6 | $-981.41 | -6.9% | $18.59 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1183 | 48.9 | 51.4 | $-1082.97 | -9.2% | $-82.97 | -3.2 | done | losing for real |
| coinflip | 2020 | 50.0 | 50.7 | $-1093.91 | -5.4% | $-93.91 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 2020 | 49.7 | 51.6 | $-1492.00 | -7.4% | $-492.00 | -3.4 | done | losing for real |
| always_up | 2020 | 46.3 | 50.1 | $-2364.92 | -11.7% | $-1364.92 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3158 | 47.3 | 49.2 | $-2540.42 |
| ETH | 3489 | 48.0 | 48.7 | $-2265.32 |
| SOL | 3643 | 47.6 | 49.0 | $-2752.13 |
| XRP | 3678 | 48.3 | 48.8 | $-2098.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
