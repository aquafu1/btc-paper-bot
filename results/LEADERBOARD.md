# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1116 windows, 30887 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 589 | 34.6 | 35.1 | $-339.77 | -5.8% | $660.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3116 | 51.2 | 50.5 | $-828.91 | -2.7% | $171.09 | -1.5 | done | can't tell from luck |
| value_ev10 | 1441 | 38.1 | 39.1 | $-880.86 | -6.1% | $119.14 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2620 | 49.8 | 49.4 | $-1064.47 | -4.1% | $-64.47 | -2.1 | done | losing for real |
| value_ev5 | 2182 | 40.1 | 41.0 | $-1246.70 | -5.7% | $-246.70 | -2.3 | done | losing for real |
| trend_filter | 1829 | 49.2 | 50.4 | $-1378.35 | -7.5% | $-378.35 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2620 | 50.2 | 51.1 | $-1707.37 | -6.5% | $-707.37 | -3.4 | done | losing for real |
| coinflip | 4458 | 50.4 | 50.2 | $-1749.38 | -3.9% | $-749.38 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3116 | 48.8 | 50.2 | $-2077.23 | -6.7% | $-1077.23 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4458 | 50.5 | 51.4 | $-2523.06 | -5.7% | $-1523.06 | -3.9 | done | losing for real |
| always_up | 4458 | 47.7 | 49.3 | $-3429.71 | -7.7% | $-2429.71 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7079 | 48.4 | 49.0 | $-3573.30 |
| ETH | 7656 | 48.1 | 48.4 | $-4609.02 |
| SOL | 8031 | 48.1 | 48.4 | $-4475.83 |
| XRP | 8121 | 48.2 | 48.2 | $-4567.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
