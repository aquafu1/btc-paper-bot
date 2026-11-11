# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 82 windows, 2063 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 320 | 57.2 | 51.0 | $+284.87 | +8.9% | $1284.87 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 194 | 57.2 | 52.0 | $+153.75 | +7.9% | $1153.75 | +1.1 | Wed 12:00 PM | too few trades (194/200) |
| reversal_60m_0.30pct | 150 | 59.3 | 52.8 | $+149.60 | +10.0% | $1149.60 | +1.3 | Wed 6:00 PM | too few trades (150/200) |
| value_ev10 | 111 | 42.3 | 40.0 | $-0.73 | -0.1% | $999.27 | -0.0 | Thu 3:30 AM | too few trades (111/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 12:30 PM | too few trades (43/200) |
| trend_filter | 110 | 47.3 | 48.8 | $-72.03 | -6.5% | $927.97 | -0.7 | Thu 3:45 AM | too few trades (110/200) |
| value_ev5 | 151 | 41.1 | 41.4 | $-86.16 | -5.7% | $913.84 | -0.6 | Wed 5:45 PM | too few trades (151/200) |
| coinflip | 320 | 50.0 | 51.5 | $-197.13 | -6.2% | $802.87 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 150 | 40.7 | 48.7 | $-284.18 | -18.9% | $715.82 | -2.3 | Wed 6:00 PM | too few trades (150/200) |
| momentum_15m_0.10pct | 194 | 42.8 | 49.6 | $-318.99 | -16.4% | $681.01 | -2.3 | Wed 12:00 PM | too few trades (194/200) |
| always_up | 320 | 46.2 | 50.2 | $-347.59 | -10.9% | $652.41 | -2.0 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 445 | 47.9 | 49.8 | $-126.68 |
| ETH | 497 | 47.3 | 48.6 | $-230.56 |
| SOL | 552 | 49.8 | 48.4 | $-199.39 |
| XRP | 569 | 50.4 | 48.5 | $-215.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
