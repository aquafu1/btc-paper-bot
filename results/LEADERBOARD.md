# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1159 windows, 32029 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 617 | 34.7 | 35.3 | $-372.55 | -6.0% | $627.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1511 | 38.4 | 39.2 | $-836.83 | -5.5% | $163.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3215 | 50.7 | 50.4 | $-1098.55 | -3.4% | $-98.55 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2702 | 49.8 | 49.5 | $-1111.15 | -4.1% | $-111.15 | -2.1 | done | losing for real |
| value_ev5 | 2284 | 40.3 | 41.1 | $-1224.63 | -5.4% | $-224.63 | -2.2 | done | losing for real |
| trend_filter | 1899 | 49.1 | 50.5 | $-1472.25 | -7.8% | $-472.25 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2702 | 50.2 | 51.0 | $-1739.04 | -6.4% | $-739.04 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3215 | 49.3 | 50.2 | $-1878.28 | -5.8% | $-878.28 | -3.3 | done | losing for real |
| coinflip | 4628 | 50.2 | 50.2 | $-1964.29 | -4.2% | $-964.29 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4628 | 50.2 | 51.4 | $-2871.83 | -6.2% | $-1871.83 | -4.3 | done | losing for real |
| always_up | 4628 | 47.8 | 49.3 | $-3420.17 | -7.4% | $-2420.17 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7341 | 48.2 | 49.0 | $-3820.92 |
| ETH | 7940 | 48.2 | 48.4 | $-4609.52 |
| SOL | 8337 | 48.1 | 48.4 | $-4545.22 |
| XRP | 8411 | 48.1 | 48.2 | $-5013.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
