# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 52 windows, 1346 settled trades, 24 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 93 | 63.4 | 51.7 | $+187.24 | +20.1% | $1187.24 | +2.0 | Wed 6:45 PM | too few trades (93/200) |
| reversal_15m_0.10pct | 125 | 56.0 | 51.8 | $+66.46 | +5.3% | $1066.46 | +0.6 | Wed 11:45 AM | too few trades (125/200) |
| value_ev10 | 79 | 44.3 | 38.6 | $+56.61 | +7.2% | $1056.61 | +0.5 | Wed 11:45 PM | too few trades (79/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 10:30 AM | too few trades (38/200) |
| momentum_5m_0.00pct | 204 | 52.5 | 50.6 | $-6.92 | -0.3% | $993.08 | -0.0 | done | can't tell from luck |
| value_ev5 | 107 | 40.2 | 40.2 | $-51.23 | -4.8% | $948.77 | -0.4 | Wed 3:15 PM | too few trades (107/200) |
| coinflip | 204 | 50.5 | 51.6 | $-126.08 | -6.2% | $873.92 | -0.9 | done | can't tell from luck |
| trend_filter | 74 | 41.9 | 48.6 | $-129.43 | -17.5% | $870.57 | -1.5 | Thu 1:45 AM | too few trades (74/200) |
| momentum_15m_0.10pct | 125 | 44.0 | 49.1 | $-163.67 | -13.1% | $836.33 | -1.4 | Wed 11:45 AM | too few trades (125/200) |
| momentum_60m_0.30pct | 93 | 36.6 | 49.0 | $-246.96 | -26.6% | $753.04 | -2.5 | Wed 6:45 PM | too few trades (93/200) |
| always_up | 204 | 41.7 | 49.8 | $-413.31 | -20.3% | $586.69 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 278 | 46.8 | 48.9 | $-62.07 |
| ETH | 326 | 44.5 | 47.9 | $-290.92 |
| SOL | 371 | 47.7 | 47.6 | $-249.07 |
| XRP | 371 | 49.6 | 47.8 | $-229.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
