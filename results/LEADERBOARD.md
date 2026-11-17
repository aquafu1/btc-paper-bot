# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 635 windows, 17548 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1484 | 51.0 | 49.5 | $-212.30 | -1.4% | $787.70 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1015 | 50.2 | 50.8 | $-546.72 | -5.4% | $453.28 | -1.8 | done | can't tell from luck |
| value_ev10 | 806 | 38.5 | 39.5 | $-549.42 | -6.8% | $450.58 | -1.6 | done | can't tell from luck |
| value_ev5 | 1223 | 40.7 | 41.4 | $-698.56 | -5.7% | $301.44 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1805 | 51.1 | 51.1 | $-754.53 | -4.2% | $245.47 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1805 | 48.9 | 50.0 | $-1073.34 | -5.9% | $-73.34 | -2.5 | done | losing for real |
| coinflip | 2532 | 50.1 | 50.5 | $-1179.52 | -4.7% | $-179.52 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1484 | 49.0 | 51.5 | $-1377.85 | -9.3% | $-377.85 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2532 | 50.6 | 51.7 | $-1451.45 | -5.7% | $-451.45 | -3.0 | done | losing for real |
| always_up | 2532 | 47.4 | 49.7 | $-2213.12 | -8.7% | $-1213.12 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3985 | 48.3 | 49.2 | $-2432.51 |
| ETH | 4392 | 48.2 | 48.6 | $-2608.53 |
| SOL | 4555 | 48.0 | 48.8 | $-2974.69 |
| XRP | 4616 | 48.5 | 48.6 | $-2315.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
