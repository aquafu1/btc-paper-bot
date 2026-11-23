# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1148 windows, 31715 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 612 | 34.5 | 35.3 | $-408.25 | -6.7% | $591.75 | -1.3 | done | can't tell from luck |
| value_ev10 | 1494 | 38.1 | 39.2 | $-952.76 | -6.4% | $47.24 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 3183 | 50.9 | 50.4 | $-1008.88 | -3.2% | $-8.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2677 | 49.6 | 49.5 | $-1186.98 | -4.4% | $-186.98 | -2.3 | done | losing for real |
| value_ev5 | 2255 | 40.1 | 41.1 | $-1313.85 | -5.8% | $-313.85 | -2.3 | done | losing for real |
| trend_filter | 1882 | 48.9 | 50.5 | $-1522.30 | -8.1% | $-522.30 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2677 | 50.4 | 51.1 | $-1650.58 | -6.2% | $-650.58 | -3.3 | done | losing for real |
| coinflip | 4584 | 50.2 | 50.2 | $-1922.48 | -4.2% | $-922.48 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 3183 | 49.1 | 50.2 | $-1951.48 | -6.1% | $-951.48 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4584 | 50.2 | 51.4 | $-2894.61 | -6.3% | $-1894.61 | -4.4 | done | losing for real |
| always_up | 4584 | 47.9 | 49.4 | $-3400.04 | -7.4% | $-2400.04 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7267 | 48.2 | 49.0 | $-3837.16 |
| ETH | 7858 | 48.1 | 48.4 | $-4667.10 |
| SOL | 8259 | 48.0 | 48.4 | $-4722.86 |
| XRP | 8331 | 48.1 | 48.2 | $-4985.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
