# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1432 windows, 36566 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 738 | 34.6 | 35.3 | $-513.47 | -7.0% | $486.53 | -1.4 | done | can't tell from luck |
| value_ev10 | 1777 | 38.8 | 39.1 | $-811.46 | -4.6% | $188.54 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3650 | 50.9 | 50.0 | $-976.63 | -2.7% | $23.37 | -1.6 | done | can't tell from luck |
| value_ev5 | 2679 | 40.5 | 41.1 | $-1295.90 | -4.8% | $-295.90 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3066 | 49.2 | 49.3 | $-1509.67 | -4.9% | $-509.67 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3066 | 50.8 | 51.0 | $-1574.04 | -5.1% | $-574.04 | -2.9 | done | losing for real |
| trend_filter | 2172 | 48.6 | 50.3 | $-1880.11 | -8.7% | $-880.11 | -4.1 | done | losing for real |
| coinflip | 5256 | 50.1 | 50.0 | $-2181.85 | -4.2% | $-1181.85 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3650 | 49.1 | 50.2 | $-2267.33 | -6.2% | $-1267.33 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5256 | 50.2 | 51.3 | $-3243.72 | -6.2% | $-2243.72 | -4.6 | done | losing for real |
| always_up | 5256 | 48.0 | 49.2 | $-3597.28 | -6.8% | $-2597.28 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9279 | 48.1 | 48.7 | $-4807.70 |
| ETH | 9977 | 48.0 | 48.0 | $-5459.53 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
