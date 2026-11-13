# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 229 windows, 6001 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 592 | 56.1 | 52.6 | $+189.71 | +3.2% | $1189.71 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 470 | 53.8 | 52.3 | $-32.74 | -0.7% | $967.26 | -0.2 | done | can't tell from luck |
| value_ev20 | 112 | 33.9 | 36.6 | $-124.82 | -11.1% | $875.18 | -0.9 | Sun 5:45 AM | too few trades (112/200) |
| value_ev10 | 296 | 37.5 | 40.7 | $-340.78 | -11.5% | $659.22 | -1.7 | done | can't tell from luck |
| trend_filter | 314 | 45.5 | 50.2 | $-411.68 | -13.1% | $588.32 | -2.4 | done | losing for real |
| value_ev5 | 431 | 39.4 | 42.5 | $-468.33 | -10.9% | $531.67 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 470 | 46.2 | 49.8 | $-530.56 | -11.3% | $469.44 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 908 | 50.3 | 51.5 | $-559.35 | -6.2% | $440.65 | -1.9 | done | can't tell from luck |
| coinflip | 908 | 49.7 | 51.0 | $-595.83 | -6.6% | $404.17 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 592 | 43.9 | 49.6 | $-889.39 | -15.0% | $110.61 | -3.7 | done | losing for real |
| always_up | 908 | 47.4 | 50.3 | $-906.73 | -10.0% | $93.27 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1347 | 46.6 | 49.7 | $-1309.70 |
| ETH | 1493 | 46.7 | 49.0 | $-1460.84 |
| SOL | 1551 | 48.1 | 49.3 | $-1218.16 |
| XRP | 1610 | 49.1 | 49.2 | $-681.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
