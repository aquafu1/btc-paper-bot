# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 245 windows, 6398 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 630 | 56.3 | 52.3 | $+247.29 | +3.9% | $1247.29 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 505 | 54.5 | 52.2 | $+24.01 | +0.5% | $1024.01 | +0.1 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 10:45 AM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 335 | 44.8 | 50.3 | $-497.96 | -14.9% | $502.04 | -2.8 | done | losing for real |
| value_ev5 | 453 | 39.1 | 42.5 | $-536.70 | -11.8% | $463.30 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 505 | 45.5 | 49.9 | $-651.14 | -12.9% | $348.86 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 972 | 49.7 | 51.5 | $-742.51 | -7.6% | $257.49 | -2.5 | done | losing for real |
| coinflip | 972 | 49.2 | 50.9 | $-749.14 | -7.7% | $250.86 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 630 | 43.7 | 49.9 | $-1013.17 | -16.1% | $-13.17 | -4.1 | done | losing for real |
| always_up | 972 | 47.3 | 50.5 | $-1033.69 | -10.6% | $-33.69 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1429 | 46.3 | 49.8 | $-1541.24 |
| ETH | 1594 | 46.5 | 49.1 | $-1684.34 |
| SOL | 1654 | 48.1 | 49.4 | $-1323.40 |
| XRP | 1721 | 48.8 | 49.2 | $-917.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
