# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 54 windows, 1370 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 95 | 64.2 | 51.8 | $+200.72 | +21.1% | $1200.72 | +2.1 | Wed 6:45 PM | too few trades (95/200) |
| reversal_15m_0.10pct | 129 | 57.4 | 52.0 | $+96.85 | +7.5% | $1096.85 | +0.9 | Wed 11:30 AM | too few trades (129/200) |
| value_ev10 | 79 | 44.3 | 38.6 | $+56.61 | +7.2% | $1056.61 | +0.5 | Thu 12:15 AM | too few trades (79/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 11:45 AM | too few trades (38/200) |
| momentum_5m_0.00pct | 208 | 52.4 | 50.7 | $-13.44 | -0.6% | $986.56 | -0.1 | done | can't tell from luck |
| value_ev5 | 107 | 40.2 | 40.2 | $-51.23 | -4.8% | $948.77 | -0.4 | Wed 3:45 PM | too few trades (107/200) |
| trend_filter | 74 | 41.9 | 48.6 | $-129.43 | -17.5% | $870.57 | -1.5 | Thu 2:30 AM | too few trades (74/200) |
| coinflip | 208 | 50.5 | 51.6 | $-132.60 | -6.4% | $867.40 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 129 | 42.6 | 49.1 | $-203.67 | -15.8% | $796.33 | -1.8 | Wed 11:30 AM | too few trades (129/200) |
| momentum_60m_0.30pct | 95 | 35.8 | 48.9 | $-266.96 | -28.1% | $733.04 | -2.7 | Wed 6:45 PM | too few trades (95/200) |
| always_up | 208 | 40.9 | 49.7 | $-453.31 | -21.8% | $546.69 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 283 | 46.3 | 48.9 | $-92.77 |
| ETH | 331 | 44.1 | 47.9 | $-323.31 |
| SOL | 378 | 47.9 | 47.7 | $-253.22 |
| XRP | 378 | 49.7 | 47.9 | $-231.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
