# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 703 windows, 19437 settled trades, 19 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1634 | 50.2 | 49.4 | $-502.57 | -3.1% | $497.43 | -1.2 | done | can't tell from luck |
| value_ev10 | 900 | 38.3 | 39.1 | $-523.27 | -5.8% | $476.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1994 | 51.6 | 50.8 | $-541.68 | -2.7% | $458.32 | -1.2 | done | can't tell from luck |
| value_ev5 | 1353 | 40.8 | 41.1 | $-615.65 | -4.6% | $384.35 | -1.4 | done | can't tell from luck |
| trend_filter | 1132 | 50.3 | 50.9 | $-625.84 | -5.5% | $374.16 | -1.9 | done | can't tell from luck |
| coinflip | 2808 | 50.2 | 50.3 | $-1206.91 | -4.3% | $-206.91 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1634 | 49.8 | 51.4 | $-1240.27 | -7.6% | $-240.27 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1994 | 48.4 | 50.0 | $-1407.93 | -7.1% | $-407.93 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2808 | 51.0 | 51.8 | $-1457.68 | -5.2% | $-457.68 | -2.8 | done | losing for real |
| always_up | 2808 | 47.4 | 49.6 | $-2382.82 | -8.5% | $-1382.82 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4407 | 48.2 | 49.1 | $-2559.29 |
| ETH | 4836 | 48.3 | 48.5 | $-2757.87 |
| SOL | 5070 | 48.2 | 48.7 | $-2893.37 |
| XRP | 5124 | 48.5 | 48.4 | $-2538.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
