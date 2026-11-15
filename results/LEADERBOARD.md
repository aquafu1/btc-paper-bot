# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 464 windows, 12741 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 236 | 34.7 | 35.9 | $-162.48 | -6.9% | $837.52 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1078 | 50.8 | 49.9 | $-282.42 | -2.6% | $717.58 | -0.9 | done | can't tell from luck |
| value_ev10 | 603 | 39.0 | 40.1 | $-383.68 | -6.4% | $616.32 | -1.3 | done | can't tell from luck |
| trend_filter | 736 | 49.9 | 50.7 | $-412.44 | -5.6% | $587.56 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1286 | 49.8 | 50.0 | $-496.49 | -3.9% | $503.51 | -1.4 | done | can't tell from luck |
| value_ev5 | 891 | 41.0 | 41.8 | $-517.06 | -5.8% | $482.94 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1286 | 50.2 | 51.6 | $-912.29 | -7.1% | $87.71 | -2.7 | done | losing for real |
| coinflip | 1849 | 50.0 | 50.8 | $-1006.09 | -5.4% | $-6.09 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1078 | 49.2 | 51.8 | $-1014.14 | -9.4% | $-14.14 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1849 | 49.9 | 51.6 | $-1254.77 | -6.8% | $-254.77 | -3.0 | done | losing for real |
| always_up | 1849 | 46.2 | 50.4 | $-2237.62 | -12.1% | $-1237.62 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2888 | 47.6 | 49.2 | $-2218.14 |
| ETH | 3195 | 48.1 | 48.8 | $-2038.65 |
| SOL | 3317 | 47.7 | 49.3 | $-2569.98 |
| XRP | 3341 | 48.5 | 49.1 | $-1852.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
