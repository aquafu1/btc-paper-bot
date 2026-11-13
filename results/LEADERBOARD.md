# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 190 windows, 4874 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 474 | 58.0 | 52.5 | $+350.72 | +7.4% | $1350.72 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 356 | 59.8 | 53.1 | $+340.99 | +9.6% | $1340.99 | +1.9 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 5:15 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 755 | 51.9 | 51.4 | $-237.41 | -3.1% | $762.59 | -0.9 | done | can't tell from luck |
| value_ev10 | 247 | 36.4 | 40.8 | $-383.19 | -15.5% | $616.81 | -2.1 | done | losing for real |
| coinflip | 755 | 50.5 | 51.0 | $-414.09 | -5.5% | $585.91 | -1.6 | done | can't tell from luck |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 364 | 38.7 | 42.6 | $-490.29 | -13.5% | $509.71 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 356 | 40.2 | 49.0 | $-768.37 | -21.6% | $231.63 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 474 | 42.0 | 49.7 | $-893.22 | -18.8% | $106.78 | -4.2 | done | losing for real |
| always_up | 755 | 46.4 | 50.2 | $-924.55 | -12.2% | $75.45 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1062 | 46.0 | 49.5 | $-1092.81 |
| ETH | 1214 | 46.0 | 48.8 | $-1360.44 |
| SOL | 1265 | 47.8 | 49.1 | $-1074.73 |
| XRP | 1333 | 49.7 | 49.2 | $-547.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
