# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 522 windows, 14391 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1225 | 51.3 | 49.9 | $-171.86 | -1.4% | $828.14 | -0.5 | done | can't tell from luck |
| value_ev20 | 269 | 34.6 | 35.6 | $-184.33 | -6.9% | $815.67 | -0.9 | done | can't tell from luck |
| value_ev10 | 671 | 38.0 | 39.7 | $-526.39 | -7.8% | $473.61 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1458 | 49.9 | 49.7 | $-532.48 | -3.7% | $467.52 | -1.4 | done | can't tell from luck |
| trend_filter | 844 | 49.5 | 50.7 | $-560.45 | -6.6% | $439.55 | -2.0 | done | can't tell from luck |
| value_ev5 | 998 | 40.0 | 41.5 | $-725.35 | -7.3% | $274.65 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1458 | 50.1 | 51.5 | $-1039.76 | -7.1% | $-39.76 | -2.8 | done | losing for real |
| coinflip | 2081 | 50.0 | 50.7 | $-1140.94 | -5.5% | $-140.94 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1225 | 48.7 | 51.4 | $-1157.68 | -9.5% | $-157.68 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2081 | 49.4 | 51.6 | $-1650.03 | -7.9% | $-650.03 | -3.8 | done | losing for real |
| always_up | 2081 | 46.4 | 50.1 | $-2398.59 | -11.5% | $-1398.59 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3263 | 47.4 | 49.2 | $-2587.22 |
| ETH | 3587 | 47.9 | 48.7 | $-2441.22 |
| SOL | 3751 | 47.6 | 49.0 | $-2812.78 |
| XRP | 3790 | 48.3 | 48.8 | $-2246.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
