# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 926 windows, 25580 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2178 | 50.2 | 49.8 | $-871.19 | -4.0% | $128.81 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2609 | 50.6 | 50.5 | $-1023.05 | -3.9% | $-23.05 | -2.0 | done | losing for real |
| trend_filter | 1521 | 50.0 | 51.0 | $-1043.57 | -6.9% | $-43.57 | -2.8 | done | losing for real |
| value_ev5 | 1761 | 39.8 | 41.0 | $-1047.50 | -5.9% | $-47.50 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2609 | 49.4 | 50.3 | $-1467.33 | -5.6% | $-467.33 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2178 | 49.8 | 50.9 | $-1536.87 | -7.1% | $-536.87 | -3.4 | done | losing for real |
| coinflip | 3696 | 50.3 | 50.3 | $-1583.98 | -4.3% | $-583.98 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3696 | 50.9 | 51.6 | $-1885.45 | -5.1% | $-885.45 | -3.2 | done | losing for real |
| always_up | 3696 | 46.8 | 49.7 | $-3772.13 | -10.2% | $-2772.13 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5826 | 48.2 | 49.1 | $-3340.04 |
| ETH | 6363 | 48.2 | 48.5 | $-3981.61 |
| SOL | 6674 | 48.1 | 48.6 | $-3904.01 |
| XRP | 6717 | 48.3 | 48.5 | $-3784.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
