# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 565 windows, 15685 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1332 | 51.2 | 49.7 | $-274.55 | -2.1% | $725.45 | -0.8 | done | can't tell from luck |
| value_ev20 | 308 | 33.1 | 35.2 | $-345.22 | -11.2% | $654.78 | -1.5 | done | can't tell from luck |
| trend_filter | 910 | 50.3 | 51.1 | $-547.42 | -6.0% | $452.58 | -1.9 | done | can't tell from luck |
| value_ev10 | 745 | 37.4 | 39.4 | $-715.71 | -9.6% | $284.29 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1592 | 50.8 | 51.0 | $-824.89 | -5.2% | $175.11 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1592 | 49.2 | 49.8 | $-904.74 | -5.7% | $95.26 | -2.3 | done | losing for real |
| value_ev5 | 1106 | 39.6 | 41.2 | $-910.83 | -8.2% | $89.17 | -2.4 | done | losing for real |
| coinflip | 2256 | 49.8 | 50.4 | $-1246.13 | -5.5% | $-246.13 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1332 | 48.8 | 51.2 | $-1292.92 | -9.7% | $-292.92 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2256 | 50.2 | 51.9 | $-1628.69 | -7.2% | $-628.69 | -3.6 | done | losing for real |
| always_up | 2256 | 47.3 | 49.8 | $-2171.48 | -9.6% | $-1171.48 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3546 | 47.6 | 49.2 | $-2759.03 |
| ETH | 3911 | 47.9 | 48.6 | $-2763.53 |
| SOL | 4093 | 47.8 | 48.7 | $-3059.41 |
| XRP | 4135 | 48.5 | 48.6 | $-2280.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
