# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1371 windows, 35670 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 709 | 34.1 | 35.3 | $-569.64 | -8.0% | $430.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1728 | 38.7 | 39.2 | $-818.68 | -4.7% | $181.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3565 | 50.9 | 50.1 | $-1013.45 | -2.8% | $-13.45 | -1.7 | done | can't tell from luck |
| value_ev5 | 2604 | 40.4 | 41.1 | $-1310.78 | -5.0% | $-310.78 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2990 | 49.3 | 49.4 | $-1495.42 | -5.0% | $-495.42 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2990 | 50.7 | 50.9 | $-1516.32 | -5.1% | $-516.32 | -2.8 | done | losing for real |
| trend_filter | 2120 | 48.5 | 50.4 | $-1873.46 | -8.8% | $-873.46 | -4.2 | done | losing for real |
| coinflip | 5133 | 50.0 | 50.0 | $-2198.93 | -4.3% | $-1198.93 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3565 | 49.1 | 50.2 | $-2215.98 | -6.2% | $-1215.98 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5133 | 50.1 | 51.3 | $-3208.42 | -6.3% | $-2208.42 | -4.6 | done | losing for real |
| always_up | 5133 | 47.9 | 49.3 | $-3701.92 | -7.2% | $-2701.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8843 | 47.9 | 48.8 | $-5193.99 |
| ETH | 9517 | 48.1 | 48.1 | $-5144.77 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
