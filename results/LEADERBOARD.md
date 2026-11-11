# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 52 windows, 1322 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 91 | 62.6 | 51.5 | $+172.75 | +19.0% | $1172.75 | +1.8 | Wed 6:45 PM | too few trades (91/200) |
| value_ev10 | 79 | 44.3 | 38.6 | $+56.61 | +7.2% | $1056.61 | +0.5 | Wed 11:00 PM | too few trades (79/200) |
| reversal_15m_0.10pct | 122 | 54.9 | 51.8 | $+41.06 | +3.4% | $1041.06 | +0.4 | Wed 11:45 AM | too few trades (122/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 9:15 AM | too few trades (38/200) |
| value_ev5 | 105 | 41.0 | 40.1 | $-31.23 | -3.0% | $968.77 | -0.3 | Wed 3:15 PM | too few trades (105/200) |
| momentum_5m_0.00pct | 200 | 51.5 | 50.5 | $-40.05 | -2.0% | $959.95 | -0.3 | done | can't tell from luck |
| coinflip | 200 | 50.5 | 51.5 | $-121.19 | -6.1% | $878.81 | -0.9 | done | can't tell from luck |
| trend_filter | 74 | 41.9 | 48.6 | $-129.43 | -17.5% | $870.57 | -1.5 | Thu 1:15 AM | too few trades (74/200) |
| momentum_15m_0.10pct | 122 | 45.1 | 49.1 | $-133.67 | -11.0% | $866.33 | -1.2 | Wed 11:45 AM | too few trades (122/200) |
| momentum_60m_0.30pct | 91 | 37.4 | 49.0 | $-226.96 | -24.9% | $773.04 | -2.3 | Wed 6:45 PM | too few trades (91/200) |
| always_up | 200 | 40.5 | 49.7 | $-446.44 | -22.3% | $553.56 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 273 | 46.5 | 48.8 | $-74.82 |
| ETH | 318 | 44.3 | 47.8 | $-279.31 |
| SOL | 368 | 47.3 | 47.6 | $-272.25 |
| XRP | 363 | 49.3 | 47.7 | $-236.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
