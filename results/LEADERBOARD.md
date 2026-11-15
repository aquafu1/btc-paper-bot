# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 457 windows, 12538 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1067 | 51.3 | 50.0 | $-193.64 | -1.8% | $806.36 | -0.6 | done | can't tell from luck |
| value_ev10 | 586 | 38.9 | 40.1 | $-377.06 | -6.4% | $622.94 | -1.3 | done | can't tell from luck |
| trend_filter | 729 | 50.1 | 50.7 | $-385.98 | -5.3% | $614.02 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1266 | 49.8 | 50.0 | $-493.58 | -3.9% | $506.42 | -1.4 | done | can't tell from luck |
| value_ev5 | 870 | 40.9 | 41.9 | $-511.74 | -5.9% | $488.26 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1266 | 50.2 | 51.7 | $-904.61 | -7.1% | $95.39 | -2.7 | done | losing for real |
| coinflip | 1820 | 49.8 | 50.8 | $-1049.02 | -5.8% | $-49.02 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1067 | 48.7 | 51.7 | $-1074.85 | -10.1% | $-74.85 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1820 | 49.6 | 51.5 | $-1332.53 | -7.3% | $-332.53 | -3.2 | done | losing for real |
| always_up | 1820 | 46.2 | 50.6 | $-2274.70 | -12.5% | $-1274.70 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2834 | 47.4 | 49.3 | $-2337.78 |
| ETH | 3146 | 48.0 | 48.9 | $-2042.20 |
| SOL | 3264 | 47.7 | 49.3 | $-2507.81 |
| XRP | 3294 | 48.5 | 49.2 | $-1862.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
