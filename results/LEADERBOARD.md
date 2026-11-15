# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 419 windows, 11522 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 989 | 50.9 | 50.1 | $-254.34 | -2.6% | $745.66 | -0.8 | done | can't tell from luck |
| value_ev10 | 536 | 39.7 | 40.4 | $-281.49 | -5.3% | $718.51 | -1.0 | done | can't tell from luck |
| value_ev5 | 807 | 41.8 | 42.1 | $-378.73 | -4.7% | $621.27 | -1.2 | done | can't tell from luck |
| trend_filter | 660 | 49.7 | 50.8 | $-402.59 | -6.1% | $597.41 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1164 | 49.2 | 50.0 | $-589.17 | -5.1% | $410.83 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1164 | 50.8 | 51.8 | $-708.07 | -6.1% | $291.93 | -2.2 | done | losing for real |
| coinflip | 1668 | 50.4 | 50.9 | $-790.09 | -4.7% | $209.91 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 989 | 49.1 | 51.8 | $-905.63 | -9.2% | $94.37 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1668 | 49.4 | 51.6 | $-1281.90 | -7.7% | $-281.90 | -3.3 | done | losing for real |
| always_up | 1668 | 45.7 | 50.7 | $-2199.28 | -13.2% | $-1199.28 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2608 | 47.7 | 49.4 | $-1894.76 |
| ETH | 2899 | 47.9 | 49.0 | $-1864.32 |
| SOL | 2984 | 47.6 | 49.5 | $-2509.35 |
| XRP | 3031 | 48.8 | 49.3 | $-1679.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
