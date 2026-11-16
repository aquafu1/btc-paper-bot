# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 492 windows, 13515 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 250 | 34.4 | 35.8 | $-179.21 | -7.2% | $820.79 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1147 | 50.9 | 49.8 | $-227.40 | -2.0% | $772.60 | -0.7 | done | can't tell from luck |
| value_ev10 | 635 | 38.6 | 40.0 | $-430.56 | -6.8% | $569.44 | -1.4 | done | can't tell from luck |
| trend_filter | 790 | 49.5 | 50.7 | $-537.16 | -6.8% | $462.84 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1363 | 49.7 | 49.9 | $-538.56 | -4.0% | $461.44 | -1.5 | done | can't tell from luck |
| value_ev5 | 940 | 40.7 | 41.7 | $-546.78 | -5.8% | $453.22 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1363 | 50.3 | 51.5 | $-891.24 | -6.5% | $108.76 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1147 | 49.1 | 51.5 | $-1009.80 | -8.8% | $-9.80 | -3.1 | done | losing for real |
| coinflip | 1960 | 50.0 | 50.8 | $-1011.63 | -5.2% | $-11.63 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1960 | 49.7 | 51.7 | $-1424.94 | -7.3% | $-424.94 | -3.3 | done | losing for real |
| always_up | 1960 | 46.4 | 50.3 | $-2263.00 | -11.5% | $-1263.00 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3046 | 47.4 | 49.3 | $-2435.00 |
| ETH | 3386 | 48.1 | 48.8 | $-2177.60 |
| SOL | 3528 | 47.8 | 49.2 | $-2540.00 |
| XRP | 3555 | 48.5 | 48.9 | $-1907.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
