# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 159 windows, 4052 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 295 | 59.3 | 53.4 | $+253.44 | +8.6% | $1253.44 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 390 | 56.2 | 52.5 | $+160.81 | +4.1% | $1160.81 | +0.9 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 4:30 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 629 | 52.1 | 51.2 | $-151.84 | -2.4% | $848.16 | -0.6 | done | can't tell from luck |
| value_ev10 | 206 | 37.9 | 40.9 | $-253.71 | -12.3% | $746.29 | -1.5 | done | can't tell from luck |
| coinflip | 629 | 50.9 | 50.9 | $-286.06 | -4.5% | $713.94 | -1.2 | done | can't tell from luck |
| trend_filter | 209 | 41.6 | 48.8 | $-373.00 | -17.8% | $627.00 | -2.6 | done | losing for real |
| value_ev5 | 303 | 38.9 | 42.6 | $-395.87 | -13.1% | $604.13 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 295 | 40.7 | 48.9 | $-578.49 | -19.6% | $421.51 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 390 | 43.8 | 49.7 | $-581.88 | -14.9% | $418.12 | -3.0 | done | losing for real |
| always_up | 629 | 45.8 | 50.3 | $-847.68 | -13.5% | $152.32 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 884 | 46.3 | 49.6 | $-763.93 |
| ETH | 1006 | 45.6 | 48.9 | $-1140.11 |
| SOL | 1063 | 48.1 | 49.0 | $-841.77 |
| XRP | 1099 | 50.2 | 49.2 | $-407.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
