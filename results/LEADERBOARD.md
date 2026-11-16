# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 540 windows, 14956 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1279 | 51.4 | 49.8 | $-166.07 | -1.3% | $833.93 | -0.5 | done | can't tell from luck |
| value_ev20 | 286 | 33.9 | 35.5 | $-272.64 | -9.5% | $727.36 | -1.2 | done | can't tell from luck |
| trend_filter | 871 | 50.6 | 50.9 | $-426.33 | -4.9% | $573.67 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1517 | 49.8 | 49.7 | $-640.49 | -4.2% | $359.51 | -1.6 | done | can't tell from luck |
| value_ev10 | 702 | 37.3 | 39.7 | $-700.63 | -10.0% | $299.37 | -2.2 | done | losing for real |
| value_ev5 | 1046 | 39.5 | 41.4 | $-916.07 | -8.8% | $83.93 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 1517 | 50.2 | 51.3 | $-1074.76 | -7.1% | $-74.76 | -2.8 | done | losing for real |
| coinflip | 2153 | 49.8 | 50.6 | $-1255.28 | -5.8% | $-255.28 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1279 | 48.6 | 51.3 | $-1290.02 | -10.1% | $-290.02 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2153 | 50.1 | 51.7 | $-1523.52 | -7.1% | $-523.52 | -3.4 | done | losing for real |
| always_up | 2153 | 46.6 | 50.1 | $-2450.17 | -11.4% | $-1450.17 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3389 | 47.5 | 49.2 | $-2761.94 |
| ETH | 3738 | 48.0 | 48.7 | $-2589.81 |
| SOL | 3897 | 47.6 | 48.9 | $-3016.62 |
| XRP | 3932 | 48.4 | 48.8 | $-2347.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
