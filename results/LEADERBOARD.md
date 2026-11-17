# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 651 windows, 17991 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 340 | 34.4 | 35.4 | $-237.49 | -7.0% | $762.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1516 | 50.6 | 49.6 | $-357.95 | -2.4% | $642.05 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1849 | 51.5 | 51.0 | $-563.79 | -3.0% | $436.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 831 | 38.4 | 39.5 | $-570.22 | -6.9% | $429.78 | -1.6 | done | can't tell from luck |
| trend_filter | 1040 | 50.0 | 50.9 | $-621.99 | -6.0% | $378.01 | -2.0 | done | can't tell from luck |
| value_ev5 | 1259 | 40.9 | 41.4 | $-645.58 | -5.1% | $354.42 | -1.6 | done | can't tell from luck |
| coinflip | 2597 | 50.1 | 50.5 | $-1198.90 | -4.6% | $-198.90 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1516 | 49.4 | 51.4 | $-1246.28 | -8.2% | $-246.28 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1849 | 48.5 | 50.0 | $-1269.29 | -6.9% | $-269.29 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2597 | 50.5 | 51.7 | $-1527.38 | -5.9% | $-527.38 | -3.1 | done | losing for real |
| always_up | 2597 | 47.5 | 49.7 | $-2184.02 | -8.4% | $-1184.02 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4076 | 48.3 | 49.3 | $-2451.07 |
| ETH | 4498 | 48.2 | 48.7 | $-2735.50 |
| SOL | 4678 | 48.1 | 48.8 | $-2865.77 |
| XRP | 4739 | 48.4 | 48.6 | $-2370.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
