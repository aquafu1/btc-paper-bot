# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 510 windows, 14062 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1194 | 51.1 | 49.8 | $-191.83 | -1.6% | $808.17 | -0.6 | done | can't tell from luck |
| value_ev10 | 659 | 38.1 | 39.7 | $-500.51 | -7.6% | $499.49 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1426 | 49.7 | 49.6 | $-565.70 | -4.0% | $434.30 | -1.5 | done | can't tell from luck |
| trend_filter | 824 | 49.4 | 50.7 | $-569.51 | -6.9% | $430.49 | -2.0 | done | losing for real |
| value_ev5 | 976 | 40.0 | 41.5 | $-713.88 | -7.3% | $286.12 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1426 | 50.3 | 51.6 | $-955.47 | -6.7% | $44.53 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1194 | 48.9 | 51.4 | $-1097.78 | -9.2% | $-97.78 | -3.3 | done | losing for real |
| coinflip | 2033 | 50.0 | 50.7 | $-1100.58 | -5.4% | $-100.58 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 2033 | 49.5 | 51.6 | $-1568.28 | -7.7% | $-568.28 | -3.6 | done | losing for real |
| always_up | 2033 | 46.2 | 50.1 | $-2399.72 | -11.8% | $-1399.72 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3187 | 47.3 | 49.2 | $-2572.63 |
| ETH | 3511 | 48.0 | 48.7 | $-2316.55 |
| SOL | 3663 | 47.6 | 49.0 | $-2805.77 |
| XRP | 3701 | 48.3 | 48.8 | $-2147.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
