# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 900 windows, 24845 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1139 | 38.3 | 39.1 | $-601.46 | -5.3% | $398.54 | -1.4 | done | can't tell from luck |
| value_ev5 | 1722 | 40.0 | 41.0 | $-969.22 | -5.6% | $30.78 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2099 | 49.9 | 49.8 | $-977.80 | -4.7% | $22.20 | -2.1 | done | losing for real |
| trend_filter | 1473 | 50.0 | 51.0 | $-1005.79 | -6.8% | $-5.79 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2532 | 50.4 | 50.4 | $-1033.74 | -4.1% | $-33.74 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2099 | 50.1 | 50.9 | $-1338.95 | -6.4% | $-338.95 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2532 | 49.6 | 50.4 | $-1358.28 | -5.4% | $-358.28 | -2.7 | done | losing for real |
| coinflip | 3595 | 50.3 | 50.3 | $-1523.22 | -4.2% | $-523.22 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3595 | 51.3 | 51.7 | $-1601.69 | -4.5% | $-601.69 | -2.8 | done | losing for real |
| always_up | 3595 | 47.0 | 49.6 | $-3460.48 | -9.6% | $-2460.48 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5664 | 48.3 | 49.1 | $-2990.49 |
| ETH | 6179 | 48.3 | 48.5 | $-3668.74 |
| SOL | 6478 | 48.2 | 48.6 | $-3637.95 |
| XRP | 6524 | 48.3 | 48.5 | $-3674.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
