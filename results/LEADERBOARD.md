# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 81 windows, 2036 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 316 | 56.6 | 51.0 | $+240.98 | +7.6% | $1240.98 | +1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 191 | 58.1 | 51.9 | $+183.75 | +9.6% | $1183.75 | +1.4 | Wed 12:00 PM | too few trades (191/200) |
| reversal_60m_0.30pct | 149 | 59.7 | 52.7 | $+159.60 | +10.7% | $1159.60 | +1.4 | Wed 6:00 PM | too few trades (149/200) |
| value_ev10 | 108 | 40.7 | 39.9 | $-37.10 | -3.4% | $962.90 | -0.3 | Thu 4:00 AM | too few trades (108/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 11:15 AM | too few trades (43/200) |
| trend_filter | 109 | 46.8 | 48.9 | $-84.87 | -7.8% | $915.13 | -0.8 | Thu 3:30 AM | too few trades (109/200) |
| value_ev5 | 148 | 39.9 | 41.4 | $-122.54 | -8.3% | $877.47 | -0.9 | Wed 6:00 PM | too few trades (148/200) |
| coinflip | 316 | 49.7 | 51.6 | $-223.50 | -7.1% | $776.50 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 149 | 40.3 | 48.7 | $-297.02 | -19.9% | $702.98 | -2.4 | Wed 6:00 PM | too few trades (149/200) |
| momentum_15m_0.10pct | 191 | 41.9 | 49.6 | $-350.04 | -18.3% | $649.96 | -2.6 | Wed 12:00 PM | too few trades (191/200) |
| always_up | 316 | 45.6 | 50.2 | $-391.48 | -12.4% | $608.52 | -2.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 437 | 47.1 | 49.8 | $-206.58 |
| ETH | 490 | 46.7 | 48.7 | $-297.62 |
| SOL | 545 | 49.4 | 48.3 | $-253.50 |
| XRP | 564 | 50.4 | 48.4 | $-218.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
