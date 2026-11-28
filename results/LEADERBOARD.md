# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1626 windows, 39063 settled trades, 353 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 827 | 34.5 | 35.2 | $-595.19 | -7.2% | $404.81 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3849 | 50.8 | 50.0 | $-1034.52 | -2.7% | $-34.52 | -1.7 | done | can't tell from luck |
| value_ev10 | 1956 | 38.3 | 39.0 | $-1088.52 | -5.6% | $-88.52 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3220 | 51.0 | 50.9 | $-1495.66 | -4.6% | $-495.66 | -2.7 | done | losing for real |
| value_ev5 | 2925 | 40.4 | 41.0 | $-1511.06 | -5.2% | $-511.06 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3220 | 49.0 | 49.2 | $-1734.92 | -5.4% | $-734.92 | -3.0 | done | losing for real |
| trend_filter | 2291 | 48.5 | 50.4 | $-2007.13 | -8.8% | $-1007.13 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3849 | 49.2 | 50.2 | $-2336.42 | -6.1% | $-1336.42 | -3.8 | done | losing for real |
| coinflip | 5642 | 50.1 | 49.9 | $-2348.66 | -4.2% | $-1348.66 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5642 | 50.2 | 51.3 | $-3409.47 | -6.0% | $-2409.47 | -4.7 | done | losing for real |
| always_up | 5642 | 48.2 | 49.1 | $-3561.90 | -6.3% | $-2561.90 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10443 | 48.0 | 48.6 | $-5807.64 |
| ETH | 11310 | 48.0 | 47.7 | $-5731.58 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
