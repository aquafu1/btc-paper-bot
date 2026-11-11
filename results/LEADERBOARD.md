# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 79 windows, 2003 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 311 | 57.2 | 50.9 | $+273.67 | +8.8% | $1273.67 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 147 | 59.9 | 52.7 | $+162.30 | +11.0% | $1162.30 | +1.4 | Wed 6:00 PM | too few trades (147/200) |
| reversal_15m_0.10pct | 187 | 57.2 | 52.1 | $+137.26 | +7.3% | $1137.26 | +1.0 | Wed 12:15 PM | too few trades (187/200) |
| value_ev10 | 106 | 40.6 | 39.8 | $-40.48 | -3.8% | $959.52 | -0.3 | Thu 4:15 AM | too few trades (106/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 10:00 AM | too few trades (43/200) |
| trend_filter | 108 | 47.2 | 48.8 | $-74.87 | -6.9% | $925.13 | -0.7 | Thu 3:30 AM | too few trades (108/200) |
| value_ev5 | 145 | 39.3 | 41.3 | $-138.07 | -9.5% | $861.93 | -1.0 | Wed 6:15 PM | too few trades (145/200) |
| coinflip | 311 | 50.2 | 51.5 | $-193.08 | -6.2% | $806.92 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 147 | 40.1 | 48.7 | $-298.39 | -20.3% | $701.61 | -2.4 | Wed 6:00 PM | too few trades (147/200) |
| momentum_15m_0.10pct | 187 | 42.8 | 49.4 | $-310.04 | -16.6% | $689.96 | -2.3 | Wed 12:15 PM | too few trades (187/200) |
| always_up | 311 | 45.0 | 50.3 | $-427.96 | -13.8% | $572.04 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 430 | 47.2 | 49.8 | $-200.68 |
| ETH | 476 | 46.8 | 48.7 | $-285.76 |
| SOL | 539 | 49.4 | 48.3 | $-259.96 |
| XRP | 558 | 50.4 | 48.4 | $-217.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
