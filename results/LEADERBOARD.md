# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1581 windows, 38475 settled trades, 385 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 809 | 34.5 | 35.1 | $-569.27 | -7.0% | $430.73 | -1.5 | done | can't tell from luck |
| value_ev10 | 1909 | 38.6 | 39.0 | $-948.56 | -5.0% | $51.44 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3800 | 50.9 | 50.0 | $-971.13 | -2.6% | $28.87 | -1.6 | done | can't tell from luck |
| value_ev5 | 2865 | 40.5 | 41.0 | $-1417.94 | -4.9% | $-417.94 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3186 | 51.0 | 50.9 | $-1497.76 | -4.7% | $-497.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3186 | 49.0 | 49.2 | $-1678.08 | -5.3% | $-678.08 | -3.0 | done | losing for real |
| trend_filter | 2264 | 48.5 | 50.3 | $-1982.39 | -8.8% | $-982.39 | -4.3 | done | losing for real |
| coinflip | 5552 | 50.1 | 49.9 | $-2308.51 | -4.2% | $-1308.51 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3800 | 49.1 | 50.2 | $-2359.22 | -6.2% | $-1359.22 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5552 | 50.1 | 51.3 | $-3461.81 | -6.2% | $-2461.81 | -4.8 | done | losing for real |
| always_up | 5552 | 48.2 | 49.1 | $-3518.95 | -6.3% | $-2518.95 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10176 | 48.0 | 48.6 | $-5679.82 |
| ETH | 10989 | 48.0 | 47.7 | $-5449.56 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
