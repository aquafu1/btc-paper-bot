# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 518 windows, 14297 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1218 | 51.3 | 49.8 | $-162.81 | -1.3% | $837.19 | -0.5 | done | can't tell from luck |
| value_ev20 | 268 | 34.3 | 35.5 | $-194.82 | -7.3% | $805.18 | -0.9 | done | can't tell from luck |
| value_ev10 | 667 | 38.1 | 39.7 | $-506.88 | -7.6% | $493.12 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1450 | 49.8 | 49.6 | $-557.89 | -3.8% | $442.11 | -1.5 | done | can't tell from luck |
| trend_filter | 840 | 49.4 | 50.7 | $-577.53 | -6.9% | $422.47 | -2.0 | done | losing for real |
| value_ev5 | 991 | 40.0 | 41.5 | $-721.77 | -7.3% | $278.23 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1450 | 50.2 | 51.6 | $-996.08 | -6.9% | $3.92 | -2.7 | done | losing for real |
| coinflip | 2065 | 50.0 | 50.7 | $-1104.83 | -5.4% | $-104.83 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1218 | 48.7 | 51.4 | $-1162.19 | -9.5% | $-162.19 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2065 | 49.3 | 51.6 | $-1688.27 | -8.2% | $-688.27 | -3.9 | done | losing for real |
| always_up | 2065 | 46.6 | 50.1 | $-2276.27 | -11.0% | $-1276.27 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3237 | 47.3 | 49.2 | $-2666.20 |
| ETH | 3571 | 48.0 | 48.7 | $-2386.48 |
| SOL | 3724 | 47.6 | 49.0 | $-2724.28 |
| XRP | 3765 | 48.4 | 48.8 | $-2172.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
