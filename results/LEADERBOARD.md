# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 469 windows, 12876 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1091 | 50.8 | 49.9 | $-281.71 | -2.6% | $718.29 | -0.9 | done | can't tell from luck |
| value_ev10 | 608 | 39.1 | 40.1 | $-352.22 | -5.8% | $647.78 | -1.2 | done | can't tell from luck |
| trend_filter | 747 | 49.7 | 50.8 | $-453.49 | -6.1% | $546.51 | -1.7 | done | can't tell from luck |
| value_ev5 | 900 | 41.1 | 41.8 | $-483.85 | -5.4% | $516.15 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1296 | 49.8 | 50.0 | $-498.91 | -3.8% | $501.09 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1296 | 50.2 | 51.5 | $-863.06 | -6.7% | $136.94 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1091 | 49.2 | 51.6 | $-955.85 | -8.8% | $44.15 | -3.0 | done | losing for real |
| coinflip | 1870 | 49.8 | 50.8 | $-1055.84 | -5.6% | $-55.84 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1870 | 49.8 | 51.7 | $-1326.97 | -7.1% | $-326.97 | -3.2 | done | losing for real |
| always_up | 1870 | 46.5 | 50.4 | $-2140.34 | -11.4% | $-1140.34 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2905 | 47.6 | 49.3 | $-2226.85 |
| ETH | 3234 | 48.1 | 48.8 | $-2134.53 |
| SOL | 3357 | 47.7 | 49.3 | $-2487.31 |
| XRP | 3380 | 48.6 | 49.1 | $-1699.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
