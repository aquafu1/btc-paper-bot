# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 81 windows, 2055 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 319 | 57.1 | 51.0 | $+272.03 | +8.5% | $1272.03 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 149 | 59.7 | 52.7 | $+159.60 | +10.7% | $1159.60 | +1.4 | Wed 6:15 PM | too few trades (149/200) |
| reversal_15m_0.10pct | 194 | 57.2 | 52.0 | $+153.75 | +7.9% | $1153.75 | +1.1 | Wed 12:00 PM | too few trades (194/200) |
| value_ev10 | 110 | 41.8 | 40.0 | $-13.57 | -1.2% | $986.43 | -0.1 | Thu 3:45 AM | too few trades (110/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 12:30 PM | too few trades (43/200) |
| trend_filter | 109 | 46.8 | 48.9 | $-84.87 | -7.8% | $915.13 | -0.8 | Thu 4:00 AM | too few trades (109/200) |
| value_ev5 | 150 | 40.7 | 41.4 | $-99.01 | -6.6% | $900.99 | -0.7 | Wed 6:00 PM | too few trades (150/200) |
| coinflip | 319 | 49.8 | 51.5 | $-209.97 | -6.6% | $790.03 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 149 | 40.3 | 48.7 | $-297.02 | -19.9% | $702.98 | -2.4 | Wed 6:15 PM | too few trades (149/200) |
| momentum_15m_0.10pct | 194 | 42.8 | 49.6 | $-318.99 | -16.4% | $681.01 | -2.3 | Wed 12:00 PM | too few trades (194/200) |
| always_up | 319 | 46.1 | 50.2 | $-360.43 | -11.3% | $639.57 | -2.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 437 | 47.1 | 49.8 | $-206.58 |
| ETH | 497 | 47.3 | 48.6 | $-230.56 |
| SOL | 552 | 49.8 | 48.4 | $-199.39 |
| XRP | 569 | 50.4 | 48.5 | $-215.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
