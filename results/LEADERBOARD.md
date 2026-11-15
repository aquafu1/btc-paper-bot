# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 439 windows, 12092 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1034 | 51.2 | 50.0 | $-193.62 | -1.9% | $806.38 | -0.6 | done | can't tell from luck |
| trend_filter | 700 | 50.3 | 50.6 | $-336.43 | -4.8% | $663.57 | -1.3 | done | can't tell from luck |
| value_ev10 | 569 | 38.7 | 40.2 | $-423.63 | -7.4% | $576.37 | -1.5 | done | can't tell from luck |
| value_ev5 | 847 | 41.0 | 41.9 | $-519.11 | -6.1% | $480.89 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1222 | 49.6 | 50.0 | $-544.64 | -4.5% | $455.36 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1222 | 50.4 | 51.7 | $-837.47 | -6.9% | $162.53 | -2.5 | done | losing for real |
| coinflip | 1748 | 50.3 | 50.9 | $-842.03 | -4.8% | $157.97 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1034 | 48.8 | 51.8 | $-1035.07 | -10.0% | $-35.07 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1748 | 49.8 | 51.6 | $-1211.84 | -6.9% | $-211.84 | -3.0 | done | losing for real |
| always_up | 1748 | 45.9 | 50.5 | $-2245.42 | -12.8% | $-1245.42 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2733 | 47.5 | 49.3 | $-2137.31 |
| ETH | 3036 | 48.0 | 48.8 | $-1910.78 |
| SOL | 3139 | 47.8 | 49.3 | $-2491.29 |
| XRP | 3184 | 48.6 | 49.2 | $-1828.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
