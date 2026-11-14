# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 316 windows, 8460 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 689 | 53.1 | 51.8 | $-116.92 | -1.7% | $883.08 | -0.5 | done | can't tell from luck |
| value_ev20 | 158 | 33.5 | 36.6 | $-210.14 | -13.3% | $789.86 | -1.3 | Sun 1:00 AM | too few trades (158/200) |
| reversal_15m_0.10pct | 839 | 52.8 | 51.9 | $-213.62 | -2.5% | $786.38 | -0.8 | done | can't tell from luck |
| value_ev10 | 405 | 37.8 | 40.5 | $-442.08 | -10.9% | $557.92 | -1.9 | done | can't tell from luck |
| value_ev5 | 605 | 39.5 | 42.2 | $-646.45 | -10.7% | $353.55 | -2.3 | done | losing for real |
| trend_filter | 468 | 44.9 | 50.3 | $-708.46 | -15.1% | $291.54 | -3.4 | done | losing for real |
| momentum_60m_0.30pct | 689 | 46.9 | 49.9 | $-734.76 | -10.7% | $265.24 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 839 | 47.2 | 49.8 | $-794.34 | -9.5% | $205.66 | -2.8 | done | losing for real |
| coinflip | 1256 | 49.8 | 50.9 | $-801.01 | -6.4% | $198.99 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1256 | 48.4 | 51.3 | $-1231.53 | -9.8% | $-231.53 | -3.6 | done | losing for real |
| always_up | 1256 | 47.5 | 50.4 | $-1266.06 | -10.1% | $-266.06 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1899 | 46.4 | 49.3 | $-1929.17 |
| ETH | 2122 | 46.7 | 48.8 | $-2096.98 |
| SOL | 2200 | 47.8 | 49.4 | $-1853.90 |
| XRP | 2239 | 48.6 | 49.1 | $-1285.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
