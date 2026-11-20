# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 876 windows, 24173 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 454 | 35.5 | 34.9 | $-126.41 | -2.8% | $873.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1107 | 38.4 | 39.1 | $-581.80 | -5.3% | $418.20 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2043 | 50.1 | 49.8 | $-833.25 | -4.1% | $166.75 | -1.8 | done | can't tell from luck |
| trend_filter | 1425 | 50.2 | 51.0 | $-944.70 | -6.6% | $55.30 | -2.6 | done | losing for real |
| value_ev5 | 1673 | 40.0 | 41.0 | $-959.02 | -5.7% | $40.98 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2470 | 50.5 | 50.5 | $-1001.51 | -4.1% | $-1.51 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2470 | 49.5 | 50.4 | $-1374.48 | -5.6% | $-374.48 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2043 | 49.9 | 51.0 | $-1431.12 | -7.0% | $-431.12 | -3.2 | done | losing for real |
| coinflip | 3496 | 50.1 | 50.3 | $-1569.98 | -4.5% | $-569.98 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3496 | 51.3 | 51.8 | $-1625.03 | -4.6% | $-625.03 | -2.8 | done | losing for real |
| always_up | 3496 | 46.9 | 49.6 | $-3454.87 | -9.9% | $-2454.87 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5517 | 48.3 | 49.1 | $-2972.87 |
| ETH | 6012 | 48.1 | 48.6 | $-3844.91 |
| SOL | 6309 | 48.3 | 48.6 | $-3597.39 |
| XRP | 6335 | 48.4 | 48.5 | $-3487.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
