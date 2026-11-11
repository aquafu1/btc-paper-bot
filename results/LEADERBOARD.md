# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 66 windows, 1628 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 114 | 60.5 | 52.1 | $+159.73 | +14.0% | $1159.73 | +1.5 | Wed 7:30 PM | too few trades (114/200) |
| reversal_15m_0.10pct | 150 | 56.0 | 51.7 | $+92.42 | +6.2% | $1092.42 | +0.8 | Wed 12:45 PM | too few trades (150/200) |
| momentum_5m_0.00pct | 256 | 53.5 | 50.9 | $+51.86 | +2.0% | $1051.86 | +0.3 | done | can't tell from luck |
| value_ev10 | 86 | 43.0 | 39.0 | $+35.17 | +4.1% | $1035.17 | +0.3 | Thu 4:30 AM | too few trades (86/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Sat 3:30 AM | too few trades (38/200) |
| value_ev5 | 120 | 40.8 | 40.8 | $-52.06 | -4.3% | $947.94 | -0.4 | Wed 6:00 PM | too few trades (120/200) |
| trend_filter | 88 | 43.2 | 49.0 | $-132.25 | -15.0% | $867.75 | -1.4 | Thu 3:45 AM | too few trades (88/200) |
| coinflip | 256 | 50.4 | 51.5 | $-137.49 | -5.4% | $862.51 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 150 | 44.0 | 49.6 | $-202.02 | -13.5% | $797.98 | -1.6 | Wed 12:45 PM | too few trades (150/200) |
| momentum_60m_0.30pct | 114 | 39.5 | 49.2 | $-238.44 | -20.9% | $761.56 | -2.2 | Wed 7:30 PM | too few trades (114/200) |
| always_up | 256 | 43.4 | 50.0 | $-415.92 | -16.2% | $584.08 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 335 | 46.9 | 49.5 | $-112.02 |
| ETH | 391 | 45.3 | 48.3 | $-294.57 |
| SOL | 440 | 48.6 | 48.1 | $-224.77 |
| XRP | 462 | 50.0 | 48.3 | $-211.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
