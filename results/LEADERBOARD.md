# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 80 windows, 2029 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 315 | 56.8 | 51.0 | $+250.98 | +8.0% | $1250.98 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 190 | 57.9 | 52.0 | $+170.36 | +9.0% | $1170.36 | +1.3 | Wed 12:15 PM | too few trades (190/200) |
| reversal_60m_0.30pct | 149 | 59.7 | 52.7 | $+159.60 | +10.7% | $1159.60 | +1.4 | Wed 6:00 PM | too few trades (149/200) |
| value_ev10 | 107 | 40.2 | 39.9 | $-50.48 | -4.7% | $949.52 | -0.4 | Thu 4:15 AM | too few trades (107/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 11:15 AM | too few trades (43/200) |
| trend_filter | 109 | 46.8 | 48.9 | $-84.87 | -7.8% | $915.13 | -0.8 | Thu 3:30 AM | too few trades (109/200) |
| value_ev5 | 147 | 39.5 | 41.4 | $-135.92 | -9.2% | $864.08 | -1.0 | Wed 6:15 PM | too few trades (147/200) |
| coinflip | 315 | 49.8 | 51.5 | $-213.50 | -6.8% | $786.50 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 149 | 40.3 | 48.7 | $-297.02 | -19.9% | $702.98 | -2.4 | Wed 6:00 PM | too few trades (149/200) |
| momentum_15m_0.10pct | 190 | 42.1 | 49.5 | $-340.04 | -17.9% | $659.96 | -2.5 | Wed 12:15 PM | too few trades (190/200) |
| always_up | 315 | 45.4 | 50.2 | $-404.86 | -12.9% | $595.14 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 437 | 47.1 | 49.8 | $-206.58 |
| ETH | 483 | 46.6 | 48.7 | $-321.15 |
| SOL | 545 | 49.4 | 48.3 | $-253.50 |
| XRP | 564 | 50.4 | 48.4 | $-218.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
