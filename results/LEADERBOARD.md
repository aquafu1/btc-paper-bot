# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1668 windows, 39576 settled trades, 363 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 845 | 34.3 | 35.2 | $-644.92 | -7.6% | $355.08 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3886 | 50.8 | 49.9 | $-1004.49 | -2.6% | $-4.49 | -1.6 | done | can't tell from luck |
| value_ev10 | 1997 | 38.4 | 39.0 | $-1122.13 | -5.6% | $-122.13 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3245 | 51.1 | 50.9 | $-1444.75 | -4.5% | $-444.75 | -2.6 | done | losing for real |
| value_ev5 | 2980 | 40.3 | 41.0 | $-1617.97 | -5.4% | $-617.97 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3245 | 48.9 | 49.2 | $-1811.06 | -5.6% | $-811.06 | -3.2 | done | losing for real |
| trend_filter | 2314 | 48.3 | 50.3 | $-2130.50 | -9.2% | $-1130.50 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3886 | 49.2 | 50.2 | $-2378.23 | -6.1% | $-1378.23 | -3.8 | done | losing for real |
| coinflip | 5726 | 49.9 | 49.9 | $-2520.82 | -4.4% | $-1520.82 | -3.3 | done | losing for real |
| always_up | 5726 | 48.3 | 49.0 | $-3560.65 | -6.2% | $-2560.65 | -4.7 | done | losing for real |
| momentum_5m_0.00pct | 5726 | 50.1 | 51.3 | $-3586.84 | -6.3% | $-2586.84 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10686 | 47.9 | 48.5 | $-6002.67 |
| ETH | 11580 | 47.8 | 47.6 | $-6235.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
