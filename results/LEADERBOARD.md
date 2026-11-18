# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 697 windows, 19295 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 370 | 34.1 | 34.9 | $-249.86 | -6.8% | $750.14 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1625 | 50.3 | 49.4 | $-473.32 | -2.9% | $526.68 | -1.2 | done | can't tell from luck |
| value_ev10 | 892 | 38.3 | 39.1 | $-514.89 | -5.8% | $485.11 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1982 | 51.6 | 50.8 | $-550.19 | -2.8% | $449.81 | -1.2 | done | can't tell from luck |
| value_ev5 | 1342 | 40.8 | 41.1 | $-600.11 | -4.5% | $399.89 | -1.4 | done | can't tell from luck |
| trend_filter | 1125 | 50.3 | 50.9 | $-616.36 | -5.5% | $383.64 | -1.9 | done | can't tell from luck |
| coinflip | 2784 | 50.1 | 50.3 | $-1219.77 | -4.4% | $-219.77 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1625 | 49.7 | 51.3 | $-1255.59 | -7.7% | $-255.59 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1982 | 48.4 | 50.0 | $-1380.36 | -7.0% | $-380.36 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2784 | 50.9 | 51.8 | $-1466.45 | -5.3% | $-466.45 | -2.9 | done | losing for real |
| always_up | 2784 | 47.3 | 49.5 | $-2374.58 | -8.5% | $-1374.58 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4373 | 48.2 | 49.1 | $-2555.63 |
| ETH | 4805 | 48.3 | 48.5 | $-2748.39 |
| SOL | 5032 | 48.2 | 48.6 | $-2932.29 |
| XRP | 5085 | 48.6 | 48.4 | $-2465.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
