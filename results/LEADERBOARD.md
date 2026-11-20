# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 894 windows, 24677 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 463 | 35.6 | 34.9 | $-91.30 | -2.0% | $908.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1133 | 38.2 | 39.1 | $-615.07 | -5.4% | $384.93 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2083 | 49.9 | 49.8 | $-957.19 | -4.6% | $42.81 | -2.1 | done | losing for real |
| trend_filter | 1454 | 50.0 | 51.0 | $-990.35 | -6.8% | $9.65 | -2.7 | done | losing for real |
| value_ev5 | 1713 | 39.9 | 41.0 | $-1019.60 | -6.0% | $-19.60 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2519 | 50.5 | 50.4 | $-1026.12 | -4.1% | $-26.12 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2083 | 50.1 | 50.9 | $-1341.50 | -6.4% | $-341.50 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2519 | 49.5 | 50.4 | $-1364.68 | -5.4% | $-364.68 | -2.7 | done | losing for real |
| coinflip | 3570 | 50.3 | 50.3 | $-1540.96 | -4.3% | $-540.96 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3570 | 51.3 | 51.7 | $-1587.24 | -4.4% | $-587.24 | -2.7 | done | losing for real |
| always_up | 3570 | 46.9 | 49.6 | $-3506.12 | -9.8% | $-2506.12 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5626 | 48.3 | 49.1 | $-2964.45 |
| ETH | 6137 | 48.2 | 48.5 | $-3716.31 |
| SOL | 6438 | 48.2 | 48.6 | $-3681.61 |
| XRP | 6476 | 48.3 | 48.5 | $-3677.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
