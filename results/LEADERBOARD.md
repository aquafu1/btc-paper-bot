# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 428 windows, 11771 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 213 | 34.7 | 36.2 | $-164.42 | -7.7% | $835.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1005 | 50.6 | 50.0 | $-294.98 | -2.9% | $705.02 | -0.9 | done | can't tell from luck |
| value_ev10 | 550 | 39.5 | 40.3 | $-315.64 | -5.7% | $684.36 | -1.1 | done | can't tell from luck |
| trend_filter | 674 | 49.7 | 50.7 | $-407.52 | -6.0% | $592.48 | -1.6 | done | can't tell from luck |
| value_ev5 | 826 | 41.5 | 42.1 | $-415.67 | -5.0% | $584.33 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1193 | 49.2 | 50.0 | $-615.03 | -5.2% | $384.97 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1193 | 50.8 | 51.7 | $-707.88 | -5.9% | $292.12 | -2.2 | done | losing for real |
| coinflip | 1704 | 50.5 | 50.9 | $-774.22 | -4.5% | $225.78 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1005 | 49.4 | 51.8 | $-898.23 | -8.9% | $101.77 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1704 | 49.6 | 51.6 | $-1258.43 | -7.4% | $-258.43 | -3.2 | done | losing for real |
| always_up | 1704 | 46.2 | 50.6 | $-2077.98 | -12.2% | $-1077.98 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2664 | 47.6 | 49.4 | $-2048.14 |
| ETH | 2952 | 48.0 | 48.9 | $-1856.43 |
| SOL | 3054 | 47.8 | 49.4 | $-2361.44 |
| XRP | 3101 | 48.8 | 49.3 | $-1663.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
