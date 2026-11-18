# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 708 windows, 19529 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1638 | 50.2 | 49.5 | $-513.35 | -3.1% | $486.65 | -1.3 | done | can't tell from luck |
| value_ev10 | 903 | 38.3 | 39.1 | $-522.57 | -5.8% | $477.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2004 | 51.5 | 50.7 | $-532.47 | -2.7% | $467.53 | -1.2 | done | can't tell from luck |
| value_ev5 | 1359 | 40.8 | 41.1 | $-602.22 | -4.4% | $397.78 | -1.4 | done | can't tell from luck |
| trend_filter | 1138 | 50.3 | 50.9 | $-636.23 | -5.6% | $363.77 | -1.9 | done | can't tell from luck |
| coinflip | 2824 | 50.2 | 50.3 | $-1200.87 | -4.3% | $-200.87 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1638 | 49.8 | 51.3 | $-1240.00 | -7.6% | $-240.00 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2004 | 48.5 | 50.0 | $-1400.71 | -7.0% | $-400.71 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2824 | 51.0 | 51.8 | $-1439.47 | -5.1% | $-439.47 | -2.8 | done | losing for real |
| always_up | 2824 | 47.3 | 49.5 | $-2421.52 | -8.6% | $-1421.52 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4426 | 48.2 | 49.1 | $-2614.47 |
| ETH | 4857 | 48.3 | 48.5 | $-2754.80 |
| SOL | 5096 | 48.2 | 48.7 | $-2873.19 |
| XRP | 5150 | 48.5 | 48.4 | $-2520.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
