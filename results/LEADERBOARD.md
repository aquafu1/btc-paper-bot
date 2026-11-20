# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 899 windows, 24811 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1138 | 38.3 | 39.1 | $-591.46 | -5.2% | $408.54 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2095 | 49.9 | 49.8 | $-958.72 | -4.6% | $41.28 | -2.1 | done | losing for real |
| value_ev5 | 1721 | 40.0 | 41.0 | $-959.22 | -5.6% | $40.78 | -1.9 | done | can't tell from luck |
| trend_filter | 1469 | 50.0 | 51.0 | $-986.71 | -6.7% | $13.29 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2528 | 50.4 | 50.4 | $-1051.35 | -4.2% | $-51.35 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2528 | 49.6 | 50.4 | $-1339.20 | -5.3% | $-339.20 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2095 | 50.1 | 50.9 | $-1356.56 | -6.5% | $-356.56 | -3.0 | done | losing for real |
| coinflip | 3591 | 50.3 | 50.3 | $-1540.83 | -4.3% | $-540.83 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3591 | 51.3 | 51.7 | $-1582.61 | -4.4% | $-582.61 | -2.7 | done | losing for real |
| always_up | 3591 | 47.0 | 49.6 | $-3441.39 | -9.6% | $-2441.39 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5648 | 48.3 | 49.1 | $-2994.11 |
| ETH | 6171 | 48.3 | 48.5 | $-3651.49 |
| SOL | 6478 | 48.2 | 48.6 | $-3637.95 |
| XRP | 6514 | 48.3 | 48.5 | $-3625.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
