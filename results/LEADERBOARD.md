# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 882 windows, 24355 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 460 | 35.7 | 34.9 | $-89.37 | -1.9% | $910.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1118 | 38.4 | 39.1 | $-567.55 | -5.1% | $432.45 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2061 | 50.1 | 49.8 | $-850.65 | -4.1% | $149.35 | -1.9 | done | can't tell from luck |
| trend_filter | 1434 | 50.3 | 50.9 | $-890.11 | -6.2% | $109.89 | -2.4 | done | losing for real |
| value_ev5 | 1689 | 39.9 | 41.0 | $-994.77 | -5.9% | $5.23 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2486 | 50.5 | 50.4 | $-999.74 | -4.0% | $0.26 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2486 | 49.5 | 50.4 | $-1379.55 | -5.5% | $-379.55 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2061 | 49.9 | 50.9 | $-1418.31 | -6.9% | $-418.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3520 | 51.4 | 51.7 | $-1528.52 | -4.3% | $-528.52 | -2.7 | done | losing for real |
| coinflip | 3520 | 50.2 | 50.3 | $-1567.90 | -4.5% | $-567.90 | -2.7 | done | losing for real |
| always_up | 3520 | 46.9 | 49.6 | $-3411.32 | -9.7% | $-2411.32 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5554 | 48.3 | 49.1 | $-2997.95 |
| ETH | 6060 | 48.2 | 48.5 | $-3683.17 |
| SOL | 6357 | 48.3 | 48.5 | $-3530.18 |
| XRP | 6384 | 48.4 | 48.5 | $-3486.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
