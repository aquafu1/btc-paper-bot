# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 227 windows, 5947 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 588 | 56.0 | 52.6 | $+174.69 | +3.0% | $1174.69 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 463 | 54.4 | 52.3 | $+18.32 | +0.4% | $1018.32 | +0.1 | done | can't tell from luck |
| value_ev20 | 112 | 33.9 | 36.6 | $-124.82 | -11.1% | $875.18 | -0.9 | Sun 4:45 AM | too few trades (112/200) |
| value_ev10 | 295 | 37.6 | 40.7 | $-330.78 | -11.2% | $669.22 | -1.6 | done | can't tell from luck |
| trend_filter | 310 | 45.2 | 50.2 | $-428.71 | -13.8% | $571.29 | -2.5 | done | losing for real |
| value_ev5 | 428 | 39.5 | 42.5 | $-458.82 | -10.7% | $541.18 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 900 | 50.4 | 51.5 | $-536.39 | -6.0% | $463.61 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 463 | 45.6 | 49.8 | $-576.08 | -12.4% | $423.92 | -2.7 | done | losing for real |
| coinflip | 900 | 49.7 | 51.0 | $-591.92 | -6.6% | $408.08 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 588 | 44.0 | 49.6 | $-867.00 | -14.7% | $133.00 | -3.6 | done | losing for real |
| always_up | 900 | 47.2 | 50.3 | $-924.64 | -10.3% | $75.36 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1334 | 46.5 | 49.7 | $-1335.74 |
| ETH | 1481 | 46.7 | 48.9 | $-1453.50 |
| SOL | 1538 | 48.0 | 49.3 | $-1230.02 |
| XRP | 1594 | 49.2 | 49.1 | $-626.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
