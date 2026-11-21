# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 974 windows, 27041 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2762 | 51.3 | 50.5 | $-725.75 | -2.6% | $274.25 | -1.4 | done | can't tell from luck |
| value_ev10 | 1234 | 37.9 | 39.1 | $-748.71 | -6.1% | $251.29 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2313 | 50.2 | 49.7 | $-883.30 | -3.8% | $116.70 | -1.8 | done | can't tell from luck |
| value_ev5 | 1871 | 39.9 | 41.0 | $-1087.45 | -5.8% | $-87.45 | -2.1 | done | losing for real |
| trend_filter | 1620 | 49.8 | 50.9 | $-1140.22 | -7.0% | $-140.22 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2313 | 49.8 | 50.9 | $-1655.25 | -7.2% | $-655.25 | -3.5 | done | losing for real |
| coinflip | 3890 | 50.1 | 50.3 | $-1828.03 | -4.7% | $-828.03 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2762 | 48.7 | 50.3 | $-1972.56 | -7.1% | $-972.56 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3890 | 50.7 | 51.5 | $-2139.46 | -5.5% | $-1139.46 | -3.5 | done | losing for real |
| always_up | 3890 | 46.8 | 49.6 | $-3901.49 | -10.0% | $-2901.49 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6165 | 48.2 | 49.1 | $-3533.16 |
| ETH | 6717 | 48.0 | 48.5 | $-4347.56 |
| SOL | 7067 | 48.1 | 48.6 | $-4045.54 |
| XRP | 7092 | 48.1 | 48.4 | $-4375.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
