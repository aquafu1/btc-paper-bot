# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 427 windows, 11750 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 213 | 34.7 | 36.2 | $-164.42 | -7.7% | $835.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1004 | 50.6 | 50.0 | $-303.31 | -3.0% | $696.69 | -1.0 | done | can't tell from luck |
| value_ev10 | 549 | 39.3 | 40.3 | $-326.49 | -5.9% | $673.51 | -1.2 | done | can't tell from luck |
| trend_filter | 673 | 49.6 | 50.7 | $-415.86 | -6.2% | $584.14 | -1.6 | done | can't tell from luck |
| value_ev5 | 824 | 41.4 | 42.0 | $-434.85 | -5.3% | $565.15 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1190 | 49.2 | 50.0 | $-621.61 | -5.2% | $378.39 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1190 | 50.8 | 51.7 | $-698.72 | -5.9% | $301.28 | -2.1 | done | losing for real |
| coinflip | 1701 | 50.6 | 50.9 | $-744.22 | -4.4% | $255.78 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1004 | 49.4 | 51.8 | $-888.23 | -8.8% | $111.77 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1701 | 49.6 | 51.6 | $-1267.61 | -7.5% | $-267.61 | -3.2 | done | losing for real |
| always_up | 1701 | 46.1 | 50.5 | $-2084.56 | -12.3% | $-1084.56 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2659 | 47.6 | 49.4 | $-2034.64 |
| ETH | 2945 | 48.0 | 48.9 | $-1869.80 |
| SOL | 3045 | 47.8 | 49.4 | $-2381.45 |
| XRP | 3101 | 48.8 | 49.3 | $-1663.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
