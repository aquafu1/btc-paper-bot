# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 61 windows, 1529 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 110 | 61.8 | 52.1 | $+181.36 | +16.5% | $1181.36 | +1.8 | Wed 6:15 PM | too few trades (110/200) |
| reversal_15m_0.10pct | 143 | 57.3 | 51.8 | $+120.86 | +8.5% | $1120.86 | +1.0 | Wed 12:00 PM | too few trades (143/200) |
| value_ev10 | 81 | 44.4 | 38.7 | $+61.79 | +7.6% | $1061.79 | +0.6 | Thu 3:45 AM | too few trades (81/200) |
| momentum_5m_0.00pct | 236 | 52.5 | 50.7 | $+7.84 | +0.3% | $1007.84 | +0.1 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 9:00 PM | too few trades (38/200) |
| value_ev5 | 113 | 41.6 | 40.5 | $-22.45 | -2.0% | $977.55 | -0.2 | Wed 5:30 PM | too few trades (113/200) |
| coinflip | 236 | 50.4 | 51.7 | $-135.95 | -5.8% | $864.05 | -0.9 | done | can't tell from luck |
| trend_filter | 83 | 42.2 | 49.0 | $-139.43 | -16.8% | $860.57 | -1.5 | Thu 3:00 AM | too few trades (83/200) |
| momentum_15m_0.10pct | 143 | 42.7 | 49.5 | $-224.81 | -15.7% | $775.19 | -1.9 | Wed 12:00 PM | too few trades (143/200) |
| momentum_60m_0.30pct | 110 | 38.2 | 49.1 | $-255.62 | -23.2% | $744.38 | -2.4 | Wed 6:15 PM | too few trades (110/200) |
| always_up | 236 | 42.8 | 49.8 | $-409.69 | -17.4% | $590.31 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 316 | 47.2 | 49.3 | $-76.82 |
| ETH | 367 | 44.1 | 48.2 | $-362.66 |
| SOL | 419 | 48.4 | 48.0 | $-233.66 |
| XRP | 427 | 50.4 | 48.1 | $-146.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
