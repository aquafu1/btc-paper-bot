# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 161 windows, 4119 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 302 | 59.3 | 53.1 | $+274.29 | +9.1% | $1274.29 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 398 | 57.0 | 52.5 | $+242.15 | +6.1% | $1242.15 | +1.3 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 4:15 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 637 | 51.6 | 51.2 | $-212.54 | -3.3% | $787.46 | -0.9 | done | can't tell from luck |
| value_ev10 | 210 | 38.6 | 40.9 | $-222.16 | -10.6% | $777.84 | -1.3 | done | can't tell from luck |
| coinflip | 637 | 50.7 | 50.8 | $-300.05 | -4.7% | $699.95 | -1.2 | done | can't tell from luck |
| value_ev5 | 308 | 39.3 | 42.6 | $-374.32 | -12.2% | $625.68 | -1.9 | done | can't tell from luck |
| trend_filter | 212 | 41.0 | 49.0 | $-403.00 | -19.0% | $597.00 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 302 | 40.7 | 49.1 | $-595.52 | -19.7% | $404.48 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 398 | 43.0 | 49.8 | $-661.88 | -16.6% | $338.12 | -3.4 | done | losing for real |
| always_up | 637 | 45.8 | 50.3 | $-836.83 | -13.1% | $163.17 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 900 | 46.1 | 49.5 | $-815.80 |
| ETH | 1023 | 45.7 | 48.9 | $-1127.18 |
| SOL | 1079 | 47.9 | 49.0 | $-870.05 |
| XRP | 1117 | 50.2 | 49.2 | $-358.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
