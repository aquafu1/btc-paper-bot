# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 157 windows, 3981 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 286 | 59.1 | 53.1 | $+252.12 | +8.8% | $1252.12 | +1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 383 | 56.4 | 52.4 | $+189.98 | +5.0% | $1189.98 | +1.0 | done | can't tell from luck |
| value_ev20 | 77 | 35.1 | 37.3 | $-98.86 | -12.8% | $901.14 | -0.9 | Sun 2:30 AM | too few trades (77/200) |
| momentum_5m_0.00pct | 620 | 52.3 | 51.3 | $-144.85 | -2.3% | $855.15 | -0.6 | done | can't tell from luck |
| value_ev10 | 204 | 37.7 | 40.8 | $-250.44 | -12.3% | $749.56 | -1.5 | done | can't tell from luck |
| coinflip | 620 | 50.6 | 50.9 | $-315.36 | -5.1% | $684.64 | -1.3 | done | can't tell from luck |
| trend_filter | 203 | 41.9 | 49.2 | $-368.28 | -18.1% | $631.72 | -2.6 | done | losing for real |
| value_ev5 | 299 | 38.8 | 42.4 | $-385.70 | -12.9% | $614.30 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 286 | 40.9 | 49.3 | $-564.69 | -19.7% | $435.31 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 383 | 43.6 | 50.0 | $-601.45 | -15.7% | $398.55 | -3.1 | done | losing for real |
| always_up | 620 | 45.5 | 50.2 | $-849.00 | -13.7% | $151.00 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 860 | 46.2 | 49.7 | $-842.17 |
| ETH | 987 | 45.5 | 48.9 | $-1099.29 |
| SOL | 1048 | 48.1 | 48.9 | $-800.16 |
| XRP | 1086 | 50.1 | 49.1 | $-394.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
