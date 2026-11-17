# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 589 windows, 16321 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1386 | 51.2 | 49.6 | $-199.29 | -1.4% | $800.71 | -0.5 | done | can't tell from luck |
| value_ev20 | 321 | 34.0 | 35.2 | $-276.40 | -8.6% | $723.60 | -1.2 | done | can't tell from luck |
| trend_filter | 947 | 50.3 | 50.9 | $-534.37 | -5.6% | $465.63 | -1.8 | done | can't tell from luck |
| value_ev10 | 768 | 37.8 | 39.4 | $-645.17 | -8.4% | $354.83 | -1.9 | done | can't tell from luck |
| value_ev5 | 1148 | 40.3 | 41.2 | $-734.66 | -6.4% | $265.34 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1656 | 50.8 | 51.0 | $-832.69 | -5.0% | $167.31 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1656 | 49.2 | 49.9 | $-919.40 | -5.6% | $80.60 | -2.3 | done | losing for real |
| coinflip | 2351 | 49.9 | 50.5 | $-1206.52 | -5.1% | $-206.52 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1386 | 48.8 | 51.3 | $-1355.19 | -9.8% | $-355.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2351 | 50.1 | 51.8 | $-1643.91 | -7.0% | $-643.91 | -3.5 | done | losing for real |
| always_up | 2351 | 47.4 | 49.8 | $-2120.04 | -9.0% | $-1120.04 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3704 | 47.9 | 49.2 | $-2556.43 |
| ETH | 4074 | 48.0 | 48.5 | $-2640.94 |
| SOL | 4247 | 47.8 | 48.7 | $-3012.99 |
| XRP | 4296 | 48.5 | 48.6 | $-2257.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
