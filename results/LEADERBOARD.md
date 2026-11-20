# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 895 windows, 24690 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 463 | 35.6 | 34.9 | $-91.30 | -2.0% | $908.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1134 | 38.3 | 39.1 | $-602.74 | -5.3% | $397.26 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2083 | 49.9 | 49.8 | $-957.19 | -4.6% | $42.81 | -2.1 | done | losing for real |
| trend_filter | 1456 | 50.1 | 51.0 | $-966.39 | -6.6% | $33.61 | -2.6 | done | losing for real |
| value_ev5 | 1715 | 39.9 | 41.0 | $-995.65 | -5.8% | $4.35 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2520 | 50.4 | 50.4 | $-1036.12 | -4.1% | $-36.12 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2083 | 50.1 | 50.9 | $-1341.50 | -6.4% | $-341.50 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2520 | 49.6 | 50.4 | $-1352.36 | -5.4% | $-352.36 | -2.7 | done | losing for real |
| coinflip | 3572 | 50.3 | 50.3 | $-1539.33 | -4.3% | $-539.33 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3572 | 51.3 | 51.7 | $-1563.28 | -4.4% | $-563.28 | -2.7 | done | losing for real |
| always_up | 3572 | 46.9 | 49.7 | $-3526.12 | -9.9% | $-2526.12 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5626 | 48.3 | 49.1 | $-2964.45 |
| ETH | 6142 | 48.3 | 48.5 | $-3679.77 |
| SOL | 6446 | 48.2 | 48.6 | $-3650.01 |
| XRP | 6476 | 48.3 | 48.5 | $-3677.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
