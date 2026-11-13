# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 217 windows, 5672 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 560 | 55.9 | 52.7 | $+173.32 | +3.1% | $1173.32 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 443 | 55.1 | 52.6 | $+78.17 | +1.8% | $1078.17 | +0.4 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 7:15 AM | too few trades (105/200) |
| value_ev10 | 280 | 37.1 | 40.9 | $-368.28 | -13.2% | $631.72 | -1.9 | done | can't tell from luck |
| trend_filter | 293 | 44.7 | 50.0 | $-409.07 | -14.0% | $590.93 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 860 | 50.6 | 51.5 | $-486.11 | -5.7% | $513.89 | -1.7 | done | can't tell from luck |
| value_ev5 | 408 | 39.2 | 42.7 | $-490.08 | -12.0% | $509.92 | -2.2 | done | losing for real |
| coinflip | 860 | 50.1 | 51.0 | $-501.17 | -5.8% | $498.83 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 443 | 44.9 | 49.6 | $-583.90 | -13.2% | $416.10 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 560 | 44.1 | 49.7 | $-822.03 | -14.7% | $177.97 | -3.5 | done | losing for real |
| always_up | 860 | 46.4 | 50.3 | $-1008.41 | -11.7% | $-8.41 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1264 | 46.1 | 49.7 | $-1322.56 |
| ETH | 1412 | 46.5 | 48.9 | $-1362.11 |
| SOL | 1462 | 48.0 | 49.4 | $-1180.65 |
| XRP | 1534 | 49.4 | 49.3 | $-678.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
