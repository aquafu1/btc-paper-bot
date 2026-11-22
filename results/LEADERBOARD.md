# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1068 windows, 29559 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 553 | 34.4 | 35.1 | $-343.30 | -6.2% | $656.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2995 | 51.4 | 50.4 | $-698.35 | -2.3% | $301.65 | -1.3 | done | can't tell from luck |
| value_ev10 | 1367 | 37.6 | 39.2 | $-980.20 | -7.2% | $19.80 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2511 | 49.7 | 49.6 | $-1144.93 | -4.6% | $-144.93 | -2.3 | done | losing for real |
| trend_filter | 1758 | 49.5 | 50.7 | $-1268.73 | -7.2% | $-268.73 | -3.1 | done | losing for real |
| value_ev5 | 2074 | 39.6 | 41.0 | $-1371.78 | -6.6% | $-371.78 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2511 | 50.3 | 51.0 | $-1594.74 | -6.4% | $-594.74 | -3.3 | done | losing for real |
| coinflip | 4265 | 50.5 | 50.3 | $-1699.15 | -4.0% | $-699.15 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4265 | 51.0 | 51.5 | $-2067.78 | -4.8% | $-1067.78 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2995 | 48.6 | 50.3 | $-2185.95 | -7.3% | $-1185.95 | -4.0 | done | losing for real |
| always_up | 4265 | 47.3 | 49.4 | $-3719.51 | -8.7% | $-2719.51 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6748 | 48.4 | 49.0 | $-3419.56 |
| ETH | 7312 | 48.1 | 48.5 | $-4659.59 |
| SOL | 7710 | 48.1 | 48.5 | $-4475.61 |
| XRP | 7789 | 48.3 | 48.3 | $-4519.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
