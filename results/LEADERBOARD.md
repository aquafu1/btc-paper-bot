# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 93 windows, 2365 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 364 | 55.5 | 50.9 | $+204.72 | +5.6% | $1204.72 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 177 | 58.8 | 52.8 | $+152.03 | +8.6% | $1152.03 | +1.2 | Wed 5:00 PM | too few trades (177/200) |
| reversal_15m_0.10pct | 228 | 56.6 | 52.5 | $+129.78 | +5.7% | $1129.78 | +0.9 | done | can't tell from luck |
| value_ev10 | 122 | 41.0 | 40.3 | $-43.04 | -3.5% | $956.96 | -0.3 | Thu 4:45 AM | too few trades (122/200) |
| value_ev20 | 45 | 31.1 | 36.1 | $-73.85 | -16.4% | $926.15 | -0.9 | Sat 8:30 PM | too few trades (45/200) |
| trend_filter | 128 | 46.9 | 48.9 | $-94.96 | -7.4% | $905.04 | -0.8 | Thu 3:00 AM | too few trades (128/200) |
| value_ev5 | 168 | 38.7 | 41.8 | $-188.48 | -11.2% | $811.52 | -1.3 | Wed 6:30 PM | too few trades (168/200) |
| coinflip | 364 | 50.3 | 51.6 | $-216.11 | -5.9% | $783.89 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 177 | 41.2 | 49.0 | $-328.49 | -18.6% | $671.51 | -2.5 | Wed 5:00 PM | too few trades (177/200) |
| momentum_15m_0.10pct | 228 | 43.4 | 49.5 | $-342.24 | -15.0% | $657.76 | -2.3 | done | losing for real |
| always_up | 364 | 45.9 | 50.2 | $-427.10 | -11.7% | $572.90 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 503 | 47.5 | 49.8 | $-226.84 |
| ETH | 577 | 46.8 | 48.8 | $-349.83 |
| SOL | 635 | 49.6 | 48.6 | $-264.44 |
| XRP | 650 | 49.5 | 48.8 | $-386.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
