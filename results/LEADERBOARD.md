# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1616 windows, 38941 settled trades, 353 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 823 | 34.1 | 35.2 | $-665.00 | -8.1% | $335.00 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3840 | 50.9 | 50.0 | $-1007.14 | -2.6% | $-7.14 | -1.6 | done | can't tell from luck |
| value_ev10 | 1947 | 38.3 | 39.0 | $-1108.33 | -5.7% | $-108.33 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3214 | 51.1 | 50.9 | $-1472.89 | -4.6% | $-472.89 | -2.7 | done | losing for real |
| value_ev5 | 2914 | 40.4 | 41.0 | $-1547.71 | -5.3% | $-547.71 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3214 | 48.9 | 49.2 | $-1750.52 | -5.4% | $-750.52 | -3.1 | done | losing for real |
| trend_filter | 2283 | 48.5 | 50.4 | $-2033.23 | -8.9% | $-1033.23 | -4.4 | done | losing for real |
| coinflip | 5622 | 50.1 | 49.9 | $-2320.06 | -4.1% | $-1320.06 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3840 | 49.1 | 50.2 | $-2371.04 | -6.2% | $-1371.04 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5622 | 50.2 | 51.3 | $-3486.21 | -6.2% | $-2486.21 | -4.8 | done | losing for real |
| always_up | 5622 | 48.2 | 49.1 | $-3640.46 | -6.5% | $-2640.46 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10391 | 47.9 | 48.6 | $-5902.32 |
| ETH | 11240 | 48.0 | 47.7 | $-5916.03 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
