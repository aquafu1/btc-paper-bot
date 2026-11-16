# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 508 windows, 14000 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1187 | 50.9 | 49.8 | $-241.40 | -2.0% | $758.60 | -0.7 | done | can't tell from luck |
| value_ev10 | 658 | 38.1 | 39.7 | $-490.51 | -7.5% | $509.49 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1418 | 49.7 | 49.6 | $-568.24 | -4.0% | $431.76 | -1.5 | done | can't tell from luck |
| trend_filter | 821 | 49.3 | 50.7 | $-578.44 | -7.0% | $421.56 | -2.1 | done | losing for real |
| value_ev5 | 975 | 40.0 | 41.5 | $-703.88 | -7.2% | $296.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1418 | 50.3 | 51.6 | $-951.39 | -6.7% | $48.61 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1187 | 49.1 | 51.4 | $-1052.95 | -8.9% | $-52.95 | -3.1 | done | losing for real |
| coinflip | 2024 | 50.0 | 50.7 | $-1081.81 | -5.3% | $-81.81 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 2024 | 49.6 | 51.6 | $-1532.00 | -7.6% | $-532.00 | -3.5 | done | losing for real |
| always_up | 2024 | 46.4 | 50.1 | $-2334.90 | -11.5% | $-1334.90 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3166 | 47.3 | 49.2 | $-2552.36 |
| ETH | 3497 | 48.0 | 48.7 | $-2276.09 |
| SOL | 3651 | 47.6 | 49.0 | $-2761.02 |
| XRP | 3686 | 48.3 | 48.8 | $-2124.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
