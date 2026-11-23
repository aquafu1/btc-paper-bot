# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1151 windows, 31792 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 613 | 34.6 | 35.2 | $-387.85 | -6.3% | $612.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1498 | 38.3 | 39.2 | $-891.80 | -6.0% | $108.20 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3193 | 50.9 | 50.4 | $-981.89 | -3.1% | $18.11 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2681 | 49.7 | 49.5 | $-1173.76 | -4.4% | $-173.76 | -2.3 | done | losing for real |
| value_ev5 | 2262 | 40.3 | 41.1 | $-1229.90 | -5.4% | $-229.90 | -2.2 | done | losing for real |
| trend_filter | 1883 | 48.9 | 50.5 | $-1532.30 | -8.1% | $-532.30 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2681 | 50.3 | 51.0 | $-1661.51 | -6.2% | $-661.51 | -3.3 | done | losing for real |
| coinflip | 4596 | 50.3 | 50.2 | $-1897.15 | -4.1% | $-897.15 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3193 | 49.1 | 50.2 | $-1980.32 | -6.2% | $-980.32 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4596 | 50.1 | 51.4 | $-2921.73 | -6.4% | $-1921.73 | -4.4 | done | losing for real |
| always_up | 4596 | 47.8 | 49.3 | $-3398.09 | -7.4% | $-2398.09 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7284 | 48.3 | 49.0 | $-3770.21 |
| ETH | 7878 | 48.1 | 48.4 | $-4644.25 |
| SOL | 8276 | 48.0 | 48.4 | $-4644.13 |
| XRP | 8354 | 48.1 | 48.2 | $-4997.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
