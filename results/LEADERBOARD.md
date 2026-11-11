# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 80 windows, 2010 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 312 | 57.4 | 50.9 | $+280.98 | +9.0% | $1280.98 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 148 | 60.1 | 52.7 | $+169.60 | +11.5% | $1169.60 | +1.5 | Wed 5:45 PM | too few trades (148/200) |
| reversal_15m_0.10pct | 187 | 57.2 | 52.1 | $+137.26 | +7.3% | $1137.26 | +1.0 | Wed 12:15 PM | too few trades (187/200) |
| value_ev10 | 107 | 40.2 | 39.9 | $-50.48 | -4.7% | $949.52 | -0.4 | Thu 3:45 AM | too few trades (107/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 10:00 AM | too few trades (43/200) |
| trend_filter | 108 | 47.2 | 48.8 | $-74.87 | -6.9% | $925.13 | -0.7 | Thu 3:30 AM | too few trades (108/200) |
| value_ev5 | 146 | 39.0 | 41.3 | $-148.07 | -10.1% | $851.93 | -1.1 | Wed 6:00 PM | too few trades (146/200) |
| coinflip | 312 | 50.0 | 51.5 | $-203.08 | -6.5% | $796.92 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 148 | 39.9 | 48.7 | $-308.39 | -20.8% | $691.61 | -2.5 | Wed 5:45 PM | too few trades (148/200) |
| momentum_15m_0.10pct | 187 | 42.8 | 49.4 | $-310.04 | -16.6% | $689.96 | -2.3 | Wed 12:15 PM | too few trades (187/200) |
| always_up | 312 | 44.9 | 50.3 | $-437.96 | -14.0% | $562.04 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 430 | 47.2 | 49.8 | $-200.68 |
| ETH | 483 | 46.6 | 48.7 | $-321.15 |
| SOL | 539 | 49.4 | 48.3 | $-259.96 |
| XRP | 558 | 50.4 | 48.4 | $-217.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
