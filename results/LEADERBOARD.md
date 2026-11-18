# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 689 windows, 19068 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 364 | 34.1 | 35.0 | $-253.12 | -7.0% | $746.88 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1610 | 50.3 | 49.5 | $-469.87 | -2.9% | $530.13 | -1.2 | done | can't tell from luck |
| value_ev10 | 883 | 38.3 | 39.2 | $-539.28 | -6.1% | $460.72 | -1.5 | done | can't tell from luck |
| trend_filter | 1111 | 50.4 | 50.9 | $-593.14 | -5.3% | $406.86 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1960 | 51.4 | 50.8 | $-623.33 | -3.2% | $376.67 | -1.4 | done | can't tell from luck |
| value_ev5 | 1326 | 40.7 | 41.1 | $-639.40 | -4.8% | $360.60 | -1.5 | done | can't tell from luck |
| coinflip | 2748 | 50.1 | 50.3 | $-1194.48 | -4.3% | $-194.48 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1610 | 49.7 | 51.3 | $-1238.58 | -7.7% | $-238.58 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1960 | 48.6 | 49.9 | $-1281.20 | -6.5% | $-281.20 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2748 | 50.8 | 51.8 | $-1508.59 | -5.5% | $-508.59 | -3.0 | done | losing for real |
| always_up | 2748 | 47.5 | 49.6 | $-2309.90 | -8.4% | $-1309.90 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4333 | 48.3 | 49.1 | $-2532.59 |
| ETH | 4748 | 48.3 | 48.6 | $-2854.43 |
| SOL | 4971 | 48.2 | 48.6 | $-2869.76 |
| XRP | 5016 | 48.5 | 48.4 | $-2394.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
