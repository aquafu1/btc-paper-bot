# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 142 windows, 3569 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 247 | 61.9 | 53.2 | $+342.92 | +13.9% | $1342.92 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 343 | 57.7 | 52.3 | $+267.75 | +7.8% | $1267.75 | +1.5 | done | can't tell from luck |
| momentum_5m_0.00pct | 560 | 52.1 | 51.2 | $-141.51 | -2.5% | $858.49 | -0.6 | done | can't tell from luck |
| value_ev20 | 69 | 30.4 | 36.9 | $-155.47 | -22.5% | $844.53 | -1.6 | Sun 4:00 AM | too few trades (69/200) |
| coinflip | 560 | 51.4 | 50.9 | $-209.75 | -3.7% | $790.25 | -0.9 | done | can't tell from luck |
| value_ev10 | 188 | 36.7 | 40.6 | $-265.28 | -14.1% | $734.72 | -1.7 | Thu 7:15 AM | too few trades (188/200) |
| trend_filter | 179 | 40.2 | 49.1 | $-378.37 | -21.1% | $621.63 | -2.8 | Thu 9:15 AM | too few trades (179/200) |
| value_ev5 | 273 | 37.7 | 42.2 | $-404.16 | -14.8% | $595.84 | -2.2 | done | losing for real |
| always_up | 560 | 47.3 | 50.1 | $-559.64 | -10.0% | $440.36 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 247 | 38.1 | 49.1 | $-615.20 | -24.9% | $384.80 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 343 | 42.3 | 49.9 | $-627.03 | -18.3% | $372.97 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 765 | 45.5 | 49.5 | $-844.81 |
| ETH | 881 | 45.1 | 48.8 | $-1032.04 |
| SOL | 941 | 48.6 | 48.8 | $-631.57 |
| XRP | 982 | 50.7 | 49.1 | $-237.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
