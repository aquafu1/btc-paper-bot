# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 881 windows, 24325 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 460 | 35.7 | 34.9 | $-89.37 | -1.9% | $910.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1118 | 38.4 | 39.1 | $-567.55 | -5.1% | $432.45 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2057 | 50.1 | 49.8 | $-834.03 | -4.1% | $165.97 | -1.8 | done | can't tell from luck |
| trend_filter | 1433 | 50.2 | 50.9 | $-903.49 | -6.3% | $96.51 | -2.5 | done | losing for real |
| value_ev5 | 1688 | 39.9 | 41.0 | $-984.77 | -5.8% | $15.23 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2482 | 50.5 | 50.4 | $-1006.41 | -4.1% | $-6.41 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2482 | 49.5 | 50.4 | $-1362.93 | -5.5% | $-362.93 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2057 | 49.9 | 50.9 | $-1424.99 | -6.9% | $-424.99 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3516 | 51.3 | 51.7 | $-1558.58 | -4.4% | $-558.58 | -2.7 | done | losing for real |
| coinflip | 3516 | 50.2 | 50.3 | $-1568.59 | -4.5% | $-568.59 | -2.7 | done | losing for real |
| always_up | 3516 | 47.0 | 49.6 | $-3394.71 | -9.7% | $-2394.71 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5547 | 48.3 | 49.1 | $-2997.17 |
| ETH | 6052 | 48.2 | 48.5 | $-3743.47 |
| SOL | 6350 | 48.3 | 48.5 | $-3503.92 |
| XRP | 6376 | 48.4 | 48.5 | $-3450.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
