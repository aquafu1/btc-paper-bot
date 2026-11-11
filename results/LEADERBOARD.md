# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 69 windows, 1711 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 119 | 59.7 | 52.2 | $+140.12 | +11.8% | $1140.12 | +1.3 | Wed 8:00 PM | too few trades (119/200) |
| momentum_5m_0.00pct | 269 | 55.4 | 51.1 | $+135.10 | +5.0% | $1135.10 | +0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 158 | 56.3 | 51.7 | $+104.40 | +6.6% | $1104.40 | +0.8 | Wed 1:00 PM | too few trades (158/200) |
| value_ev10 | 91 | 42.9 | 39.2 | $+27.08 | +3.0% | $1027.08 | +0.2 | Thu 4:45 AM | too few trades (91/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 2:15 AM | too few trades (41/200) |
| value_ev5 | 127 | 40.2 | 41.0 | $-80.14 | -6.3% | $919.86 | -0.6 | Wed 6:15 PM | too few trades (127/200) |
| trend_filter | 91 | 45.1 | 49.1 | $-105.18 | -11.6% | $894.82 | -1.1 | Thu 4:45 AM | too few trades (91/200) |
| coinflip | 269 | 50.2 | 51.6 | $-163.55 | -6.1% | $836.45 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 158 | 43.7 | 49.7 | $-228.70 | -14.5% | $771.30 | -1.8 | Wed 1:00 PM | too few trades (158/200) |
| momentum_60m_0.30pct | 119 | 40.3 | 49.1 | $-231.37 | -19.4% | $768.63 | -2.1 | Wed 8:00 PM | too few trades (119/200) |
| always_up | 269 | 43.9 | 50.1 | $-419.85 | -15.6% | $580.15 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 352 | 47.2 | 49.6 | $-115.20 |
| ETH | 412 | 46.4 | 48.5 | $-238.21 |
| SOL | 465 | 48.6 | 48.1 | $-274.55 |
| XRP | 482 | 50.0 | 48.3 | $-227.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
