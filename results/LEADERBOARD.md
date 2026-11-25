# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1425 windows, 36467 settled trades, 436 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 734 | 34.6 | 35.3 | $-505.63 | -6.9% | $494.37 | -1.4 | done | can't tell from luck |
| value_ev10 | 1770 | 38.8 | 39.1 | $-797.88 | -4.5% | $202.12 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3641 | 50.8 | 50.1 | $-1029.80 | -2.8% | $-29.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 2671 | 40.6 | 41.1 | $-1272.32 | -4.8% | $-272.32 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3060 | 49.2 | 49.3 | $-1508.56 | -4.9% | $-508.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3060 | 50.8 | 51.0 | $-1559.38 | -5.1% | $-559.38 | -2.9 | done | losing for real |
| trend_filter | 2164 | 48.6 | 50.4 | $-1889.41 | -8.7% | $-889.41 | -4.2 | done | losing for real |
| coinflip | 5242 | 50.1 | 50.0 | $-2209.80 | -4.2% | $-1209.80 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3641 | 49.2 | 50.2 | $-2239.74 | -6.2% | $-1239.74 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5242 | 50.2 | 51.4 | $-3246.64 | -6.2% | $-2246.64 | -4.6 | done | losing for real |
| always_up | 5242 | 47.9 | 49.3 | $-3671.88 | -7.0% | $-2671.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9232 | 48.1 | 48.7 | $-5000.91 |
| ETH | 9925 | 48.1 | 48.0 | $-5345.90 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
