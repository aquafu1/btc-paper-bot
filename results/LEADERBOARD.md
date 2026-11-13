# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 231 windows, 6046 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 593 | 56.0 | 52.6 | $+179.71 | +3.0% | $1179.71 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 475 | 53.7 | 52.4 | $-50.50 | -1.1% | $949.50 | -0.2 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 5:30 AM | too few trades (113/200) |
| value_ev10 | 298 | 37.6 | 40.7 | $-336.23 | -11.3% | $663.77 | -1.7 | done | can't tell from luck |
| trend_filter | 318 | 45.6 | 50.1 | $-406.22 | -12.8% | $593.78 | -2.3 | done | losing for real |
| value_ev5 | 433 | 39.5 | 42.5 | $-463.79 | -10.7% | $536.21 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 475 | 46.3 | 49.8 | $-518.08 | -10.9% | $481.92 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 916 | 50.2 | 51.5 | $-572.05 | -6.2% | $427.95 | -2.0 | done | can't tell from luck |
| coinflip | 916 | 49.8 | 51.0 | $-574.90 | -6.3% | $425.10 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 593 | 44.0 | 49.6 | $-874.85 | -14.8% | $125.15 | -3.6 | done | losing for real |
| always_up | 916 | 47.3 | 50.3 | $-932.18 | -10.2% | $67.82 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1358 | 46.5 | 49.6 | $-1360.80 |
| ETH | 1502 | 46.9 | 49.0 | $-1410.06 |
| SOL | 1560 | 48.0 | 49.3 | $-1260.08 |
| XRP | 1626 | 49.2 | 49.1 | $-628.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
