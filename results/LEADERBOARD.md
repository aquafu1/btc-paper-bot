# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 670 windows, 18552 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 347 | 34.3 | 35.2 | $-235.88 | -6.8% | $764.12 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1577 | 50.5 | 49.6 | $-392.49 | -2.5% | $607.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 852 | 38.4 | 39.4 | $-548.43 | -6.4% | $451.57 | -1.5 | done | can't tell from luck |
| trend_filter | 1080 | 50.5 | 51.0 | $-555.70 | -5.1% | $444.30 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1903 | 51.4 | 50.8 | $-591.33 | -3.1% | $408.67 | -1.4 | done | can't tell from luck |
| value_ev5 | 1285 | 40.7 | 41.3 | $-673.79 | -5.2% | $326.21 | -1.6 | done | can't tell from luck |
| coinflip | 2676 | 50.1 | 50.4 | $-1181.53 | -4.4% | $-181.53 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1577 | 49.5 | 51.3 | $-1265.54 | -8.0% | $-265.54 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1903 | 48.6 | 50.1 | $-1276.76 | -6.7% | $-276.76 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2676 | 50.8 | 51.8 | $-1463.57 | -5.5% | $-463.57 | -2.9 | done | losing for real |
| always_up | 2676 | 47.3 | 49.7 | $-2343.05 | -8.8% | $-1343.05 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4218 | 48.3 | 49.2 | $-2507.87 |
| ETH | 4625 | 48.3 | 48.6 | $-2786.24 |
| SOL | 4827 | 48.1 | 48.8 | $-2874.05 |
| XRP | 4882 | 48.5 | 48.5 | $-2359.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
