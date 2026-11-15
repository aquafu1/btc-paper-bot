# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 413 windows, 11369 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 207 | 35.3 | 36.3 | $-136.95 | -6.6% | $863.05 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 972 | 51.2 | 50.1 | $-187.89 | -1.9% | $812.11 | -0.6 | done | can't tell from luck |
| value_ev10 | 533 | 40.0 | 40.4 | $-251.49 | -4.7% | $748.51 | -0.9 | done | can't tell from luck |
| trend_filter | 649 | 50.5 | 50.8 | $-292.59 | -4.5% | $707.41 | -1.2 | done | can't tell from luck |
| value_ev5 | 802 | 41.9 | 42.1 | $-350.32 | -4.4% | $649.68 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1145 | 49.4 | 49.9 | $-528.16 | -4.6% | $471.84 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1145 | 50.6 | 51.8 | $-748.57 | -6.5% | $251.43 | -2.3 | done | losing for real |
| coinflip | 1648 | 50.2 | 50.9 | $-819.87 | -5.0% | $180.13 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 972 | 48.8 | 51.7 | $-948.50 | -9.8% | $51.50 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1648 | 49.9 | 51.6 | $-1101.20 | -6.7% | $-101.20 | -2.8 | done | losing for real |
| always_up | 1648 | 46.1 | 50.7 | $-2078.07 | -12.6% | $-1078.07 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2572 | 47.8 | 49.4 | $-1810.95 |
| ETH | 2858 | 48.1 | 49.0 | $-1716.23 |
| SOL | 2942 | 47.9 | 49.5 | $-2317.67 |
| XRP | 2997 | 48.8 | 49.3 | $-1598.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
