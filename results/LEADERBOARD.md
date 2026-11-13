# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 222 windows, 5795 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 572 | 56.3 | 52.7 | $+224.02 | +3.9% | $1224.02 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 453 | 55.2 | 52.6 | $+86.78 | +1.9% | $1086.78 | +0.4 | done | can't tell from luck |
| value_ev20 | 106 | 34.9 | 36.9 | $-105.89 | -10.0% | $894.11 | -0.8 | Sun 8:30 AM | too few trades (106/200) |
| value_ev10 | 285 | 38.2 | 40.9 | $-293.69 | -10.3% | $706.31 | -1.5 | done | can't tell from luck |
| value_ev5 | 413 | 40.0 | 42.6 | $-415.49 | -10.1% | $584.51 | -1.8 | done | can't tell from luck |
| trend_filter | 301 | 44.5 | 50.1 | $-435.99 | -14.5% | $564.01 | -2.5 | done | losing for real |
| coinflip | 880 | 50.0 | 51.0 | $-522.51 | -5.9% | $477.49 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 880 | 50.3 | 51.5 | $-523.85 | -6.0% | $476.15 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 453 | 44.8 | 49.7 | $-613.21 | -13.5% | $386.79 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 572 | 43.7 | 49.7 | $-872.26 | -15.2% | $127.74 | -3.7 | done | losing for real |
| always_up | 880 | 46.7 | 50.3 | $-973.16 | -11.1% | $26.84 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1295 | 46.3 | 49.7 | $-1297.02 |
| ETH | 1440 | 46.5 | 49.0 | $-1417.97 |
| SOL | 1498 | 48.1 | 49.4 | $-1146.55 |
| XRP | 1562 | 49.6 | 49.3 | $-583.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
