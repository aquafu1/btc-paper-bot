# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 699 windows, 19352 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 371 | 34.0 | 34.9 | $-259.86 | -7.0% | $740.14 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1630 | 50.2 | 49.4 | $-481.28 | -3.0% | $518.72 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 1988 | 51.7 | 50.8 | $-522.80 | -2.6% | $477.20 | -1.2 | done | can't tell from luck |
| value_ev10 | 896 | 38.2 | 39.1 | $-554.89 | -6.2% | $445.11 | -1.5 | done | can't tell from luck |
| trend_filter | 1129 | 50.2 | 50.9 | $-636.39 | -5.6% | $363.61 | -1.9 | done | can't tell from luck |
| value_ev5 | 1347 | 40.7 | 41.1 | $-650.11 | -4.8% | $349.89 | -1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 1630 | 49.8 | 51.4 | $-1255.98 | -7.7% | $-255.98 | -3.2 | done | losing for real |
| coinflip | 2791 | 50.1 | 50.3 | $-1256.76 | -4.5% | $-256.76 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1988 | 48.3 | 49.9 | $-1423.05 | -7.2% | $-423.05 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2791 | 50.9 | 51.8 | $-1500.54 | -5.4% | $-500.54 | -2.9 | done | losing for real |
| always_up | 2791 | 47.4 | 49.5 | $-2355.83 | -8.4% | $-1355.83 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4382 | 48.2 | 49.1 | $-2598.53 |
| ETH | 4820 | 48.2 | 48.5 | $-2794.55 |
| SOL | 5049 | 48.1 | 48.6 | $-2993.33 |
| XRP | 5101 | 48.5 | 48.4 | $-2511.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
