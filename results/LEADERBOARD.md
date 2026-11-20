# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 867 windows, 23887 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 448 | 35.0 | 34.9 | $-178.27 | -4.0% | $821.73 | -0.6 | done | can't tell from luck |
| value_ev10 | 1096 | 38.2 | 39.1 | $-627.29 | -5.7% | $372.71 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2016 | 50.2 | 49.7 | $-735.96 | -3.7% | $264.04 | -1.6 | done | can't tell from luck |
| trend_filter | 1398 | 50.3 | 50.9 | $-862.42 | -6.2% | $137.58 | -2.4 | done | losing for real |
| value_ev5 | 1657 | 40.0 | 41.0 | $-979.69 | -5.9% | $20.31 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2438 | 50.5 | 50.5 | $-1010.67 | -4.1% | $-10.67 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2438 | 49.5 | 50.3 | $-1344.92 | -5.5% | $-344.92 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2016 | 49.8 | 51.1 | $-1504.58 | -7.5% | $-504.58 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3460 | 51.3 | 51.7 | $-1546.97 | -4.5% | $-546.97 | -2.7 | done | losing for real |
| coinflip | 3460 | 50.1 | 50.3 | $-1551.64 | -4.5% | $-551.64 | -2.7 | done | losing for real |
| always_up | 3460 | 46.8 | 49.6 | $-3404.97 | -9.8% | $-2404.97 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5447 | 48.3 | 49.0 | $-2952.98 |
| ETH | 5942 | 48.1 | 48.5 | $-3867.73 |
| SOL | 6233 | 48.3 | 48.6 | $-3492.31 |
| XRP | 6265 | 48.3 | 48.5 | $-3434.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
