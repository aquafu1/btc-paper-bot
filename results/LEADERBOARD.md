# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 429 windows, 11803 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 214 | 34.6 | 36.2 | $-174.42 | -8.2% | $825.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1006 | 50.7 | 50.0 | $-286.93 | -2.9% | $713.07 | -0.9 | done | can't tell from luck |
| value_ev10 | 553 | 39.2 | 40.3 | $-345.64 | -6.3% | $654.36 | -1.2 | done | can't tell from luck |
| trend_filter | 676 | 49.7 | 50.7 | $-412.51 | -6.1% | $587.49 | -1.6 | done | can't tell from luck |
| value_ev5 | 830 | 41.4 | 42.0 | $-431.13 | -5.2% | $568.87 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1194 | 49.2 | 50.0 | $-625.03 | -5.2% | $374.97 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1194 | 50.8 | 51.7 | $-699.83 | -5.9% | $300.17 | -2.1 | done | losing for real |
| coinflip | 1710 | 50.5 | 50.9 | $-780.17 | -4.6% | $219.83 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1006 | 49.3 | 51.8 | $-908.23 | -9.0% | $91.77 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1710 | 49.6 | 51.6 | $-1272.21 | -7.4% | $-272.21 | -3.2 | done | losing for real |
| always_up | 1710 | 46.3 | 50.6 | $-2050.88 | -12.0% | $-1050.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2672 | 47.6 | 49.4 | $-2033.86 |
| ETH | 2957 | 48.1 | 48.9 | $-1861.41 |
| SOL | 3061 | 47.8 | 49.4 | $-2386.41 |
| XRP | 3113 | 48.7 | 49.3 | $-1705.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
