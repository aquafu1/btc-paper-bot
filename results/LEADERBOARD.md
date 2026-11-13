# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 219 windows, 5726 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 567 | 56.3 | 52.7 | $+203.10 | +3.6% | $1203.10 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 448 | 55.1 | 52.5 | $+82.47 | +1.8% | $1082.47 | +0.4 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 8:15 AM | too few trades (105/200) |
| value_ev10 | 280 | 37.1 | 40.9 | $-368.28 | -13.2% | $631.72 | -1.9 | done | can't tell from luck |
| trend_filter | 299 | 44.5 | 50.1 | $-439.49 | -14.7% | $560.51 | -2.6 | done | losing for real |
| value_ev5 | 408 | 39.2 | 42.7 | $-490.08 | -12.0% | $509.92 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 868 | 50.5 | 51.5 | $-517.93 | -6.0% | $482.07 | -1.8 | done | can't tell from luck |
| coinflip | 868 | 50.0 | 51.0 | $-535.64 | -6.2% | $464.36 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 448 | 44.9 | 49.7 | $-604.31 | -13.5% | $395.69 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 567 | 43.7 | 49.6 | $-870.04 | -15.3% | $129.96 | -3.7 | done | losing for real |
| always_up | 868 | 46.5 | 50.3 | $-1000.24 | -11.5% | $-0.24 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1280 | 46.1 | 49.7 | $-1370.61 |
| ETH | 1424 | 46.5 | 49.0 | $-1387.94 |
| SOL | 1478 | 48.0 | 49.4 | $-1214.66 |
| XRP | 1544 | 49.4 | 49.4 | $-693.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
