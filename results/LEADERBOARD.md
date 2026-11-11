# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 69 windows, 1704 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 119 | 59.7 | 52.2 | $+140.12 | +11.8% | $1140.12 | +1.3 | Wed 7:30 PM | too few trades (119/200) |
| momentum_5m_0.00pct | 268 | 55.2 | 51.1 | $+123.27 | +4.6% | $1123.27 | +0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 157 | 56.1 | 51.7 | $+92.56 | +5.9% | $1092.56 | +0.8 | Wed 12:45 PM | too few trades (157/200) |
| value_ev10 | 90 | 42.2 | 39.1 | $+15.25 | +1.7% | $1015.25 | +0.1 | Thu 4:30 AM | too few trades (90/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 1:00 AM | too few trades (41/200) |
| value_ev5 | 126 | 39.7 | 40.9 | $-91.98 | -7.3% | $908.02 | -0.7 | Wed 6:00 PM | too few trades (126/200) |
| trend_filter | 91 | 45.1 | 49.1 | $-105.18 | -11.6% | $894.82 | -1.1 | Thu 4:15 AM | too few trades (91/200) |
| coinflip | 268 | 50.4 | 51.6 | $-153.55 | -5.7% | $846.45 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 157 | 43.9 | 49.7 | $-218.70 | -13.9% | $781.30 | -1.7 | Wed 12:45 PM | too few trades (157/200) |
| momentum_60m_0.30pct | 119 | 40.3 | 49.1 | $-231.37 | -19.4% | $768.63 | -2.1 | Wed 7:30 PM | too few trades (119/200) |
| always_up | 268 | 44.0 | 50.0 | $-409.85 | -15.3% | $590.15 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 352 | 47.2 | 49.6 | $-115.20 |
| ETH | 405 | 46.2 | 48.5 | $-255.56 |
| SOL | 465 | 48.6 | 48.1 | $-274.55 |
| XRP | 482 | 50.0 | 48.3 | $-227.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
