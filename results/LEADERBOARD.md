# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 510 windows, 14054 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1193 | 51.1 | 49.8 | $-181.83 | -1.5% | $818.17 | -0.5 | done | can't tell from luck |
| value_ev10 | 659 | 38.1 | 39.7 | $-500.51 | -7.6% | $499.49 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1425 | 49.8 | 49.6 | $-555.70 | -3.9% | $444.30 | -1.5 | done | can't tell from luck |
| trend_filter | 823 | 49.5 | 50.7 | $-559.51 | -6.8% | $440.49 | -2.0 | done | can't tell from luck |
| value_ev5 | 976 | 40.0 | 41.5 | $-713.88 | -7.3% | $286.12 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1425 | 50.2 | 51.6 | $-970.64 | -6.8% | $29.36 | -2.6 | done | losing for real |
| coinflip | 2032 | 50.0 | 50.7 | $-1090.58 | -5.4% | $-90.58 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1193 | 48.9 | 51.4 | $-1112.95 | -9.3% | $-112.95 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2032 | 49.6 | 51.6 | $-1558.28 | -7.7% | $-558.28 | -3.6 | done | losing for real |
| always_up | 2032 | 46.2 | 50.1 | $-2414.90 | -11.9% | $-1414.90 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3179 | 47.3 | 49.2 | $-2568.15 |
| ETH | 3511 | 48.0 | 48.7 | $-2316.55 |
| SOL | 3663 | 47.6 | 49.0 | $-2805.77 |
| XRP | 3701 | 48.3 | 48.8 | $-2147.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
