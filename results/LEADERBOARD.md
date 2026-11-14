# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 310 windows, 8281 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 819 | 53.4 | 51.8 | $-104.75 | -1.3% | $895.25 | -0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 674 | 52.8 | 51.7 | $-141.55 | -2.1% | $858.45 | -0.6 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 1:15 AM | too few trades (155/200) |
| value_ev10 | 398 | 37.9 | 40.5 | $-416.52 | -10.5% | $583.48 | -1.8 | done | can't tell from luck |
| trend_filter | 455 | 45.5 | 50.4 | $-644.55 | -14.2% | $355.45 | -3.1 | done | losing for real |
| value_ev5 | 591 | 39.3 | 42.2 | $-662.64 | -11.2% | $337.36 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 674 | 47.2 | 50.0 | $-698.29 | -10.4% | $301.71 | -2.8 | done | losing for real |
| coinflip | 1232 | 49.9 | 50.9 | $-761.29 | -6.2% | $238.71 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 819 | 46.6 | 50.0 | $-882.60 | -10.8% | $117.40 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1232 | 48.8 | 51.4 | $-1130.80 | -9.2% | $-130.80 | -3.4 | done | losing for real |
| always_up | 1232 | 47.4 | 50.4 | $-1240.35 | -10.1% | $-240.35 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1861 | 46.5 | 49.3 | $-1853.20 |
| ETH | 2073 | 47.0 | 48.8 | $-1967.83 |
| SOL | 2155 | 47.9 | 49.4 | $-1780.46 |
| XRP | 2192 | 48.6 | 49.1 | $-1261.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
