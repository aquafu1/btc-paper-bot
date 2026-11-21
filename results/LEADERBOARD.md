# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1002 windows, 27845 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 514 | 34.2 | 34.9 | $-296.26 | -5.8% | $703.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2837 | 51.0 | 50.4 | $-871.54 | -3.1% | $128.46 | -1.6 | done | can't tell from luck |
| value_ev10 | 1274 | 37.5 | 39.1 | $-899.88 | -7.1% | $100.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2392 | 49.9 | 49.7 | $-1061.93 | -4.4% | $-61.93 | -2.2 | done | losing for real |
| trend_filter | 1667 | 49.6 | 50.8 | $-1224.06 | -7.3% | $-224.06 | -3.1 | done | losing for real |
| value_ev5 | 1932 | 39.5 | 41.0 | $-1280.53 | -6.6% | $-280.53 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2392 | 50.1 | 50.9 | $-1595.64 | -6.7% | $-595.64 | -3.3 | done | losing for real |
| coinflip | 4000 | 50.4 | 50.4 | $-1709.20 | -4.3% | $-709.20 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2837 | 49.0 | 50.3 | $-1920.66 | -6.8% | $-920.66 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4000 | 50.7 | 51.5 | $-2220.61 | -5.6% | $-1220.61 | -3.6 | done | losing for real |
| always_up | 4000 | 47.0 | 49.5 | $-3813.81 | -9.5% | $-2813.81 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6345 | 48.2 | 49.0 | $-3586.87 |
| ETH | 6917 | 48.0 | 48.5 | $-4519.69 |
| SOL | 7282 | 48.2 | 48.6 | $-4113.06 |
| XRP | 7301 | 48.1 | 48.4 | $-4674.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
