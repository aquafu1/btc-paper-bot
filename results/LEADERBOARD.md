# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 700 windows, 19377 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1630 | 50.2 | 49.4 | $-481.28 | -3.0% | $518.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 899 | 38.4 | 39.1 | $-513.27 | -5.7% | $486.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1990 | 51.7 | 50.8 | $-519.96 | -2.6% | $480.04 | -1.2 | done | can't tell from luck |
| value_ev5 | 1350 | 40.8 | 41.1 | $-608.49 | -4.5% | $391.51 | -1.4 | done | can't tell from luck |
| trend_filter | 1131 | 50.2 | 50.9 | $-634.55 | -5.6% | $365.45 | -1.9 | done | can't tell from luck |
| coinflip | 2795 | 50.2 | 50.3 | $-1202.29 | -4.3% | $-202.29 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1630 | 49.8 | 51.4 | $-1255.98 | -7.7% | $-255.98 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1990 | 48.3 | 49.9 | $-1421.22 | -7.1% | $-421.22 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2795 | 50.8 | 51.8 | $-1518.71 | -5.4% | $-518.71 | -3.0 | done | losing for real |
| always_up | 2795 | 47.3 | 49.5 | $-2395.83 | -8.6% | $-1395.83 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4394 | 48.2 | 49.1 | $-2569.51 |
| ETH | 4825 | 48.2 | 48.5 | $-2772.70 |
| SOL | 5057 | 48.2 | 48.6 | $-2942.31 |
| XRP | 5101 | 48.5 | 48.4 | $-2511.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
