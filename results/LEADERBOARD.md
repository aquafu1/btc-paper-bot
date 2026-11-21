# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 976 windows, 27094 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 499 | 34.5 | 34.9 | $-249.50 | -5.0% | $750.50 | -0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2767 | 51.2 | 50.4 | $-741.98 | -2.7% | $258.02 | -1.4 | done | can't tell from luck |
| value_ev10 | 1238 | 37.8 | 39.1 | $-788.71 | -6.4% | $211.29 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2318 | 50.1 | 49.7 | $-915.34 | -3.9% | $84.66 | -1.9 | done | can't tell from luck |
| value_ev5 | 1876 | 39.8 | 41.0 | $-1137.45 | -6.1% | $-137.45 | -2.2 | done | losing for real |
| trend_filter | 1623 | 49.7 | 50.9 | $-1152.26 | -7.1% | $-152.26 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2318 | 49.9 | 50.9 | $-1638.61 | -7.1% | $-638.61 | -3.5 | done | losing for real |
| coinflip | 3896 | 50.2 | 50.3 | $-1820.16 | -4.7% | $-820.16 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2767 | 48.8 | 50.3 | $-1971.73 | -7.1% | $-971.73 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3896 | 50.7 | 51.5 | $-2132.30 | -5.5% | $-1132.30 | -3.5 | done | losing for real |
| always_up | 3896 | 46.8 | 49.6 | $-3927.20 | -10.1% | $-2927.20 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6174 | 48.2 | 49.1 | $-3552.07 |
| ETH | 6737 | 48.0 | 48.5 | $-4407.99 |
| SOL | 7077 | 48.1 | 48.6 | $-4100.24 |
| XRP | 7106 | 48.1 | 48.4 | $-4414.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
