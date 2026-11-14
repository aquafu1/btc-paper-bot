# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 280 windows, 7398 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 730 | 54.7 | 52.1 | $+74.01 | +1.0% | $1074.01 | +0.3 | done | can't tell from luck |
| value_ev20 | 136 | 36.0 | 36.9 | $-89.35 | -6.6% | $910.65 | -0.6 | Sun 5:15 AM | too few trades (136/200) |
| reversal_60m_0.30pct | 593 | 52.6 | 52.2 | $-174.28 | -2.9% | $825.72 | -0.7 | done | can't tell from luck |
| value_ev10 | 359 | 38.4 | 40.8 | $-333.02 | -9.3% | $666.98 | -1.5 | done | can't tell from luck |
| value_ev5 | 525 | 40.2 | 42.4 | $-476.88 | -9.1% | $523.12 | -1.8 | done | can't tell from luck |
| trend_filter | 393 | 46.3 | 50.3 | $-486.54 | -12.4% | $513.46 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 593 | 47.4 | 49.7 | $-550.58 | -9.3% | $449.42 | -2.3 | done | losing for real |
| coinflip | 1113 | 50.0 | 50.9 | $-646.20 | -5.8% | $353.80 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1113 | 49.6 | 51.5 | $-859.21 | -7.7% | $140.79 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 730 | 45.3 | 49.8 | $-936.20 | -12.8% | $63.80 | -3.5 | done | losing for real |
| always_up | 1113 | 47.3 | 50.2 | $-1110.22 | -10.0% | $-110.22 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1658 | 46.8 | 49.5 | $-1576.56 |
| ETH | 1845 | 47.1 | 49.0 | $-1662.23 |
| SOL | 1915 | 48.3 | 49.4 | $-1429.33 |
| XRP | 1980 | 48.9 | 49.1 | $-920.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
