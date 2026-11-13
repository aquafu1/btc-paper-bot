# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 202 windows, 5226 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 514 | 57.4 | 52.7 | $+284.26 | +5.5% | $1284.26 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 392 | 56.4 | 52.8 | $+121.99 | +3.1% | $1121.99 | +0.7 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 6:30 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 800 | 51.2 | 51.4 | $-362.92 | -4.5% | $637.08 | -1.3 | done | can't tell from luck |
| trend_filter | 266 | 44.0 | 49.7 | $-401.92 | -15.1% | $598.08 | -2.5 | done | losing for real |
| coinflip | 800 | 50.2 | 51.0 | $-492.63 | -6.2% | $507.37 | -1.8 | done | can't tell from luck |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| value_ev5 | 385 | 37.9 | 42.7 | $-605.55 | -15.7% | $394.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 392 | 43.6 | 49.4 | $-623.13 | -15.9% | $376.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 514 | 42.6 | 49.6 | $-910.39 | -17.7% | $89.61 | -4.1 | done | losing for real |
| always_up | 800 | 45.1 | 50.3 | $-1186.42 | -14.8% | $-186.42 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1155 | 45.8 | 49.6 | $-1303.04 |
| ETH | 1301 | 46.0 | 48.9 | $-1504.40 |
| SOL | 1352 | 47.5 | 49.2 | $-1273.12 |
| XRP | 1418 | 49.0 | 49.3 | $-828.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
