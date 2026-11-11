# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 95 windows, 2420 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 372 | 55.6 | 51.0 | $+216.25 | +5.8% | $1216.25 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 180 | 59.4 | 52.7 | $+182.93 | +10.2% | $1182.93 | +1.4 | Wed 5:15 PM | too few trades (180/200) |
| reversal_15m_0.10pct | 234 | 56.8 | 52.3 | $+152.20 | +6.5% | $1152.20 | +1.0 | done | can't tell from luck |
| value_ev10 | 126 | 39.7 | 40.5 | $-83.04 | -6.6% | $916.96 | -0.6 | Thu 4:15 AM | too few trades (126/200) |
| value_ev20 | 47 | 29.8 | 36.4 | $-93.85 | -20.0% | $906.15 | -1.1 | Sat 6:15 PM | too few trades (47/200) |
| trend_filter | 131 | 45.8 | 49.0 | $-124.96 | -9.5% | $875.04 | -1.1 | Thu 2:45 AM | too few trades (131/200) |
| coinflip | 372 | 50.5 | 51.7 | $-207.51 | -5.6% | $792.49 | -1.1 | done | can't tell from luck |
| value_ev5 | 172 | 37.8 | 41.9 | $-228.48 | -13.3% | $771.52 | -1.5 | Wed 6:30 PM | too few trades (172/200) |
| momentum_60m_0.30pct | 180 | 40.6 | 49.1 | $-358.49 | -19.9% | $641.51 | -2.7 | Wed 5:15 PM | too few trades (180/200) |
| momentum_15m_0.10pct | 234 | 43.2 | 49.6 | $-368.50 | -15.7% | $631.50 | -2.4 | done | losing for real |
| always_up | 372 | 46.0 | 50.3 | $-437.08 | -11.7% | $562.92 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 516 | 47.5 | 49.9 | $-240.86 |
| ETH | 591 | 46.5 | 48.8 | $-400.25 |
| SOL | 650 | 49.4 | 48.7 | $-305.04 |
| XRP | 663 | 49.5 | 48.9 | $-404.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
