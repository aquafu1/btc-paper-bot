# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 517 windows, 14263 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1214 | 51.2 | 49.8 | $-182.16 | -1.5% | $817.84 | -0.5 | done | can't tell from luck |
| value_ev20 | 268 | 34.3 | 35.5 | $-194.82 | -7.3% | $805.18 | -0.9 | done | can't tell from luck |
| value_ev10 | 667 | 38.1 | 39.7 | $-506.88 | -7.6% | $493.12 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1447 | 49.8 | 49.6 | $-569.00 | -3.9% | $431.00 | -1.5 | done | can't tell from luck |
| trend_filter | 836 | 49.3 | 50.7 | $-596.88 | -7.1% | $403.12 | -2.1 | done | losing for real |
| value_ev5 | 990 | 39.9 | 41.5 | $-733.60 | -7.4% | $266.40 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1447 | 50.2 | 51.6 | $-984.66 | -6.8% | $15.34 | -2.7 | done | losing for real |
| coinflip | 2060 | 50.0 | 50.7 | $-1091.66 | -5.3% | $-91.66 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1214 | 48.8 | 51.4 | $-1140.77 | -9.4% | $-140.77 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2060 | 49.3 | 51.6 | $-1697.63 | -8.2% | $-697.63 | -3.9 | done | losing for real |
| always_up | 2060 | 46.6 | 50.1 | $-2304.21 | -11.2% | $-1304.21 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3228 | 47.2 | 49.2 | $-2704.60 |
| ETH | 3562 | 47.9 | 48.7 | $-2427.50 |
| SOL | 3716 | 47.7 | 49.0 | $-2681.45 |
| XRP | 3757 | 48.3 | 48.8 | $-2188.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
