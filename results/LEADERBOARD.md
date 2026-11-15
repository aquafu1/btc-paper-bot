# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 413 windows, 11327 settled trades, 80 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 204 | 35.8 | 36.5 | $-106.95 | -5.2% | $893.05 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 968 | 51.0 | 50.0 | $-203.56 | -2.1% | $796.44 | -0.7 | done | can't tell from luck |
| value_ev10 | 530 | 40.2 | 40.5 | $-221.49 | -4.2% | $778.51 | -0.8 | done | can't tell from luck |
| trend_filter | 645 | 50.2 | 50.7 | $-308.26 | -4.8% | $691.74 | -1.2 | done | can't tell from luck |
| value_ev5 | 798 | 42.1 | 42.2 | $-310.32 | -3.9% | $689.68 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1141 | 49.3 | 49.9 | $-543.83 | -4.8% | $456.17 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1141 | 50.7 | 51.9 | $-708.57 | -6.2% | $291.43 | -2.2 | done | losing for real |
| coinflip | 1644 | 50.2 | 50.9 | $-805.79 | -4.9% | $194.21 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 968 | 49.0 | 51.9 | $-908.50 | -9.4% | $91.50 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1644 | 49.8 | 51.6 | $-1116.87 | -6.8% | $-116.87 | -2.9 | done | losing for real |
| always_up | 1644 | 45.9 | 50.6 | $-2093.73 | -12.7% | $-1093.73 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2561 | 47.8 | 49.5 | $-1773.20 |
| ETH | 2847 | 48.1 | 49.0 | $-1689.48 |
| SOL | 2931 | 47.9 | 49.5 | $-2277.93 |
| XRP | 2988 | 48.8 | 49.3 | $-1587.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
