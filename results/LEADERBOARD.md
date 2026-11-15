# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 421 windows, 11591 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 993 | 50.7 | 50.0 | $-294.34 | -3.0% | $705.66 | -0.9 | done | can't tell from luck |
| value_ev10 | 538 | 39.6 | 40.4 | $-301.49 | -5.6% | $698.51 | -1.1 | done | can't tell from luck |
| value_ev5 | 811 | 41.6 | 42.1 | $-418.73 | -5.2% | $581.27 | -1.3 | done | can't tell from luck |
| trend_filter | 664 | 49.4 | 50.7 | $-442.59 | -6.7% | $557.41 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1173 | 49.1 | 50.0 | $-626.62 | -5.3% | $373.38 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1173 | 50.9 | 51.8 | $-689.37 | -5.9% | $310.63 | -2.1 | done | losing for real |
| coinflip | 1679 | 50.4 | 51.0 | $-795.54 | -4.7% | $204.46 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 993 | 49.3 | 51.8 | $-878.65 | -8.8% | $121.35 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1679 | 49.4 | 51.6 | $-1300.83 | -7.7% | $-300.83 | -3.3 | done | losing for real |
| always_up | 1679 | 45.9 | 50.7 | $-2161.09 | -12.9% | $-1161.09 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2619 | 47.7 | 49.4 | $-1887.73 |
| ETH | 2914 | 47.9 | 49.0 | $-1864.97 |
| SOL | 3006 | 47.6 | 49.5 | $-2559.68 |
| XRP | 3052 | 48.7 | 49.3 | $-1753.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
