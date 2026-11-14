# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 288 windows, 7615 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 749 | 54.2 | 51.8 | $+19.24 | +0.3% | $1019.24 | +0.1 | done | can't tell from luck |
| value_ev20 | 142 | 35.9 | 36.4 | $-101.22 | -7.1% | $898.78 | -0.7 | Sun 3:00 AM | too few trades (142/200) |
| reversal_60m_0.30pct | 612 | 52.5 | 51.8 | $-190.58 | -3.1% | $809.42 | -0.8 | done | can't tell from luck |
| value_ev10 | 369 | 38.5 | 40.5 | $-336.90 | -9.1% | $663.10 | -1.5 | done | can't tell from luck |
| trend_filter | 406 | 46.6 | 50.4 | $-496.66 | -12.2% | $503.34 | -2.5 | done | losing for real |
| value_ev5 | 544 | 40.1 | 42.2 | $-505.43 | -9.3% | $494.57 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 612 | 47.5 | 49.8 | $-577.45 | -9.4% | $422.55 | -2.4 | done | losing for real |
| coinflip | 1144 | 50.1 | 50.9 | $-664.60 | -5.8% | $335.40 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1144 | 49.5 | 51.5 | $-911.97 | -8.0% | $88.03 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 749 | 45.8 | 49.9 | $-926.62 | -12.4% | $73.38 | -3.4 | done | losing for real |
| always_up | 1144 | 47.7 | 50.2 | $-1046.10 | -9.1% | $-46.10 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1696 | 46.9 | 49.4 | $-1509.76 |
| ETH | 1901 | 47.3 | 48.8 | $-1661.08 |
| SOL | 1979 | 48.3 | 49.3 | $-1543.32 |
| XRP | 2039 | 48.8 | 49.1 | $-1024.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
