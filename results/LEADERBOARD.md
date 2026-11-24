# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1283 windows, 34390 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 676 | 33.9 | 35.3 | $-570.36 | -8.4% | $429.64 | -1.7 | done | can't tell from luck |
| value_ev10 | 1652 | 38.5 | 39.2 | $-880.65 | -5.3% | $119.35 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3449 | 50.7 | 50.2 | $-1164.67 | -3.4% | $-164.67 | -2.0 | done | can't tell from luck |
| value_ev5 | 2496 | 40.3 | 41.1 | $-1342.01 | -5.4% | $-342.01 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2883 | 49.5 | 49.4 | $-1369.08 | -4.7% | $-369.08 | -2.5 | done | losing for real |
| trend_filter | 2034 | 49.0 | 50.5 | $-1633.73 | -8.0% | $-633.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2883 | 50.5 | 51.0 | $-1643.64 | -5.7% | $-643.64 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3449 | 49.3 | 50.2 | $-2098.38 | -6.1% | $-1098.38 | -3.6 | done | losing for real |
| coinflip | 4956 | 49.9 | 50.1 | $-2330.71 | -4.7% | $-1330.71 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4956 | 50.5 | 51.4 | $-2778.27 | -5.6% | $-1778.27 | -4.1 | done | losing for real |
| always_up | 4956 | 47.8 | 49.3 | $-3669.85 | -7.4% | $-2669.85 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8212 | 48.0 | 48.8 | $-4963.01 |
| ETH | 8868 | 48.2 | 48.2 | $-4934.12 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
