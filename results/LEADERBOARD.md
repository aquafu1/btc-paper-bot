# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 65 windows, 1611 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 114 | 60.5 | 52.1 | $+159.73 | +14.0% | $1159.73 | +1.5 | Wed 7:00 PM | too few trades (114/200) |
| momentum_5m_0.00pct | 252 | 54.0 | 50.7 | $+74.84 | +3.0% | $1074.84 | +0.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 148 | 55.4 | 51.7 | $+70.86 | +4.8% | $1070.86 | +0.6 | Wed 12:45 PM | too few trades (148/200) |
| value_ev10 | 86 | 43.0 | 39.0 | $+35.17 | +4.1% | $1035.17 | +0.3 | Thu 4:00 AM | too few trades (86/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Sat 2:15 AM | too few trades (38/200) |
| value_ev5 | 119 | 40.3 | 40.7 | $-59.07 | -5.0% | $940.93 | -0.5 | Wed 5:45 PM | too few trades (119/200) |
| coinflip | 252 | 50.8 | 51.6 | $-123.40 | -4.9% | $876.60 | -0.8 | done | can't tell from luck |
| trend_filter | 88 | 43.2 | 49.0 | $-132.25 | -15.0% | $867.75 | -1.4 | Thu 3:15 AM | too few trades (88/200) |
| momentum_15m_0.10pct | 148 | 44.6 | 49.6 | $-182.02 | -12.3% | $817.98 | -1.5 | Wed 12:45 PM | too few trades (148/200) |
| momentum_60m_0.30pct | 114 | 39.5 | 49.2 | $-238.44 | -20.9% | $761.56 | -2.2 | Wed 7:00 PM | too few trades (114/200) |
| always_up | 252 | 42.9 | 50.1 | $-448.70 | -17.8% | $551.30 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 330 | 47.0 | 49.5 | $-111.11 |
| ETH | 388 | 45.4 | 48.3 | $-286.90 |
| SOL | 437 | 48.5 | 48.1 | $-246.59 |
| XRP | 456 | 50.0 | 48.3 | $-202.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
