# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1202 windows, 33173 settled trades, 112 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 647 | 34.6 | 35.3 | $-418.79 | -6.5% | $581.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1584 | 38.6 | 39.2 | $-810.46 | -5.1% | $189.54 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3324 | 50.8 | 50.3 | $-1097.65 | -3.3% | $-97.65 | -1.9 | done | can't tell from luck |
| value_ev5 | 2395 | 40.4 | 41.1 | $-1249.26 | -5.2% | $-249.26 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2778 | 49.5 | 49.4 | $-1267.33 | -4.6% | $-267.33 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2778 | 50.5 | 51.1 | $-1675.99 | -6.0% | $-675.99 | -3.3 | done | losing for real |
| trend_filter | 1958 | 48.7 | 50.5 | $-1681.91 | -8.6% | $-681.91 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3324 | 49.2 | 50.2 | $-2042.20 | -6.1% | $-1042.20 | -3.6 | done | losing for real |
| coinflip | 4795 | 50.1 | 50.1 | $-2125.92 | -4.4% | $-1125.92 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4795 | 50.2 | 51.4 | $-2960.64 | -6.2% | $-1960.64 | -4.4 | done | losing for real |
| always_up | 4795 | 47.9 | 49.3 | $-3465.05 | -7.2% | $-2465.05 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7627 | 48.1 | 48.9 | $-4260.64 |
| ETH | 8236 | 48.1 | 48.4 | $-4950.33 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
