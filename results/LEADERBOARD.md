# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1165 windows, 32213 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1524 | 38.5 | 39.2 | $-819.07 | -5.4% | $180.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3231 | 50.9 | 50.4 | $-1036.64 | -3.2% | $-36.64 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2719 | 49.8 | 49.4 | $-1114.61 | -4.1% | $-114.61 | -2.1 | done | losing for real |
| value_ev5 | 2303 | 40.3 | 41.1 | $-1222.93 | -5.3% | $-222.93 | -2.2 | done | losing for real |
| trend_filter | 1907 | 49.0 | 50.5 | $-1513.93 | -7.9% | $-513.93 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2719 | 50.2 | 51.1 | $-1734.98 | -6.4% | $-734.98 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3231 | 49.1 | 50.2 | $-1969.81 | -6.1% | $-969.81 | -3.5 | done | losing for real |
| coinflip | 4653 | 50.2 | 50.2 | $-1994.87 | -4.3% | $-994.87 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4653 | 50.1 | 51.4 | $-2912.46 | -6.3% | $-1912.46 | -4.4 | done | losing for real |
| always_up | 4653 | 47.8 | 49.3 | $-3415.82 | -7.3% | $-2415.82 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7391 | 48.2 | 49.0 | $-3868.84 |
| ETH | 7989 | 48.2 | 48.4 | $-4645.50 |
| SOL | 8380 | 48.1 | 48.4 | $-4537.96 |
| XRP | 8453 | 48.1 | 48.2 | $-5058.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
