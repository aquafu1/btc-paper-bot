# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 551 windows, 15290 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1306 | 51.4 | 49.7 | $-218.15 | -1.7% | $781.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 301 | 33.2 | 35.2 | $-334.71 | -11.1% | $665.29 | -1.5 | done | can't tell from luck |
| trend_filter | 890 | 50.6 | 51.0 | $-479.63 | -5.4% | $520.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 724 | 37.0 | 39.4 | $-762.52 | -10.5% | $237.48 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1549 | 49.5 | 49.8 | $-771.16 | -5.0% | $228.84 | -2.0 | done | can't tell from luck |
| value_ev5 | 1077 | 39.5 | 41.2 | $-925.81 | -8.6% | $74.19 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 1549 | 50.5 | 51.2 | $-982.76 | -6.3% | $17.24 | -2.6 | done | losing for real |
| coinflip | 2196 | 50.0 | 50.5 | $-1223.75 | -5.6% | $-223.75 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1306 | 48.6 | 51.2 | $-1324.37 | -10.1% | $-324.37 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2196 | 50.1 | 51.8 | $-1619.88 | -7.4% | $-619.88 | -3.6 | done | losing for real |
| always_up | 2196 | 46.8 | 49.9 | $-2390.52 | -10.9% | $-1390.52 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3458 | 47.5 | 49.2 | $-2795.20 |
| ETH | 3811 | 47.9 | 48.6 | $-2741.39 |
| SOL | 3992 | 47.7 | 48.7 | $-3101.57 |
| XRP | 4029 | 48.5 | 48.6 | $-2395.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
