# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 281 windows, 7417 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 732 | 54.5 | 52.1 | $+54.01 | +0.7% | $1054.01 | +0.2 | done | can't tell from luck |
| value_ev20 | 136 | 36.0 | 36.9 | $-89.35 | -6.6% | $910.65 | -0.6 | Sun 5:15 AM | too few trades (136/200) |
| reversal_60m_0.30pct | 595 | 52.8 | 52.2 | $-156.12 | -2.6% | $843.88 | -0.7 | done | can't tell from luck |
| value_ev10 | 359 | 38.4 | 40.8 | $-333.02 | -9.3% | $666.98 | -1.5 | done | can't tell from luck |
| value_ev5 | 526 | 40.1 | 42.4 | $-486.88 | -9.3% | $513.12 | -1.9 | done | can't tell from luck |
| trend_filter | 394 | 46.2 | 50.3 | $-496.54 | -12.6% | $503.46 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 595 | 47.2 | 49.7 | $-570.58 | -9.6% | $429.42 | -2.4 | done | losing for real |
| coinflip | 1116 | 50.1 | 50.9 | $-634.39 | -5.7% | $365.61 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1116 | 49.6 | 51.5 | $-867.99 | -7.8% | $132.01 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 732 | 45.5 | 49.8 | $-917.41 | -12.5% | $82.59 | -3.4 | done | losing for real |
| always_up | 1116 | 47.4 | 50.2 | $-1080.84 | -9.7% | $-80.84 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1658 | 46.8 | 49.5 | $-1576.56 |
| ETH | 1851 | 47.1 | 49.0 | $-1660.48 |
| SOL | 1923 | 48.3 | 49.4 | $-1456.62 |
| XRP | 1985 | 49.0 | 49.1 | $-885.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
