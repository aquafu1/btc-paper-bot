# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1465 windows, 36991 settled trades, 364 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1803 | 38.5 | 39.2 | $-960.25 | -5.3% | $39.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3687 | 50.9 | 50.0 | $-961.47 | -2.6% | $38.53 | -1.6 | done | can't tell from luck |
| value_ev5 | 2715 | 40.4 | 41.1 | $-1443.06 | -5.3% | $-443.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3097 | 49.2 | 49.2 | $-1542.10 | -5.0% | $-542.10 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3097 | 50.8 | 51.0 | $-1583.76 | -5.1% | $-583.76 | -2.9 | done | losing for real |
| trend_filter | 2197 | 48.7 | 50.3 | $-1876.06 | -8.5% | $-876.06 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3687 | 49.1 | 50.2 | $-2326.77 | -6.3% | $-1326.77 | -3.9 | done | losing for real |
| coinflip | 5320 | 49.9 | 50.0 | $-2391.61 | -4.5% | $-1391.61 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5320 | 50.2 | 51.3 | $-3313.28 | -6.2% | $-2313.28 | -4.7 | done | losing for real |
| always_up | 5320 | 48.0 | 49.2 | $-3597.80 | -6.8% | $-2597.80 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9489 | 48.0 | 48.7 | $-5265.78 |
| ETH | 10192 | 47.9 | 48.0 | $-5759.62 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
