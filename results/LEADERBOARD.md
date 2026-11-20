# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 897 windows, 24750 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1137 | 38.3 | 39.1 | $-604.14 | -5.3% | $395.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2091 | 50.0 | 49.8 | $-941.40 | -4.5% | $58.60 | -2.1 | done | losing for real |
| trend_filter | 1461 | 50.1 | 51.0 | $-974.54 | -6.7% | $25.46 | -2.6 | done | losing for real |
| value_ev5 | 1718 | 39.9 | 41.0 | $-997.05 | -5.8% | $2.95 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2524 | 50.4 | 50.4 | $-1029.60 | -4.1% | $-29.60 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2524 | 49.6 | 50.4 | $-1363.90 | -5.4% | $-363.90 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2091 | 50.0 | 50.8 | $-1374.98 | -6.6% | $-374.98 | -3.1 | done | losing for real |
| coinflip | 3580 | 50.3 | 50.3 | $-1555.24 | -4.3% | $-555.24 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3580 | 51.3 | 51.7 | $-1601.43 | -4.5% | $-601.43 | -2.8 | done | losing for real |
| always_up | 3580 | 46.8 | 49.6 | $-3559.60 | -9.9% | $-2559.60 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5639 | 48.3 | 49.1 | $-3005.31 |
| ETH | 6157 | 48.3 | 48.5 | $-3735.51 |
| SOL | 6461 | 48.2 | 48.6 | $-3639.91 |
| XRP | 6493 | 48.3 | 48.5 | $-3722.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
