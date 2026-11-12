# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 161 windows, 4110 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 301 | 59.5 | 53.2 | $+284.29 | +9.4% | $1284.29 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 397 | 56.9 | 52.5 | $+236.68 | +6.0% | $1236.68 | +1.2 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 3:45 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 636 | 51.7 | 51.2 | $-202.54 | -3.2% | $797.46 | -0.8 | done | can't tell from luck |
| value_ev10 | 209 | 38.8 | 40.9 | $-212.16 | -10.2% | $787.84 | -1.3 | done | can't tell from luck |
| coinflip | 636 | 50.8 | 50.9 | $-290.05 | -4.6% | $709.95 | -1.2 | done | can't tell from luck |
| value_ev5 | 307 | 39.4 | 42.6 | $-364.32 | -11.9% | $635.68 | -1.9 | done | can't tell from luck |
| trend_filter | 212 | 41.0 | 49.0 | $-403.00 | -19.0% | $597.00 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 301 | 40.5 | 49.1 | $-600.98 | -20.0% | $399.02 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 397 | 43.1 | 49.8 | $-651.88 | -16.4% | $348.12 | -3.3 | done | losing for real |
| always_up | 636 | 45.9 | 50.3 | $-826.83 | -13.0% | $173.17 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 891 | 46.4 | 49.6 | $-756.73 |
| ETH | 1023 | 45.7 | 48.9 | $-1127.18 |
| SOL | 1079 | 47.9 | 49.0 | $-870.05 |
| XRP | 1117 | 50.2 | 49.2 | $-358.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
