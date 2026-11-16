# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 524 windows, 14460 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1233 | 51.3 | 49.8 | $-151.76 | -1.2% | $848.24 | -0.4 | done | can't tell from luck |
| value_ev20 | 270 | 34.8 | 35.6 | $-172.96 | -6.4% | $827.04 | -0.8 | done | can't tell from luck |
| value_ev10 | 672 | 38.1 | 39.7 | $-515.03 | -7.7% | $484.97 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1466 | 49.9 | 49.7 | $-533.74 | -3.6% | $466.26 | -1.4 | done | can't tell from luck |
| trend_filter | 851 | 49.5 | 50.7 | $-551.72 | -6.5% | $448.28 | -1.9 | done | can't tell from luck |
| value_ev5 | 1002 | 40.1 | 41.5 | $-688.64 | -6.9% | $311.36 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1466 | 50.1 | 51.5 | $-1009.64 | -6.9% | $-9.64 | -2.7 | done | losing for real |
| coinflip | 2089 | 50.0 | 50.7 | $-1114.72 | -5.3% | $-114.72 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1233 | 48.7 | 51.4 | $-1148.92 | -9.3% | $-148.92 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2089 | 49.4 | 51.6 | $-1651.30 | -7.9% | $-651.30 | -3.7 | done | losing for real |
| always_up | 2089 | 46.4 | 50.1 | $-2389.83 | -11.4% | $-1389.83 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3281 | 47.4 | 49.2 | $-2604.64 |
| ETH | 3604 | 47.9 | 48.7 | $-2374.74 |
| SOL | 3768 | 47.6 | 49.0 | $-2724.90 |
| XRP | 3807 | 48.3 | 48.8 | $-2223.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
