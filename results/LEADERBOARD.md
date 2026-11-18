# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 707 windows, 19500 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1636 | 50.1 | 49.4 | $-522.57 | -3.2% | $477.43 | -1.3 | done | can't tell from luck |
| value_ev10 | 902 | 38.2 | 39.1 | $-543.27 | -6.0% | $456.73 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2000 | 51.5 | 50.8 | $-561.41 | -2.8% | $438.59 | -1.3 | done | can't tell from luck |
| value_ev5 | 1358 | 40.8 | 41.1 | $-622.92 | -4.6% | $377.08 | -1.4 | done | can't tell from luck |
| trend_filter | 1135 | 50.2 | 50.9 | $-635.44 | -5.6% | $364.56 | -1.9 | done | can't tell from luck |
| coinflip | 2820 | 50.2 | 50.3 | $-1174.85 | -4.2% | $-174.85 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1636 | 49.9 | 51.4 | $-1220.00 | -7.5% | $-220.00 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2000 | 48.4 | 50.0 | $-1389.93 | -6.9% | $-389.93 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2820 | 51.0 | 51.8 | $-1428.69 | -5.1% | $-428.69 | -2.8 | done | losing for real |
| always_up | 2820 | 47.3 | 49.6 | $-2450.46 | -8.7% | $-1450.46 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4418 | 48.2 | 49.1 | $-2595.39 |
| ETH | 4849 | 48.3 | 48.5 | $-2744.73 |
| SOL | 5090 | 48.2 | 48.7 | $-2889.67 |
| XRP | 5143 | 48.5 | 48.4 | $-2573.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
