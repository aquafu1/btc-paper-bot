# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 694 windows, 19191 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 369 | 34.1 | 34.9 | $-239.86 | -6.5% | $760.14 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1618 | 50.4 | 49.5 | $-439.72 | -2.7% | $560.28 | -1.1 | done | can't tell from luck |
| value_ev10 | 890 | 38.3 | 39.1 | $-518.76 | -5.8% | $481.24 | -1.4 | done | can't tell from luck |
| trend_filter | 1118 | 50.4 | 50.9 | $-582.75 | -5.2% | $417.25 | -1.8 | done | can't tell from luck |
| value_ev5 | 1338 | 40.9 | 41.1 | $-583.98 | -4.4% | $416.02 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1968 | 51.4 | 50.8 | $-605.19 | -3.1% | $394.81 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 1618 | 49.6 | 51.3 | $-1260.59 | -7.8% | $-260.59 | -3.2 | done | losing for real |
| coinflip | 2768 | 50.0 | 50.3 | $-1270.37 | -4.6% | $-270.37 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1968 | 48.6 | 50.0 | $-1291.31 | -6.6% | $-291.31 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2768 | 50.9 | 51.8 | $-1476.03 | -5.3% | $-476.03 | -2.9 | done | losing for real |
| always_up | 2768 | 47.4 | 49.5 | $-2303.87 | -8.3% | $-1303.87 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4351 | 48.2 | 49.1 | $-2508.53 |
| ETH | 4781 | 48.3 | 48.5 | $-2694.99 |
| SOL | 5006 | 48.1 | 48.6 | $-2913.72 |
| XRP | 5053 | 48.5 | 48.3 | $-2455.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
