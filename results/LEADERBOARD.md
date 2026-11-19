# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 852 windows, 23505 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 442 | 34.4 | 34.8 | $-245.60 | -5.6% | $754.40 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1988 | 50.3 | 49.7 | $-721.07 | -3.6% | $278.93 | -1.6 | done | can't tell from luck |
| value_ev10 | 1077 | 37.8 | 39.0 | $-721.99 | -6.7% | $278.01 | -1.8 | done | can't tell from luck |
| trend_filter | 1384 | 50.2 | 50.9 | $-872.50 | -6.3% | $127.50 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2401 | 50.6 | 50.5 | $-958.52 | -4.0% | $41.48 | -2.0 | done | can't tell from luck |
| value_ev5 | 1624 | 39.8 | 41.0 | $-1034.54 | -6.4% | $-34.54 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2401 | 49.4 | 50.3 | $-1399.72 | -5.8% | $-399.72 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1988 | 49.7 | 51.1 | $-1525.54 | -7.7% | $-525.54 | -3.5 | done | losing for real |
| coinflip | 3400 | 50.2 | 50.3 | $-1529.03 | -4.5% | $-529.03 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3400 | 51.3 | 51.7 | $-1560.10 | -4.6% | $-560.10 | -2.8 | done | losing for real |
| always_up | 3400 | 47.0 | 49.5 | $-3248.00 | -9.6% | $-2248.00 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5354 | 48.3 | 49.0 | $-2995.60 |
| ETH | 5853 | 48.0 | 48.5 | $-3862.17 |
| SOL | 6128 | 48.2 | 48.5 | $-3575.94 |
| XRP | 6170 | 48.4 | 48.5 | $-3382.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
