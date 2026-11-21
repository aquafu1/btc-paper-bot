# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 965 windows, 26722 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 493 | 34.9 | 34.8 | $-189.50 | -3.8% | $810.50 | -0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2729 | 51.4 | 50.5 | $-677.46 | -2.5% | $322.54 | -1.3 | done | can't tell from luck |
| value_ev10 | 1218 | 38.1 | 39.1 | $-679.76 | -5.6% | $320.24 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2276 | 50.0 | 49.7 | $-943.11 | -4.1% | $56.89 | -2.0 | done | can't tell from luck |
| value_ev5 | 1848 | 39.9 | 41.0 | $-1060.59 | -5.7% | $-60.59 | -2.1 | done | losing for real |
| trend_filter | 1597 | 49.8 | 50.9 | $-1085.09 | -6.8% | $-85.09 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2276 | 50.0 | 51.0 | $-1539.74 | -6.8% | $-539.74 | -3.3 | done | losing for real |
| coinflip | 3852 | 50.2 | 50.4 | $-1741.62 | -4.5% | $-741.62 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2729 | 48.6 | 50.3 | $-1970.32 | -7.2% | $-970.32 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3852 | 50.9 | 51.6 | $-1978.07 | -5.1% | $-978.07 | -3.3 | done | losing for real |
| always_up | 3852 | 46.9 | 49.6 | $-3729.88 | -9.7% | $-2729.88 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6087 | 48.2 | 49.0 | $-3496.46 |
| ETH | 6639 | 48.1 | 48.5 | $-4125.22 |
| SOL | 6980 | 48.3 | 48.6 | $-3751.82 |
| XRP | 7016 | 48.2 | 48.5 | $-4221.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
