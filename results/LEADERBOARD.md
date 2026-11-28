# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1642 windows, 39273 settled trades, 366 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 835 | 34.5 | 35.2 | $-593.68 | -7.1% | $406.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3864 | 50.8 | 49.9 | $-1043.86 | -2.7% | $-43.86 | -1.7 | done | can't tell from luck |
| value_ev10 | 1973 | 38.4 | 39.0 | $-1072.71 | -5.4% | $-72.71 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3233 | 51.0 | 50.9 | $-1479.17 | -4.6% | $-479.17 | -2.7 | done | losing for real |
| value_ev5 | 2947 | 40.4 | 41.0 | $-1524.55 | -5.2% | $-524.55 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3233 | 49.0 | 49.2 | $-1760.63 | -5.4% | $-760.63 | -3.1 | done | losing for real |
| trend_filter | 2302 | 48.4 | 50.4 | $-2068.35 | -9.0% | $-1068.35 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3864 | 49.2 | 50.2 | $-2338.65 | -6.1% | $-1338.65 | -3.8 | done | losing for real |
| coinflip | 5674 | 49.9 | 49.9 | $-2503.70 | -4.4% | $-1503.70 | -3.3 | done | losing for real |
| always_up | 5674 | 48.3 | 49.0 | $-3516.05 | -6.2% | $-2516.05 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5674 | 50.2 | 51.3 | $-3527.43 | -6.2% | $-2527.43 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10543 | 48.0 | 48.6 | $-5857.92 |
| ETH | 11420 | 47.9 | 47.6 | $-5986.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
