# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 62 windows, 1548 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 111 | 61.3 | 52.1 | $+171.36 | +15.4% | $1171.36 | +1.7 | Wed 6:30 PM | too few trades (111/200) |
| reversal_15m_0.10pct | 143 | 57.3 | 51.8 | $+120.86 | +8.5% | $1120.86 | +1.0 | Wed 12:15 PM | too few trades (143/200) |
| value_ev10 | 83 | 43.4 | 38.9 | $+41.79 | +5.0% | $1041.79 | +0.4 | Thu 3:30 AM | too few trades (83/200) |
| momentum_5m_0.00pct | 240 | 53.3 | 50.8 | $+40.27 | +1.7% | $1040.27 | +0.3 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 10:15 PM | too few trades (38/200) |
| value_ev5 | 115 | 40.9 | 40.6 | $-42.45 | -3.7% | $957.55 | -0.3 | Wed 5:30 PM | too few trades (115/200) |
| trend_filter | 84 | 42.9 | 49.0 | $-129.75 | -15.4% | $870.25 | -1.4 | Thu 3:00 AM | too few trades (84/200) |
| coinflip | 240 | 50.4 | 51.7 | $-139.25 | -5.8% | $860.75 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 143 | 42.7 | 49.5 | $-224.81 | -15.7% | $775.19 | -1.9 | Wed 12:15 PM | too few trades (143/200) |
| momentum_60m_0.30pct | 111 | 38.7 | 49.1 | $-245.94 | -22.2% | $754.06 | -2.3 | Wed 6:30 PM | too few trades (111/200) |
| always_up | 240 | 42.1 | 49.8 | $-449.69 | -18.7% | $550.31 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 321 | 46.7 | 49.3 | $-109.51 |
| ETH | 372 | 44.1 | 48.2 | $-378.62 |
| SOL | 422 | 48.3 | 48.1 | $-245.24 |
| XRP | 433 | 50.6 | 48.2 | $-128.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
