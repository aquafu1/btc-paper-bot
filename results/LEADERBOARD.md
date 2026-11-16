# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 546 windows, 15149 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1296 | 51.5 | 49.7 | $-180.40 | -1.4% | $819.60 | -0.5 | done | can't tell from luck |
| value_ev20 | 298 | 32.9 | 35.2 | $-362.88 | -12.2% | $637.12 | -1.6 | done | can't tell from luck |
| trend_filter | 884 | 50.8 | 50.9 | $-433.62 | -4.9% | $566.38 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1533 | 49.8 | 49.8 | $-677.25 | -4.4% | $322.75 | -1.7 | done | can't tell from luck |
| value_ev10 | 717 | 36.7 | 39.4 | $-820.87 | -11.4% | $179.13 | -2.6 | done | losing for real |
| value_ev5 | 1064 | 39.1 | 41.2 | $-1017.93 | -9.6% | $-17.93 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 1533 | 50.2 | 51.2 | $-1091.85 | -7.1% | $-91.85 | -2.9 | done | losing for real |
| coinflip | 2176 | 49.8 | 50.5 | $-1313.83 | -6.0% | $-313.83 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1296 | 48.5 | 51.2 | $-1363.50 | -10.5% | $-363.50 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2176 | 50.2 | 51.7 | $-1564.85 | -7.2% | $-564.85 | -3.5 | done | losing for real |
| always_up | 2176 | 46.7 | 50.0 | $-2461.87 | -11.3% | $-1461.87 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3432 | 47.5 | 49.2 | $-2840.45 |
| ETH | 3779 | 47.8 | 48.6 | $-2789.55 |
| SOL | 3952 | 47.6 | 48.7 | $-3117.39 |
| XRP | 3986 | 48.4 | 48.6 | $-2541.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
