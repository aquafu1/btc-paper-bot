# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1668 windows, 39590 settled trades, 349 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 845 | 34.3 | 35.2 | $-644.92 | -7.6% | $355.08 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3888 | 50.8 | 49.9 | $-1001.90 | -2.6% | $-1.90 | -1.6 | done | can't tell from luck |
| value_ev10 | 1997 | 38.4 | 39.0 | $-1122.13 | -5.6% | $-122.13 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3246 | 51.1 | 50.9 | $-1432.15 | -4.4% | $-432.15 | -2.6 | done | losing for real |
| value_ev5 | 2981 | 40.3 | 41.0 | $-1627.97 | -5.5% | $-627.97 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3246 | 48.9 | 49.3 | $-1821.06 | -5.6% | $-821.06 | -3.2 | done | losing for real |
| trend_filter | 2315 | 48.3 | 50.3 | $-2140.50 | -9.2% | $-1140.50 | -4.6 | done | losing for real |
| momentum_15m_0.10pct | 3888 | 49.2 | 50.2 | $-2379.80 | -6.1% | $-1379.80 | -3.8 | done | losing for real |
| coinflip | 5728 | 49.9 | 49.9 | $-2540.82 | -4.4% | $-1540.82 | -3.4 | done | losing for real |
| always_up | 5728 | 48.3 | 49.0 | $-3558.06 | -6.2% | $-2558.06 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5728 | 50.1 | 51.3 | $-3606.84 | -6.3% | $-2606.84 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10694 | 47.9 | 48.5 | $-6014.89 |
| ETH | 11586 | 47.8 | 47.6 | $-6277.05 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
