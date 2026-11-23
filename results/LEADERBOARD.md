# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1160 windows, 32064 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 617 | 34.7 | 35.3 | $-372.55 | -6.0% | $627.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1514 | 38.4 | 39.2 | $-842.59 | -5.6% | $157.41 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3219 | 50.8 | 50.4 | $-1087.50 | -3.4% | $-87.50 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2706 | 49.8 | 49.5 | $-1126.90 | -4.2% | $-126.90 | -2.2 | done | losing for real |
| value_ev5 | 2288 | 40.3 | 41.1 | $-1240.38 | -5.4% | $-240.38 | -2.2 | done | losing for real |
| trend_filter | 1899 | 49.1 | 50.5 | $-1472.25 | -7.8% | $-472.25 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2706 | 50.2 | 51.0 | $-1728.00 | -6.4% | $-728.00 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3219 | 49.2 | 50.2 | $-1894.04 | -5.9% | $-894.04 | -3.4 | done | losing for real |
| coinflip | 4632 | 50.2 | 50.2 | $-1970.71 | -4.3% | $-970.71 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4632 | 50.2 | 51.4 | $-2860.78 | -6.2% | $-1860.78 | -4.3 | done | losing for real |
| always_up | 4632 | 47.8 | 49.3 | $-3435.92 | -7.4% | $-2435.92 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7350 | 48.2 | 49.0 | $-3844.52 |
| ETH | 7949 | 48.2 | 48.4 | $-4578.29 |
| SOL | 8345 | 48.1 | 48.4 | $-4572.81 |
| XRP | 8420 | 48.1 | 48.2 | $-5036.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
