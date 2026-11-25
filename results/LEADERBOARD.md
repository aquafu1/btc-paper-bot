# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1375 windows, 35733 settled trades, 421 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 714 | 34.2 | 35.3 | $-567.28 | -7.9% | $432.72 | -1.6 | done | can't tell from luck |
| value_ev10 | 1733 | 38.7 | 39.1 | $-816.33 | -4.7% | $183.67 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3572 | 50.8 | 50.1 | $-1055.84 | -3.0% | $-55.84 | -1.8 | done | can't tell from luck |
| value_ev5 | 2609 | 40.4 | 41.1 | $-1308.42 | -5.0% | $-308.42 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2995 | 49.2 | 49.4 | $-1493.06 | -5.0% | $-493.06 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2995 | 50.8 | 50.9 | $-1526.39 | -5.1% | $-526.39 | -2.9 | done | losing for real |
| trend_filter | 2123 | 48.5 | 50.4 | $-1877.96 | -8.8% | $-877.96 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3572 | 49.2 | 50.2 | $-2179.74 | -6.1% | $-1179.74 | -3.7 | done | losing for real |
| coinflip | 5140 | 50.0 | 50.0 | $-2214.78 | -4.3% | $-1214.78 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5140 | 50.1 | 51.3 | $-3199.04 | -6.2% | $-2199.04 | -4.6 | done | losing for real |
| always_up | 5140 | 47.9 | 49.3 | $-3707.24 | -7.2% | $-2707.24 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8870 | 47.9 | 48.8 | $-5172.76 |
| ETH | 9553 | 48.1 | 48.1 | $-5189.09 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
